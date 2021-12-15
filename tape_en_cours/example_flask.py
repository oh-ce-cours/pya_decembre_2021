from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/toto")
def toto():
    return "<p>Hello, TOTO!</p>"


@app.route("/hello/<username>")
def say_hello_to_user(username):
    # show the user profile for that user
    return f"Hello {username}"
