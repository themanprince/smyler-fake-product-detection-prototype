#smylerCM server
from flask import Flask, render_template, request
import uuid
from StorageHandler import StorageHandler
from NFTHandler import NFTHandler


app = Flask(__name__)
store = StorageHandler()

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")



@app.route("/process-order", methods=["POST"])
def process_order():
    order_id = str(uuid.uuid4())
    user_wallet_address = request.form["wallet-address"]
    NFT_for_this_order = NFTHandler.mintToken(order_id)
    
    store.store(id=order_id, NFT_id=NFT_for_this_order, user_wallet_address = user_wallet_address)
    return render_template("barcode.html", id=order_id)


@app.route("/verify", methods=["GET"])
def verify():
    id = request.args.get("id")
    print(f"in /verify route, id that is passed is {id}")
    exists = store.exists_in_store(id)
    print(f"in /verify route, exists is {exists}")
    used = store.is_used(id)
    
    is_authentic = exists and not used
   
    if is_authentic:
        NFTHandler.transferToken() #this is only a prototype and this method has not been implemented
        store.markAsUsed(id)
 
    
    return render_template("output.html", real=is_authentic)
 
   
@app.route("/scan", methods=["GET"])
def scan():
    return render_template("scan-page.html")
    

if __name__ == "__main__":
    app.run()