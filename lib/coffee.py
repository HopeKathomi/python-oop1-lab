#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")

coffee = Coffee(12, 200)
coffee.tip()