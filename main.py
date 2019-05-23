from flask import Flask, render_template, Response, jsonify, redirect, url_for
from res import stream, names
from res.bot import send_public_message as send_to_webhook
from res.keuzemenu import events, calculate_event_score, calculate_relative_score
import res.data as data
import res.keuzes as keuzes
import os
import sys

import random

app = Flask(__name__)

@app.route('/stream/<channel>')
def stream_data(channel):
    return Response(stream.answer(channel), mimetype="text/event-stream")

@app.route('/')
def main():
    return render_template('index.html', name=names.random_name())

@app.route('/<group>')
def start_in_group(group):
    return render_template('group.html', group=group, name=names.random_name())


# -----------------------------------------------------
# -----------------------------------------------------
# -------------------   API   -------------------------
# -----------------------------------------------------
# -----------------------------------------------------ks

visitors = []

@app.route('/api/v1/<group>/players')
def get_players(group):
    try:
        info = {"players" : list(data.groups[group].players.keys())}
    except KeyError:
        info = {"players" : []}
    return jsonify(info)

@app.route('/api/v1/<group>/leave/<name>')
def leave_group(group, name):
    try:
        del data.groups[group].players[name]
    except KeyError:
        return jsonify({"successful" : False})
    else:    
        stream.send_msg("USER UPDATE", group)
        return jsonify({"successful" : True})

@app.route('/api/v1/creategroup/<name>')
def creategroup(name):
    return jsonify(data.create_group(name))

@app.route('/api/v1/<group>/join/<name>')
def join_group(group, name):
    response = data.joingroup(group, name)
    if response["successful"]:
        stream.send_msg("USER UPDATE", group)
    return jsonify(response)

@app.route('/api/v1/<group>/myrole/<name>/<secretid>')
def discover_role(group, name, secretid):
    info = {"role": None}
    try:
        player = data.groups[group].players[name]
    except KeyError:
        pass
    else:
        if secretid == player.id:
            info = {"role" : player.role}
            
    return jsonify(info)


@app.route('/api/v1/<group>/start')
def start_game(group):
    data.groups[group].started = True
    stream.send_msg("GAME START", group)

    return jsonify({"players" : list(data.groups[group].players.keys()), "locations" : data.groups[group].locations})


# -----------------------------------------------------
# -----------------------------------------------------
# -------------------   BIT   -------------------------
# -----------------------------------------------------
# -----------------------------------------------------

@app.route('/destination')
def location_generator():
    locations = [
        'Elysium', 'Elysium', 'Elysium', 'Elysium', 'Elysium', 'Hell', 'Startup Village', 'Science Park',
        'Unilever', 'Bit', 'America', 'Africa', 'Europe', 'Asia', 'Antarctica', 'the moon', 'poop in an old shoe',
        'stay home', 'another country', 'Amsterdam', 'Amersfoort, the most beautiful city around', 'Almere',
        'Friesland', 'Drente', 'Oudega', 'Marco\'s house', 'rob the bank', 'visit Granny', 'raid Stijn\'s house',
        'the movie', 'some random hostel in Amstelveen', 'Rotterdam', 'Australia', 'die'
    ]
    random_location = locations[random.randint(0, len(locations)-1)]

    return render_template('location.html', location=random_location)

@app.route('/facts/false')
def hidden_fact_false():
    return '<p style="text-align:center">Vincent knows what the location is - but pretends he doesn\'t. He will give you a hint if you Slack him a banana GIF.</p>'

@app.route('/facts/true')
def hidden_fact_true():
    return '<p style="text-align:center">Somewhere in the office, a hint has been hidden. Ironically, you will find it if you manage to fulfill the DeMa goals.</p>'

@app.route('/storytime')
def story_time():
    return render_template('storytime.html')

@app.route('/api/v1/bit/story/check1/<answer_1>/<answer_2>/<answer_3>')
def story_first_check(answer_1, answer_2, answer_3):
    answer = (answer_1.lower() == 'elon musk' and answer_2.lower() == 'deer' and answer_3.lower() == 'errvelousast')
    return jsonify({"answer": answer})

@app.route('/api/v1/bit/story/check2/<answer_1>/<answer_2>/<answer_3>/<answer_4>/<answer_5>')
def story_second_check(answer_1, answer_2, answer_3, answer_4, answer_5):
    response = {"solution": ""}

    if answer_1.lower() == "elon musk" and answer_2.lower() == "deer" and answer_3.lower() == "errvelousast":
        if answer_4.lower() == "elysium" and answer_5.lower() == "mom\'s mayo":
            response = {"solution": "/what-the-sisters-looked-like"}
    
    return jsonify(response)

@app.route('/what-the-sisters-looked-like')
def evil_sister_image():
    send_to_webhook('Somebody got the sisters\' picture.')
    return render_template('sisters.html')


@app.route('/api/v1/keuzes/addevent/<name>/<description>')
def request_event(name, description):
    send_to_webhook(f'Somebody requested the following event:\n```{name}```\n**Description:**```{description}```')
    return jsonify({})

@app.route('/api/v1/keuzes/choose-event/<event_name>/<person>/<yesorno>')
def say_yes_or_no(event_name, person, yesorno):
    send_to_webhook(f"{person} said **{yesorno.upper()}** to the event ```{event_name}```")
    for event in events:
        if event['name'] == event_name:
            event['NA'].remove(person)
            event[yesorno].append(person)
            return jsonify({})

@app.route('/keuzemenu/<name>')
def keuze_menu(name):
    if name not in ["Brom", "Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"]:
        return 'Invalid name.'
    
    print(events)
    options = []

    for event in events:
        option = {
            'name': event['name'],
            'desc': event['desc'],
            'yes': len(event['yes']),
            'probably': len(event['probably']),
            'maybe': len(event['maybe']),
            'hmm': len(event['hmm']),
            'no': len(event['no']),
            'NA': len(event['NA'])
        }
        option['popularity'] = int(calculate_event_score(option)*100)
        option['relative'] = int(calculate_relative_score(option)*100)

        if name in event['yes']:
            option['yourChoice'] = 'omg yes'
        elif name in event['probably']:
            option['yourChoice'] = 'yeah'
        elif name in event['maybe']:
            option['yourChoice'] = 'maybe'
        elif name in event['hmm']:
            option['yourChoice'] = 'hmm'
        elif name in event['no']:
            option['yourChoice'] = 'meh'
        elif name in event['NA']:
            option['yourChoice'] = 'NA'
        else:
            continue
        
        options.append(option)

    options.sort(key=calculate_event_score, reverse=True)

    return render_template('keuzemenu.html', options=options, person=name)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)