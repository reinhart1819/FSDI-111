from flask import Flask  # we imported flask class from flask module

app = Flask(__name__)  # app is an instance


@app.route("/")  # this is a route
def index():  # our view finction
    return "<h1>Hello world</h1>"  # return string


@app.route("/about")
def about():
    me = {
        "first name": "Chris",
        "last name": "Reinahrt"
    }
    return me
