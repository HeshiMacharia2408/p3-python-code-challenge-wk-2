class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'): 
            if isinstance(value, str):
                self._name = value
            elif len(value) <= 3:
                raise ValueError("Name must be more than 3 characters long.")
            else:
                raise ValueError("Please type in a name.")
        else:
            raise AttributeError("Cannot change the name of the coffee after initialization.")

    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())
    
    def full_price(self):
        total_orders = self.orders()
        if not total_orders:
            return 0
        return sum(order.price for order in total_orders) / len(total_orders)
