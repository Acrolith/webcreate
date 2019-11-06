from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello1():
    return "hello"


@app.route('/')
def hello():
    return render_template("index.html")


app.run(port=5001, host="0.0.0.0")