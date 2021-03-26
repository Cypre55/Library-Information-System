import copy
from abc import ABC, abstractmethod
from book import Book
from bookHandler import BookHandler, SplitTableEntry, JoinTableEntry
from datetime import date, datetime, timedelta
import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "lis"
)
cursor = db.cursor(dictionary = True)

class LibraryMember(ABC):
    def __init__(self, *args):
        ABC.__init__(self)
        if len(args) == 1:
            orig = args[0]
            self._memberID = copy.deepcopy(orig._memberID)
            self._name = copy.deepcopy(orig._name)
            self._listOfBooksIssued = copy.deepcopy(orig._listOfBooksIssued)
            self._reservedBook = copy.deepcopy(orig._reservedBook) # consider changing the name to reserved ISBN?
            self._numberOfBooksIssued = 0
        else:
            self._memberID = args[0]
            self._name = args[1]
            self._listOfBooksIssued = args[2]
            self._reservedBook = args[3]
            self._numberOfBooksIssued = args[4]

    def GetMemberID(self):
        return self._memberID
    def GetName(self):
        return self._name
    def GetNumberOfBookIssued(self):
        return self._numberOfBooksIssued
    def UpdateReservationStatus(self):
        bH = BookHandler.Create()
        bH.OpenBook(self._reservedBook)
        bH.UpdateBook()
        bH.CloseBook()
        self.UpdateFromDatabase()
    def CheckForReminder(self):
        stro = {
            'MemberID': self._memberID
        }
        cursor.execute(("SELECT GotReminder from members WHERE MemberID = %(MemberID)s"), stro)
        flag = False
        for row in cursor:
            flag = row["GotReminder"]
        return flag
    def SearchBook(self):
        searchKey = input("Enter your search string: ")
        searchKey = '\'%' + searchKey + '%\''
        searchBooks = "SELECT DISTINCT ISBN, BookName FROM BOOKS WHERE BookName LIKE "
        cursor.execute(searchBooks + searchKey)
        searchResults = []
        for row in cursor:
            searchResults.append(("{ISBN}".format(ISBN=row['ISBN']),"{BookName}".format(BookName=row['BookName'])))
        print(searchResults)
    def CheckAvailabilityOfBook(self, ISBN: str):
        bH = BookHandler.Create()
        bH.OpenBook(ISBN)
        bH.UpdateBook()
        bH.UpdateDatabase()
        if (self._reservedBook == ISBN):
            if(bH.IsActive(self._memberID)):
                return bH.GetActiveReservedUIDs()
            else:
                return 'Your Reservation is still pending. Pls wait for a few more days'
        else:
            if (bH.IsAvailable(ISBN)):
                return bH.GetAvailableUIDs()
            else:
                if (self._reservedBook == None):
                    return 'Would you like to reserve this book?'
                else:
                    return 'Sorry this book is not available currently, and you already have a reservation'
         
    def IssueBook(self, book: Book):
        bH = BookHandler.Create()
        bH.OpenBook(Book)
        bH.IssueSelected(self._memberID)
        bH.CloseBook()
        self._listOfBooksIssued.append(book.__UID)
        joined_string = ",".join(self._listOfBooksIssued)
        joined_string = joined_string+','
        cursor.execute(str("UPDATE MEMBERS SET ListOfBooksIssued = \""+joined_string+"\" WHERE MemberID = \""+self._memberID+"\""))
        
        db.commit()
        #self.UpdateFromDatabase()

    def ReserveBook(self, ISBN: str):
        bH = BookHandler.Create()
        bH.OpenBook(ISBN)
        bH.CloseBook()
        self.reservedBook = ISBN
        command = "UPDATE MEMBERS SET ReservedBook = %(book)s WHERE MemberID = %(MemberID)s"
        dici = {
            'isbn' : ISBN,
            'memid' : self._memberID
        }
        cursor.execute(command,dici)
        db.commit()

    def UpdateFromDatabase(self):
        selectMember = ("SELECT * FROM MEMBERS WHERE MemberID = %(MemberID)s")
        member = {
            'MemberID' : self._memberID
        }
        cursor.execute(selectMember, member)
        for row in cursor:
            self._memberID = row['MemberID']
            self._name = row['MemberName']
            self._listOfBooksIssued = SplitTableEntry(row['ListOfBooksIssued'])
            self._reservedBook = row['ReservedBook']
    
    @abstractmethod
    def CanIssue(self):
        pass