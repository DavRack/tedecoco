from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def home():
    title = "Dynamic title"
    return flask.render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
