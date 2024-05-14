class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self): # Returning the name of the author
        return self.__name

    def get_biography(self): # Returning the biography of the author
        return self.__biography
