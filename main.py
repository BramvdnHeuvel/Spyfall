from flask import Flask, render_template, Response, jsonify
from res import stream

app = Flask(__name__)

@app.route('/')
def functie():
    return render_template('index.html')

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

visitors = []

@app.route('/api/v1/<group>/players')
def get_players(group):
    global visitors
    return jsonify(visitors)

@app.route('/game/<name>')
def show_game(name):
    global visitors
    visitors.append(name)
    stream.new_msg("USER UPDATE", 'yay')
    return render_template('index.html')

app.run(debug = True)

