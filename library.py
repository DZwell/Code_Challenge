# Use object-oriented Python to model a public library
# w/ three classes: Library, Shelf, & Book.
# The library should be aware of a number of distinct shelves.
# Each shelf should know what books it contains.
# Create methods to add and remove a book from a shelf.
# The library should have a method to report all books it contains.


class Library(object):
    '''Class to hold shelves of books'''

    def __init__(self, shelves):
        self.shelves = []

    def add_shelves(self, shelf):
        self.shelves.append(shelf)
        return self.shelves

    def report_books(self):
        print('Shelf 1:', shelf1.books,
              '\nShelf 2:', shelf2.books,
              '\nShelf 3:', shelf3.books)


class Shelf(object):
    '''Class to hold books'''

    def __init__(self, books):
        self.books = []

    def __str__(self):
        return str(self.books)

    def add_books(self, book):
        if (book in self.books):
            Book.book_id += 1
            self.books.append(book + '(%d)' % (Book.book_id))
            return self.books
        else:
            self.books.append(book)
            return self.books

    def remove_books(self, book):
        if (book not in self.books):
            print('Title does not exist on shelf.')
        else:
            self.books.remove(book)
            return self.books


class Book(object):

    #variable to store unique id for multiple copies of book.
    book_id = 0

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


if __name__ == '__main__':

    seattle = Library([])

    shelf1 = Shelf([])
    shelf2 = Shelf([])
    shelf3 = Shelf([])

    harry_potter = Book('Harry Potter')
    yellow_garden = Book('The Yellow Garden')
    phantom = Book('The Phantom Toll Booth')
    hobbit = Book('The Hobbit')
    websters = Book('Websters Dictionary')
    guide = Book('Python for Dummies')
    jane = Book('Sense and Sensibility')

    shelf1.add_books(str(harry_potter))
    seattle.add_shelves(str(shelf1))

    shelf2.add_books(str(yellow_garden))
    seattle.add_shelves(str(shelf2))

    shelf3.add_books(str(phantom))
    seattle.add_shelves(str(shelf3))
    seattle.report_books()

    print("\nAdding 'The Hobbit' to shelf 1:")
    shelf1.add_books(str(hobbit))
    print('Shelf 1: {}'.format(shelf1))

    print("\nAdding 'Websters Dictionary' to shelf 2:")
    shelf2.add_books(str(websters))
    print('Shelf 2: {}'.format(shelf2))

    print('\nAdding additional copies of existent book:')
    shelf2.add_books(str(yellow_garden))
    print('Shelf 2: {}'.format(shelf2))
    shelf2.add_books(str(yellow_garden))
    print('Shelf 2: {}'.format(shelf2))

    print('\nRemoving copy of existent book:')
    shelf2.remove_books(str(yellow_garden))
    print('Shelf 2: {}'.format(shelf2))
    shelf2.remove_books('The Yellow Garden(1)')
    print('Shelf 2: {}'.format(shelf2))

    print('\nTrying to remove non-existent book:')
    shelf3.remove_books(str(jane))

    print("\nRemoving 'The Hobbit' from shelf 1:")
    shelf1.remove_books(str(hobbit))
    seattle.report_books()

    print("\nRemoving 'Harry Potter' from shelf 1:")
    shelf1.remove_books(str(harry_potter))
    seattle.report_books()





