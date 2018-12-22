from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome_buddy():
    return render_template('main.html')

@app.route('/hello/<name>')
def welcome_name(name):
    return "Hello {}!".format(name)

app.run(debug = True)