import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main Page With Instructions"""
    return "To Send A Message Use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    return "HI " + username


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
