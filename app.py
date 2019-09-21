from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method == "GET":
        return render_template("base_view.html")
    elif request.method == "POST":
        return render_template("xml.html")