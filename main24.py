class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"Book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Book '{self.title}' by {self.author} is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Book '{self.title}' by {self.author} has been checked in.")
        else:
            print(f"Book '{self.title}' by {self.author} is not checked out.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Catalog:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book.title} by {book.author} ({book.year_published}) {'(Checked Out)' if book.checked_out else ''}")

if __name__ == "__main__":
    library = Library()
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("1984", "George Orwell", 1949))

    library.display_books()
    print()

    library.books[0].check_out()
    library.books[1].check_out()
    library.books[0].check_in()

    library.display_books()
