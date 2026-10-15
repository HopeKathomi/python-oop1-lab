#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
    


        

coffee = Coffee("small", 200)
if coffee.size not in ["Small", "Medium", "Large"]:
    print("size must be Small, Medium, or Large")
else:
    print(coffee.size)
    coffee.tip()
    print(coffee.price)

