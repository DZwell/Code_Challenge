# Use object-oriented Python to model a public library
# w/ three classes: Library, Shelf, & Book.
# The library should be aware of a number of distinct shelves.
# Each shelf should know what books it contains.
# Create methods to add and remove a book from a shelf.
# The library should have a method to report all books it contains.
import sys


class Library(object):

    def __init__(self, shelves):
        self.shelves = []

    def add_to_shelf(self, shelf):
        self.shelves.append(shelf)
        return self.shelves

    def report_books(self):
        print(self.shelves)


class Shelf(object):

    def __init__(self, books):
        self.books = []

    def __str__(self):
        return str(self.books)

    def add_books(self, book):
        self.books.append(book)
        return self.books

    def remove_books(self, book):
        self.books.remove(book)
        return self.books


class Book(object):

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return str(self.title)


seattle = Library([])

shelf1 = Shelf([])
shelf2 = Shelf([])

harry_potter = Book('Harry Potter')
yellow_garden = Book('The Yellow Garden')
golden_compass = Book('The Golden Compass')


shelf1.add_books(str(harry_potter))
shelf1.add_books(str(yellow_garden))

seattle.add_to_shelf(str(shelf1))

seattle.report_books()


seattle.add_to_shelf(str(shelf1))

seattle.report_books()

shelf2.add_books(str(golden_compass))

seattle.add_to_shelf(str(shelf2))

seattle.report_books()

shelf1.remove_books(str(harry_potter))

seattle.report_books()

shelf1.add_books(str(harry_potter))


seattle.report_books()










