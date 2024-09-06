#smylerCM server
from flask import Flask, render_template, request
import uuid
from StorageHandler import StorageHandler


app = Flask(__name__)
store = StorageHandler()

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")



@app.route("/process-order", methods=["GET"])
def process_order():
    id = str(uuid.uuid4())
    store.storeID(id)
    print(f"in /process-order, id is {id}")
    link = f"localhost:5000/verify?id={id}"
    return render_template("barcode.html", link=link)


@app.route("/verify", methods=["GET"])
def verify():
    id = request.args.get("id")
    print(f"in /verify route, id that is passed is {id}")
    exists = store.exists_in_store(id)
    print(f"in /verify route, exists is {exists}")
    used = store.is_used(id)
    
    if not used:
        store.markAsUsed(id)
    
    is_authentic = exists and not used
    
    
    return render_template("output.html", real=is_authentic)