#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
    
    def specify_size(self, size):

        if size not in ["small", "medium", "large"]:
            raise ValueError("size must be Small, Medium, or Large")
        else:
            self.size = size

coffee = Coffee(12, 200)

coffee.specify_size("small")
print(coffee.size)
coffee.tip()

