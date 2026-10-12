#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")

while True:
    title = input("Enter book title: ")
    page_count = int(input("Enter page count: "))

    if not isinstance(page_count, int):
        print("page_count must be an integer")

    break

book = Book(title,page_count)
book.turn_page()