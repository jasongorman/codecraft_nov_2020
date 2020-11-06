class Item(object):
    def __init__(self, price, quantity):
        self._quantity = quantity
        self._price = price

    def subtotal(self):
        return self._price * self._quantity