#smylerCM server
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/gen-link", methods=["GET"])
def genLink():
    pass