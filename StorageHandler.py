class StorageHandler:
    def __init__(self):
        self.__store = [] #for now
    
    def store(self, id, NFT_id, user_wallet_address):
        self.__store.append({"id": id, "NFT_id": NFT_id, "user_wallet_id": user_wallet_address, "is_used": False})
    
    def exists_in_store(self, id):
        items_with_id = [item for item in self.__store if item["id"] == id]
        print(f"in StorageHandler.exists_in_store, id to search for is {id}")
        print(f"self.__store is {self.__store}")
        return len(items_with_id) > 0
    
    def find_in_store(self, id):
        for i in range(len(self.__store)):
            curr_el = self.__store[i]
            if curr_el["id"] == id:
                return curr_el
    
        return None
    
    def is_used(self, id):
        el = self.find_in_store(id)
        print(f"in is_used(), el is {str(el)}")
        is_used = el["is_used"] if el is not None else True #not found is no different from having been used
        return is_used
    
    def markAsUsed(self, id):
        el = self.find_in_store(id)
        if el is not None:
            el["is_used"] = True

