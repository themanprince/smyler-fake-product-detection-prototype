import requests


class NFTHandler:
    
    @staticmethod
    def mintToken(name):
        description = f"purchase by {name}"
        
        #created with users details but stored in my address
        #it will be released when delivery is verified
        recipient =  "email:smylercm@gmail.com:polygon-amoy"
        
        crossmint_collection = "default-polygon-amoy"
        url = f"https://staging.crossmint.com/api/2022-06-09/collections/{crossmint_collection}/nfts"
        
        payload = {
         "metadata": {
            "image": "https://www.crossmint.com/assets/crossmint/logo.png",
            "name": name,
            "description": description
         },
         "recipient": recipient
        }
        
        headers = {
         "X-API-KEY": "sk_staging_5ZVMsvkhQtNpizsbUM4dkmoNrRoMhupYch8dKPciKN5ysz3Q3RYmU837zdZ8YrSUerwxYxvRrZgCRrrTLBQzRowant4vy6fdMVfeC47ZYjBPi9RsYZ5kAY1YD5Cwnt6o519LUMva9WJMh97z4jToxcQgaPFwhF3FEBLkcaWDsEkfACUtRZbNPTHXDwFF3SfhEftViAnjccpUiL3JUc2G1n63",
         "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        json = response.json()
        
        if response.status_code == 200:
            return json["actionId"]
        else:
            print(f"status code is {response.status_code}")
            print(f"ERROR MINT TOKEN REQUEST\n{json['message']}")
            exit(1)
       
    @staticmethod
    def transferToken():
        pass #transfer token from admin wallet to user wallet address
        #thus, transferring ownership

