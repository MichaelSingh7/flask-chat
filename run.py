import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))
    """Add Messages To The `messages` List"""


def get_all_messages():
    "Get All Of The Messages And Separate Them With A `br`"""
    return "<br>".join(messages)



@app.route('/')
def index():
    """Main Page With Instructions"""
    return "To Send A Message Use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display Chat Messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create A New Message And Redirect Back To The Chat Page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
