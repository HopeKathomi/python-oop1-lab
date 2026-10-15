#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")


book = Book("title",3)
book.turn_page()