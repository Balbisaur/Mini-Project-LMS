class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            return True
        else:
            return False