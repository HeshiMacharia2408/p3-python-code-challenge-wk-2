class Order:
    def __init__(self, customer, coffee, price):
        if isinstance(customer) and isinstance(coffee) and isinstance(price, (float, int)):
            self._customer = customer
            self._coffee = coffee
            self._price = float(price)
            if price <= 1.0:
                raise ValueError ("Enter a price that is more than 1.0")
            elif price >= 10.0:
                raise ValueError("Enter a price that is less than 10.0.")
            coffee.orders().append(self)
            customer.orders().append(self)
        else:
            raise ValueError("Please type in a correct name for the coffee/order.")
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price
