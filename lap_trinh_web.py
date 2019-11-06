from flask import Flask, render_template,send_file

app = Flask(__name__)


@app.route('/hello')
def hello1():
    return "hello"


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/123')
def ledinhnhan():
    path = "dota2.jpg"
    return send_file (path)
app.run(port=5001, host="0.0.0.0")