from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def welcome_buddy():
    return "Bliepedie!"

@app.route('/hello/<name>')
def welcome_name(name):
    return "Wat een Snorks zijn jullie Bram & {}".format(name)

@app.route('/pepernoot')
def pepernoot():
    ingredients = ['Water', 'Pepper', 'Nuts', 'Brams broertje', 'Bram']
    return render_template("template.html", lijst=ingredients)

@app.route('/api/pepernoot')
def data_ophalen():
    ingredients = ['Water', 'Pepper', 'Nuts', 'Brams broertje', 'Bram']
    return jsonify(ingredients)

app.run(debug = True)