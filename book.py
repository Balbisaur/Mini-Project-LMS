class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True 

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__availability

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        else:
            return False

    def return_book(self):
        self.__availability = True
