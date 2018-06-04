from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world!"


@app.route("/hello")
def hello():
    return "hello"

@app.route("/world")
def world():
    return "world"


@app.route("/HELLO WORLD")
def helloworld():
    return "HELLO WORLD"


@app.route("/dlrow olleh")
def reverse():
    return "dlrow olleh"


if __name__ == "__main__":
    app.run()