from book import Book
from libraryMember import LibraryMember
from underGraduateStudent import UnderGraduateStudent
from bookHandler import BookHandler, JoinTableEntry, SplitTableEntry
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
        cursor.execute("SELECT ISBN FROM RESERVATIONS")
        flag=0
        for row in cursor:
            if(bookDetails[0] == row['ISBN']):
                flag=1
                break
        
        if (flag == 0):
            cursor.execute("SELECT UniqueID FROM BOOKS WHERE ISBN = " + bookDetails[0])
            row = cursor.fetchone()
            addISBN = ("INSERT INTO RESERVATIONS "
            "VALUES (%(ISBN)s, %(AvailableUIDs)s, %(TakenUIDs)s, %(PendingReservations)s, %(ActiveReservations)s, %(ActiveReservedUIDs)s, %(NumberOfCopiesAvailable)s)")
            dataISBN = {
                'ISBN' : bookDetails[0],
                'AvailableUIDs' : row['UniqueID'] + ',',
                'TakenUIDs' : None,
                'PendingReservations' : None,
                'ActiveReservations' : None,
                'ActiveReservedUIDs' : None,
                'NumberOfCopiesAvailable' : 1
            }
            cursor.execute(addISBN,dataISBN)
            db.commit()

    def DeleteBook(self, book: Book):
        deleteBook = ("DELETE FROM BOOKS WHERE IsDisposed = 1")
        cursor.execute(deleteBook)
        db.commit()
        
        # implement updation of reservations table also accordingly
    def ReturnBook(self, libraryMember : LibraryMember, book : Book):
        #throw error if returning book not issued
        libraryMember._listOfBooksIssued.remove(str(book.GetUID()))
        joined_string = JoinTableEntry(libraryMember._listOfBooksIssued)
        memberUpdate = ("UPDATE MEMBERS SET ListOfBooksIssued = %(ListOfBooks)s WHERE MemberID = %(MemberID)s")
        listOfBooks = {
            'ListOfBooks' : joined_string,
            'MemberID' : libraryMember._memberID
        }
        cursor.execute(memberUpdate, listOfBooks)
        db.commit()
        bH = BookHandler.Create()
        bH.OpenBook(book)
        bH.ReturnSelected(libraryMember._memberID)
        bH.CloseBook()
    def CollectPenalty(self, libraryMember: LibraryMember,  book: Book):
        pass
# lib=LibraryClerk(1,"fds")
# print(lib._penaltyRate)
# mem = UnderGraduateStudent('19CS10073', 'Rajat', ['4'], '918-0789532743', 0)
# b= Book(4, '988-0789032742', date.today(), None)
# lib.ReturnBook(mem, b)