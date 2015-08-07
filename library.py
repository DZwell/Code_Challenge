# Use object-oriented Python to model a public library
# w/ three classes: Library, Shelf, & Book.
# The library should be aware of a number of distinct shelves.
# Each shelf should know what books it contains.
# Create methods to add and remove a book from a shelf.
# The library should have a method to report all books it contains.


class Library(object):

    def __init__(self, shelves):
        self.shelves = []

    def add_to_shelf(self, shelf):
        self.shelves.append(shelf)
        return self.shelves

    def report_books(self):
        print('Shelf 1:', shelf1.books,
              '\nShelf 2:', shelf2.books,
              '\nShelf 3:', shelf3.books)


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
        return self.title


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


shelf1.add_books(str(harry_potter))
seattle.add_to_shelf(str(shelf1))

shelf2.add_books(str(yellow_garden))
seattle.add_to_shelf(str(shelf2))

shelf3.add_books(str(phantom))
seattle.add_to_shelf(str(shelf3))


if __name__ == '__main__':

    print('\nShelf 1: {}'.format(shelf1))
    print('Shelf 2: {}'.format(shelf2))
    print('Shelf 3: {}'.format(shelf3))

    print("\nAdding 'The Hobbit' to shelf 1:")
    shelf1.add_books(str(hobbit))
    print('Shelf 1: {}'.format(shelf1))

    print("\nAdding 'Websters Dictionary' to shelf 2:")
    shelf2.add_books(str(websters))
    print('Shelf 2: {}'.format(shelf2))

    print("\nAdding 'Python for Dummies' to shelf 3:")
    shelf3.add_books(str(guide))
    print('Shelf 3: {}'.format(shelf3))

    print("\nHere's the Library:")
    seattle.report_books()

    print("\nRemoving 'The Hobbit' from shelf 1:")
    shelf1.remove_books(str(hobbit))
    seattle.report_books()

    print("\nRemoving 'Harry Potter' from shelf 1:")
    shelf1.remove_books(str(harry_potter))
    seattle.report_books()

















