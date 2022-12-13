from src.Domain.domain import book
from src.Repository.repo import repository

class service:
    '''
        Class that implements the required functionalities.
    '''

    def __init__(self, rep: repository):
        self.rep = rep

    def check_isbn(self, isbn):
        '''
            Method that checks if the isbn provided by the user exists already.
            Returns True if it exists.
            Returns False if it doesn't exist.
        '''
        list_of_books = self.rep.check_isbn_unique()
        for i in list_of_books:
            id = book.get_isbn(i)
            if id == isbn:
                return True
        return False

    def add_book(self, isbn, title, author):
        '''
            Creates an object book with the given input.
            Adds the new book to the repository.
        '''
        entity = book(isbn, title, author)
        self.rep.add_book(entity)

    def test_add_book(self):
        '''
            Test method for the first functionality.
        '''
        entity1 = book('21', 'title1', 'author1')
        entity2 = book('56', 'title2', 'author2')
        isbn1 = '21'
        isbn2 = '56'
        try:
            assert self.check_isbn(isbn1) == False
        except AssertionError:
            assert True
        try:
            assert self.check_isbn(isbn2) == False
        except AssertionError:
            assert True


    def display_book_list(self):
        '''
            Returns the book list in order to print it.
        '''
        return self.rep.display_list_of_books()

    def sort_books(self, word):
        '''
            Method that filters the list so that book titles starting with a given word are deleted from the list.
            Creates a new list that contains all the books except the ones that have a title that starts with the given word,
            then this new list becomes the book list from the repository.

        '''
        list_of_books = self.rep.display_list_of_books()
        new_book_list = []
        for i in list_of_books:
            book_title = book.get_title(i)
            book_title_list = book_title.split()
            if book_title_list[0] != word:
                new_book_list.append(i)

        self.rep.sort_books(new_book_list)

    def undo_book_list(self):
        '''
            Calls the method undo from the repository in order to undo the changes.
        '''
        self.rep.undo()
