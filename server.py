#smylerCM server
from flask import Flask, render_template
import uuid
from StorageHandler import StorageHandler


app = Flask(__name__)
store = StorageHandler()

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/process-order", methods=["GET"])
def process_order():
    id = uuid.uuid4()
    store.storeID(id)
    link = f"localhost:5000/verify?id={id}"
    return render_template("barcode.html", link=link)