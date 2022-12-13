
class book:
    '''
        The domain entity class.
        Has getters and setters methods.
    '''
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.author = author
        self.title = title

    def get_isbn(self):
        return self.isbn

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_author(self, author):
        self.author = author

    def set_title(self, title):
        self.title = title

    def __str__(self):
        return "Book isbn: " + str(self.isbn) + " || " + str(self.title) + " by " + str(self.author)
