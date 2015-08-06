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
        for books in self.shelves:
            print(books)


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


shelf1.add_books(str(harry_potter))
seattle.add_to_shelf(str(shelf1))


while True:

    print('\nWelcome to the Library!\nChoose from the following:\n'
          'L - See a (L)ist of books.\nA - (A)dd a book.\nR - (R)emove a book.\n'
          'Q - (Q)uit')
    user_choice = input('> ').upper()

    if (user_choice == 'Q'):
        sys.exit()
    elif (user_choice == 'L'):
        seattle.report_books()
    elif (user_choice == 'A'):
        while True:
            print('Type the title of the book you wish you add or (Q)uit:')
            title = input('> ').title()
            if (title == 'Q' or title == 'q'):
                break
            else:
                if (title in shelf1.books):
                    print('Title already exists in library.\n')
                else:
                    shelf1.add_books(str(title))
                    seattle.add_to_shelf(str(shelf1))
                    break
    elif (user_choice == 'R'):
        while True:
            print('Type the title of the book you wish to remove or (Q)uit:')
            removed = input('> ').title()
            if (removed == 'Q' or removed == 'q'):
                break
            else:
                if (removed not in shelf1.books):
                    print('Book not found in list.\n')
                else:
                    shelf1.remove_books(removed)
                    seattle.add_to_shelf(str(shelf1))
                    break













