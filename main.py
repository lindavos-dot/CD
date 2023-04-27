# Import what we need from flask
from flask import Flask


# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/winc')
def winc():
    return 'Whoohooo, laatste opdracht van winc!'

# Aangepast nadat Github Actions/run-tests.yml groen is voor: run-tests, Deploy, Build

@app.route('/hoera')
def winc():
    return 'Hoera, als je dit ziet dan werkt het!'