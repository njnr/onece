from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return "<P> hello world </P>"

@app.route("/user/<username>")
def user(username):
    return "<p> hell,%s </p>" %username

@app.route("/html/<username>")
def html(username):
    return render_template('index.html', name=username)


if __name__ == "__main__":
    manager.run()
