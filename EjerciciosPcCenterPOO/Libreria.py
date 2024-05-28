class Library:
    total_books = 0
    books = []

    @classmethod
    def add_book(cls, book_name):
        cls.total_books += 1
        cls.books.append(book_name)

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @classmethod
    def print_books(cls):
        print("Lista de libros en la biblioteca:")
        for book in cls.books:
            print(book)


library1 = Library()
library2 = Library()
library3 = Library()

library1.add_book("Libro 1")
library2.add_book("Libro 2")
library3.add_book("Libro 3")

print("Número total de libros en la biblioteca:", Library.get_total_books())
Library.print_books()