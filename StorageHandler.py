class StorageHandler:
    def __init__(self):
        self.__store = [] #for now
    
    def storeID(self, id):
        self.__store.append({"id": id, "is_used": False})
    
    def exists_in_store(self, id):
        items_with_id = [item for item in self.__store if item["id"] == id]
        
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

