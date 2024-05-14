class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = [] # list of book objects borrowed by the user.

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id # library id of the user.

    def get_borrowed_books(self):
        return self.__borrowed_books # returning the list of book objects borrowed by the user.

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book) # appending the book object to the __borrowed_books list of the User object.
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.__borrowed_books: # checking if the book object is present in the __borrowed_books list of the User object.
            self.__borrowed_books.remove(book)
            book.return_book()
            return True
        else:
            return False
