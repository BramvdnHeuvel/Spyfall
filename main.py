from flask import Flask, render_template, Response, jsonify
from res import stream, names
import res.data as data
import os
import sys

app = Flask(__name__)

@app.route('/stream/<channel>')
def stream_data(channel):
    return Response(stream.answer(channel), mimetype="text/event-stream")

@app.route('/')
def main():
    return render_template('index.html', name=names.random_name())


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
    id = data.create_group(name)
    return jsonify({"successful" : True, "groupname" : id})

@app.route('/api/v1/<group>/join/<name>')
def join_group(group, name):
    response = data.joingroup(group, name)
    if response["successful"]:
        stream.send_msg("USER UPDATE", group)
    return jsonify(response)

@app.route('/api/v1/<group>/myrole/<name>')
def discover_role(group, name):
    try:
        info = {"role" : data.groups[group].players[name].role}
    except KeyError:
        info = {"role" : None}
    return jsonify(info)

@app.route('/api/v1/<group>/start')
def start_game(group):
    data.groups[group].started = True
    stream.send_msg("GAME START", group)

    return jsonify({"players" : list(data.groups[group].players.keys()), "locations" : data.groups[group].locations})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)