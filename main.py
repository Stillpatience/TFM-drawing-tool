from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    #string = request.url
    #split_string = (string.split("/?")[1]).split("&")
    #x = split_string[0].split("=")[1]
    #y = split_string[0].split("=")[1]
    return render_template("base_view.html")

