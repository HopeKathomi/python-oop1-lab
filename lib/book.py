#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = int(page_count)

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")


book = Book("title",3)
book.turn_page()