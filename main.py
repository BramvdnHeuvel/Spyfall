from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome_buddy():
    names = ["Bram", "Sam", "Sietse", "Mick", "Larissa", "Mark"]
    locations = ["Supermarkt", "Snackbar", "Het huis van Brams imaginaire vriendin", "Diemen-zuid"]
    return render_template('spyfall.html', names = names, locations = locations)

@app.route('/hello/<name>')
def welcome_name(name):
    return "Hello {}!".format(name)

@app.route('/spyfall.html')
def goto_spyfall():
    return render_template('spyfall.html')

app.run(debug = True)