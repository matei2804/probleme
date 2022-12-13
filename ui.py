from src.Repository.repo import repository
from src.Services.services import service

class ui:
    '''
        Class for the User Interface.
    '''
    def __init__(self, serv: service):
        self.serv = serv

    @staticmethod
    def menu():
        '''
            Method that prints the menu for the user.
        '''
        print("1 - Add a book")
        print("2 - Display the list of books")
        print("3 - Filter the list")
        print("4 - Undo")
        print("5 - Exit")

    def ui_add_book(self):
        '''
            Method for adding a new book to the list of books.
            Asks the user for input and calls the method from the services package.
            Checks if the isbn provided from the user does not appear already in the book list.
        '''
        while True:
            try:
                isbn = input("Isbn: ")
                if int(isbn) > 99 or int(isbn) < 0:
                    continue
                else:
                    if self.serv.check_isbn(isbn) == False:
                        break
                    else:
                        print("Isbn already exists!")
                        continue
            except ValueError:
                print("Invalid command!")

        book_title = input("Title: ")
        author = input("Author: ")
        self.serv.add_book(isbn, book_title, author)

    def ui_display_list_of_books(self):
        '''
            Method that prints the list of books.
        '''
        list = self.serv.display_book_list()
        for i in list:
            print(i)

    def ui_sort_books(self):
        '''
            Method that removes certain books from the list based on the user input.
            Asks the user for input.
            Calls the method from service.
        '''
        word = input("First word from the book title: ")
        self.serv.sort_books(word)

    def ui_undo(self):
        '''
            Method for the undo option.
            Calls the method from service.
        '''
        self.serv.undo_book_list()


    def start(self):
        '''
            Starts the program.
            Asks the user for input and then calls on the methods above based on the input from the user.
        '''
        while True:
            self.menu()
            while True:
                try:
                    n = int(input(">"))
                except ValueError:
                    print("Invalid command!")
                    continue
                if n >= 1 and n <= 5:
                    break
                else:
                    print("Invalid command!")

            if n == 1:
                self.ui_add_book()
            elif n == 2:
                self.ui_display_list_of_books()
            elif n == 3:
                self.ui_sort_books()
            elif n == 4:
                self.ui_undo()
            elif n == 5:
                break
