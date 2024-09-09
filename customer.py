class Customer:
    _all_customers = []  

    def __init__(self, name):
        self.name = name 
        self._orders = []
        Customer._all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        elif len(value) <= 1:
            raise ValueError("Name must be more than one character.")
        elif len(value) >= 15:
            raise ValueError("Name must be less than 15 characters.")
        else:
            raise ValueError("Please type in a name.")
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        if isinstance(coffee) and isinstance(price, (float, int)):
            order = order(self, coffee, float(price))
            self._orders.append(order)
            return order
        else:
            raise ValueError("Invalid coffee or price")

    @classmethod
    def most_aficionado(cls, coffee):
        customers_spending = {customer: 0 for customer in cls._all_customers}
        for customer in cls._all_customers:
            for order in customer.orders():
                if order.coffee == coffee:
                    customers_spending[customer] += order.price
        return max(customers_spending, key=customers_spending.get) if customers_spending else None
