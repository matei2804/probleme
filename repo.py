import copy
from src.Domain.domain import book
import pickle

class repository:
    '''
        Repository class whose job it is to store the domain entity instances.
    '''

    def __init__(self):
        '''
            Creates a book list with 10 elements already added.
            Creates another list that is used in order to undo operations.
        '''
        self.book_list = [
                        book('21', 'The Adventures of Huckleberry Finn',  'Mark Twain'),
                        book('56', 'The Great Gatsby', 'F. Scott Fitzgerald'),
                        book('32', 'Anna Karenina', 'Leo Tolstoy'),
                        book('12', 'Madame Bovary', 'Gustave Flaubert'),
                        book('53', 'Moby Dick', 'Herman Melville'),
                        book('93', 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez'),
                        book('43', '1984', 'George Orwell'),
                        book('73', 'Brave New World', 'Aldous Huxley'),
                        book('72', 'The Feast of the Goat', 'Mario Vargas Llosa'),
                        book('36', 'In Search of Lost Time', 'Marcel Proust')
                        ]

        self.undo_book_list = [
                        [book('21', 'The Adventures of Huckleberry Finn',  'Mark Twain'),
                        book('56', 'The Great Gatsby', 'F. Scott Fitzgerald'),
                        book('32', 'Anna Karenina', 'Leo Tolstoy'),
                        book('12', 'Madame Bovary', 'Gustave Flaubert'),
                        book('53', 'Moby Dick', 'Herman Melville'),
                        book('93', 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez'),
                        book('43', '1984', 'George Orwell'),
                        book('73', 'Brave New World', 'Aldous Huxley'),
                        book('72', 'The Feast of the Goat', 'Mario Vargas Llosa'),
                        book('36', 'In Search of Lost Time', 'Marcel Proust')]
                              ]

    def check_isbn_unique(self):
        '''
            Method that returns the book list.
        '''
        return self.book_list

    def add_book(self, book):
        '''
            Method that adds another object to the list.
        '''
        self.book_list.append(book)
        list = copy.deepcopy(self.book_list)
        self.undo_book_list.append(list)

    def display_list_of_books(self):
        '''
            Method that returns the book list.
        '''
        return self.book_list

    def sort_books(self, new_book_list):
        '''
            Method that changes the book list with the new sorted list.
        '''
        self.book_list = new_book_list.copy()
        list = copy.deepcopy(new_book_list)
        self.undo_book_list.append(list)


    def undo(self):
        '''
            Method that changes the book list in order to undo the last operation.
        '''
        if len(self.undo_book_list) >= 2:
            self.undo_book_list.pop()
            self.book_list = self.undo_book_list[-1]

class repository_txt(repository):
    '''
        Repository for the txt file implementation.
    '''

    def __init__(self, txt_file):
        self.txt_file = txt_file
        super().__init__()
        self.book_list = []
        self.load_from_file()
        self.undo_book_list.append(self.book_list.copy())

    def load_from_file(self):
        '''
            Reads the content from the file.
        '''
        with open(self.txt_file, 'r') as f:
            for line in f:
                line = line.split(',')
                isbn = line[0]
                title = line[1]
                author = line[2]
                self.book_list.append(book(isbn, title, author))

    def store_to_file(self):
        '''
            Writes the content to the file.
        '''
        with open(self.txt_file, 'w') as f:
            for v in self.book_list:
                stri = str(v.get_isbn()) + ',' + v.get_title() + ',' + v.get_author() + ',\n'
                f.write(stri)

    def add_book(self, book):
        super().add_book(book)
        self.store_to_file()

    def sort_books(self, new_book_list):
        super().sort_books(new_book_list)
        self.store_to_file()

    def undo(self):
        super().undo()
        self.store_to_file()

class repository_binary(repository):
    def __init__(self, binary_file):
        self.binary_file = binary_file
        super().__init__()
        self.book_list = []
        self.unpickle_file()

    def pickle_file(self):
        pickle_out = open(self.binary_file, 'wb')
        pickle.dump(self.book_list, pickle_out)
        pickle_out.close()

    def unpickle_file(self):
        pickle_in = open(self.binary_file, 'rb')
        self.book_list = pickle.load(pickle_in)

    def add_book(self, book):
        super().add_book(book)
        self.pickle_file()

    def sort_books(self, new_book_list):
        super().sort_books(new_book_list)
        self.pickle_file()

    def undo(self):
        super().undo()
        self.pickle_file()