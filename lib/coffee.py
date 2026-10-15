#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.prize += 1
    
    def specify_size(self, size):

        if size not in ["Small", "Medium", "Large"]:
           print("size must be Small, Medium, or Large")
        else:
            self.size = size

coffee = Coffee(12, 200)

coffee.specify_size("small")
print(coffee.size)
coffee.tip()
print(coffee.size)

