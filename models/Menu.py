class Menu:
    def __init__(self):
        self._item_list = []
        
    def get_item_list(self):
        return self._item_list
    
    def add_item(self, item):
        self._item_list.append(item)
        
    def doesItemExist(self, name):
        for item in self.get_item_list():
            if name == item.get_name():
                return True
        return False