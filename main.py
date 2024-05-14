
from book import Book
from user import User
from author import Author

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self, title, author_name, isbn, genre, publication_date):
        author = self.find_or_create_author(author_name)
        book = Book(title, author, isbn, genre, publication_date)
        self.books.append(book)

    def find_or_create_author(self, author_name):
        for author in self.authors:
            if author.get_name() == author_name:
                return author
        author = Author(author_name, "")
        self.authors.append(author)
        return author

    def display_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.get_title()} by {book.get_author().get_name()}")

    def add_user(self, name, library_id):
        user = User(name, library_id)
        self.users.append(user)

    def display_users(self):
        for i, user in enumerate(self.users, 1):
            print(f"{i}. {user.get_name()} (ID: {user.get_library_id()})")

    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors.append(author)

    def display_authors(self):
        for i, author in enumerate(self.authors, 1):
            print(f"{i}. {author.get_name()}")

    def main_menu(self):
        while True:
            print('''
            1.) Book Operations
            2.) User Operations
            3.) Author Operations
            4.) Exit     
            ''')

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print('''
            1.) Add new book
            2.) Borrow a book
            3.) Return a book
            4.) Search for a book
            5.) Display all books
            ''')

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_book(self):
        title = input("Enter book title: ")
        author_name = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        genre = input("Enter genre: ")
        publication_date = input("Enter publication date: ")
        self.add_book(title, author_name, isbn, genre, publication_date)
        print("Book added successfully!")

    # Implement other book operations

    def user_operations(self):
        while True:
            print('''
            1.) Add a new user
            2.) View user details
            3.) Display all users
            4.) GO back to main menu
            ''')

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_user()
            elif choice == "2":
                self.view_user_details()
            elif choice == "3":
                self.display_users()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        self.add_user(name, library_id)
        print("User added successfully!")

    # Implement other user operations

    def author_operations(self):
        while True:
            print('''
            1.) Add a new author
            2.) View author details
            3.) Display all authors
            ''')

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_author()
            elif choice == "2":
                self.view_author_details()
            elif choice == "3":
                self.display_authors()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_new_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        self.add_author(name, biography)
        print("Author added successfully!")

    # Implement other author operations

# Main program
if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.main_menu()
