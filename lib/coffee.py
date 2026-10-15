#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
    
    def specify_size(self, size):
        
        if size not in ["small", "medium", "large"]:
            raise ValueError("size must be small, medium or Large")
        else:
            self.size = size

coffee = Coffee(12, 200)

while True:
    print("Enter 'q' to quit")
    s = input("Enter size: ")
    coffee.specify_size(s)

    if s == "q":
        break

    # print("You entered: ", s)

coffee.tip()

