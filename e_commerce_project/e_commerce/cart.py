"""
    EEMI E-commerce project, 2025
    E-commerce website in Django
    file description:
    This file handles the cart functionalities
"""

from .models import product

class cart:
    def __init__(self):
        self.items = {}

    def add(self, product_id, quantity=1):
        product_obj = product.objects.get(id=product_id)
        if product_id not in self.items:
            self.items[product_id] = {'product': product_obj, 'quantity': quantity}
        else:
            self.items[product_id]['quantity'] += quantity

    def remove(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def clear(self):
        self.items = {}

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += float(item['product'].price) * item['quantity']
        return total

    def increase_quantity(self, product_id):
        if product_id in self.items:
            self.items[product_id]['quantity'] += 1

    def decrease_quantity(self, product_id):
        if product_id in self.items:
            if self.items[product_id]['quantity'] > 1:
                self.items[product_id]['quantity'] -= 1
            else:
                del self.items[product_id]