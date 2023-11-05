class MenuItem:
    def __init__(self, name, price):
        self.set_name(name)
        self.set_price(price)
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_name(self, name):
        self._name = name
    
    def set_price(self, price):
        self._price = price