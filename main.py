from flask import Flask, render_template
from data import filmy

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/filmy')
def get_filmy():
    return render_template('filmy.html', filmy=filmy)


if __name__ == '__main__':
    app.run(debug=True)
