from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Dynamic title"
    return render_template('home.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)