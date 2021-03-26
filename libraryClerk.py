from book import Book
from libraryMember import LibraryMember
from datetime import date, datetime, timedelta
import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "lis"
)
cursor = db.cursor(dictionary = True)

class LibraryClerk:
    _penaltyRate = 2
    def __init__(self, employeeID, name):
        self._employeeID = employeeID
        self._name = name
    def AddBook(self, bookDetails):
        addBook = ("INSERT INTO BOOKS "
            "VALUES (%(UniqueID)s, %(ISBN)s, %(BookName)s, %(RackNumber)s, %(IssueDate)s, %(IsDisposed)s)")
        dataBook = {
            'UniqueID': None,
            'ISBN': bookDetails[0],
            'BookName': bookDetails[1] + '-by-' + bookDetails[2],
            'RackNumber': bookDetails[3],
            'IssueDate' : bookDetails[4],
            'IsDisposed' : bookDetails[5]
        }
        cursor.execute(addBook, dataBook)
        db.commit()
    def DeleteBook(self, book: Book):
        deleteBook = ("DELETE FROM BOOKS WHERE IsDisposed = 1")
        cursor.execute(deleteBook)
        db.commit()
    def ReturnBook(self, libraryMember : LibraryMember, Book : book):
        #throw error if returning book not issued
        libraryMember._listOfBooksIssued.remove(book.__UID)
        joined_string = ",".join(self._listOfBooksIssued)
        joined_string = joined_string+','
        cursor.execute(str("UPDATE MEMBERS SET ListOfBooksIssued = \""+joined_string+"\" WHERE MemberID = "+libraryMember._memberID))
        db.commit()
        bH = BookHandler.OpenBook(Book)
        bH.ReturnSelected(self._memberID)
        bH.CloseBook()
    def CollectPenalty(self, libraryMember: LibraryMember,  book: Book):
        pass
# lib=LibraryClerk(1,"fds")
# print(lib._penaltyRate)
# lib.AddBook(['420-0000000000','Students and Sourangshu', 'Dan Frown', 6, date(2001,1,1), 0])