from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome_buddy():
    return "Bliepedie!"

@app.route('/hello/<name>')
def welcome_name(name):
    return "Wat een Snork ben je {}".format(name)\

@app.route('/pepernoot')
def pepernoot():
    return render_template("template.html")

app.run(debug = True)