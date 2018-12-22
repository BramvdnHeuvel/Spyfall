from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def functie():
    return render_template('spyfall.html',names=['sam','mark'],locations=['strand', 'duinen'])

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/welcome')
def welcome_buddy():
    names = ["Bram", "Sam", "Sietse", "Mick", "Larissa", "Mark"]
    locations = ["Supermarkt", "Snackbar", "Het huis van Brams imaginaire vriendin", "Diemen-zuid"]
    return render_template('spyfall.html', names = names, locations = locations)

app.run(debug = True)

