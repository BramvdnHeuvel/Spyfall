from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def functie():
    return render_template('spyfall.html',names=['sam','mark'],locations=['strand', 'duinen'])

app.run(debug = True)

