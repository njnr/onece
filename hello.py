from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return "<P> hello world </P>"

@app.route("/user/<username>")
def user(username):
    return "<p> hell,%s </p>" %username


if __name__ == "__main__":
    manager.run()

    
