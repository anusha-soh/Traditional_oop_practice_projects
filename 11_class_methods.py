# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self , name):
        self.name = name
        Book.increment_count()


    @classmethod
    def increment_count(cls):
        cls.total_books += 1
        
b1 = Book("WIN IN LIFE")
b2 = Book("THE LAST LIGHT")
b3 = Book("ONE MORE DAY")
b4 = Book("THE SRCRET")

print(Book.total_books)