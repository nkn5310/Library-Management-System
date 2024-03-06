import csv

# Main classes for library including Book, Patron, Transaction, and Library class along with user interface
class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = str(isbn)
        self.quantity = quantity

    def display_details(self):
        return [self.title, self.author, self.isbn, self.quantity]

class Patron:
    def __init__(self, name, patron_id, contact_info):
        self.name = name
        self.patron_id = patron_id
        self.contact_info = contact_info

    def display_details(self):
        return [self.name, self.patron_id, self.contact_info]

class Transaction:
    def __init__(self, book, patron):
        self.book = book
        self.patron = patron
        self.checked_out = False

    def check_out(self):
        if self.book.quantity > 0:
            self.book.quantity -= 1
            self.checked_out = True
            print("Book '{}' checked out to '{}'".format(self.book.title, self.patron.name))
        else:
            print("Sorry, '{}' is out of stock.".format(self.book.title))

    def check_in(self):
        if self.checked_out:
            self.book.quantity += 1
            self.checked_out = False
            print("Book '{}' checked in.".format(self.book.title))
        else:
            print("Book '{}' is not checked out.".format(self.book.title))

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("{} added.".format(book.title))

    def add_patron(self, patron):
        self.patrons.append(patron)
        print("Patron added.")

    def update_book(self, isbn, new_quantity):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity = new_quantity
                print("Book quantity updated.")
                return
        print("Book not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            return []
        book_details = [["Title", "Author", "ISBN", "Quantity"]]
        for book in self.books:
            book_details.append(book.display_details())
        return book_details

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return
        for patron in self.patrons:
            patron.display_details()

def main():
    library = Library()
    book1 = Book("magic_school_bus", "sum lady", 6534787, 3)
    book2 = Book("the_odyssey", "homer", 4376086, 2)
    book3 = Book("romeo_and_juliet", "shakespeare", 9473832, 1)
    book4 = Book("harry_potter", "j.k. rowling", 567898765, 2)
    book5 = Book("ispy", "jean marzollo", 42762389, 0)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    patron1 = Patron("Alice", 1, "alice@example.com")
    patron2 = Patron("Bob", 2, "bob@example.com")
    patron3 = Patron("Nick", 3, "nick@example.com")
    library.add_patron(patron1)
    library.add_patron(patron2)
    library.add_patron(patron3)

    file_path = 'library_books.csv'
    book_details = library.display_books()
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(book_details)
        print(f"Library books exported to {file_path}")

if __name__ == "__main__":
    main()