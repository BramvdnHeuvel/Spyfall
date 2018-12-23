from flask import Flask, render_template, Response, jsonify
from res import stream
import res.data as data

app = Flask(__name__)

@app.route('/')
def functie():
    stream.send_msg('Hey there, kid!','yay')
    return jsonify()

@app.route('/stream/<channel>')
def stream_data(channel):
    return Response(stream.answer(channel), mimetype="text/event-stream")

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/welcome')
def welcome_buddy():
    names = ["Bram", "Sam", "Sietse", "Mick", "Larissa", "Mark"]
    locations = ["Supermarkt", "Snackbar", "Het huis van Brams imaginaire vriendin", "Diemen-zuid"]
    return render_template('spyfall.html', names = names, locations = locations)

@app.route('/index')
def view_index():
    return render_template('index.html')


# -----------------------------------------------------
# -----------------------------------------------------
# -------------------   API   -------------------------
# -----------------------------------------------------
# -----------------------------------------------------

visitors = []

@app.route('/api/v1/<group>/players')
def get_players(group):
    try:
        info = {"players" : list(data.groups[group].players.keys())}
    except KeyError:
        info = {"players" : []}
    return jsonify(info)
    # TODO: Return a list of players in a given group
    # The client expects a dictionary with at least the following properties:
    # {
    #   players - (List of player objects)
    # }

@app.route('/api/v1/<group>/leave/<name>')
def leave_group(group, name):
    try:
        del data.groups[group].players[name]
        return jsonify({"succesful" : True})
    except KeyError:
        return jsonify({"succesful" : False})
    # TODO: Kick a given player from a given group
    # The client expects a dictionary with at least the following properties:
    # {
    #   successful - (Bool whether the kick was succesful)
    # }

@app.route('/api/v1/creategroup/<name>')
def creategroup(name):
    id = data.create_group(name)
    return jsonify({"succesful" : True, "groupname" : id})

@app.route('/api/v1/<group>/join/<name>')
def join_group(group, name):
    stream.send_msg("USER UPDATE", group)
    return jsonify(data.joingroup(group, name))
    # TODO: Join a group if there isn't already an (active) player with that name.
    # The client expects a dictionary with at least the following properties:
    # {
    #   successful  - (Bool whether the kick was succesful)
    #   players     - (List of player objects)
    # }

@app.route('/api/v1/<group>/myrole/<name>')
def discover_role(group, name):
    try:
        info = {"role" : data.groups[group].players[name].role}
    except KeyError:
        info = {"role" : None}
    return jsonify(info)
    pass # TODO: Receive a one-time object with the player's role and location
    # The client expects a dictionary with at least the following properties:
    # {
    #   location    - (String. Unknown if the player is the spy)
    #   role        - (String. Equal to "Spy" if the player is the spy)
    # }
    # If the player's role has already been discovered, send an error value.

@app.route('/api/v1/<group>/start')
def start_game(group):
    data.groups[group].started = True
    stream.send_msg("GAME STARTED", group)

    return jsonify({"players" : list(data.groups[group].players.keys()), "locations" : data.groups[group].locations})


@app.route('/game/<name>')
def show_game(name):
    global visitors
    visitors.append(name)
    stream.send_msg("USER UPDATE", 'yay')
    return render_template('index.html', name=name)


app.run(debug = True)