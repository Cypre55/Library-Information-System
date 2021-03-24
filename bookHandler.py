import mysql.connector as mysql
from book import Book
class BookHandler:
    __instance = None
    __currISBN = None
    __currUID = None
    __available = None
    __waitList = None
    __readyToClaimUsers = None
    __readyToClaimUsers = None
    __numberOfCopies = None
    @staticmethod 
    # Static Access Method
    def Create():
        if BookHandler.__instance == None:
            BookHandler()
        return BookHandler.__instance
    # Virtually private constructor
    def __init__(self):
        if BookHandler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BookHandler.__instance = self
    @staticmethod 
    def OpenBook(book: Book):
        BookHandler.__currISBN = book.__ISBN # Accessing private member, be careful
        BookHandler.__currUID = book.__UID # Accessing private member, be careful
        '''
        Fill the other data members using the database
        '''
    def UpdateBook(self):
        pass
    def CloseBook(self):
        BookHandler.__instance = None
        BookHandler.__currISBN = None
        BookHandler.__currUID = None
        BookHandler.__available = None
        BookHandler.__waitList = None
        BookHandler.__readyToClaimUsers = None
        BookHandler.__readyToClaimUsers = None
        BookHandler.__numberOfCopies = None
