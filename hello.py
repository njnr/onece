from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<P> hello world </P>"

@app.route("/user/<username>")
def user(username):
    return "<p> hell,%s </p>" %username


if __name__ == "__main__":
    app.run()

    
