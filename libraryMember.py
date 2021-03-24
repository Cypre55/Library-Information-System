import copy
from abc import ABC, abstractmethod
from book import Book
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
            self._reservedBook = copy.deepcopy(orig._reservedBook)
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
    def CheckForReminder(self):
        stro = {
            'MemberID': self._memberID
        }
        cursor.execute(("SELECT GotReminder from members WHERE MemberID = %(MemberID)s"), stro)
        flag = False
        for row  in cursor:
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
        #if(self._reservedBook is not None and self._reservedBook.__ISBN == ISBN):
        isbn = {
        'ISBN': ISBN
        }
        cursor.execute(("SELECT ActiveReservations,ActiveReservedUIDs,AvailableUIDs from RESERVATIONS where ISBN = %(ISBN)s"),isbn)
        stri = ""
        stri2 = ""
        stri3 = ""
        for row in cursor:
            stri = row["ActiveReservations"]
            stri2 = row["ActiveReservedUIDs"]
            stri3 = row["AvailableUIDs"]
        if(stri is not None):
            reserves = stri.split(',')
            reserves = reserves[0:-1]
            reservedbooks = stri2.split(',')
            reservedbooks = reservedbooks[0:-1]
            reservesfinal = reserves.copy()
            print(reserves)
            avails = []
            if(stri3 is not None):
                avails = stri3.split(',')
                avails = avails[0:-1]
            print(avails)
            for active in reserves:
                curr = active.split('*')
                #print(curr[0])
                datex = curr[0].split('-')
                #print(datex)
                intdates = list((int(x) for x in datex))
                tilldate = date(intdates[0], intdates[1], intdates[2])
                memid = curr[1]
                #print(tilldate)
                #print(memid)
                if(tilldate<date.today()):
                    memedid = {
                        'id': memid
                    }
                    cursor.execute(("UPDATE MEMBERS SET ReservedBook = NULL WHERE MemberID = %(id)s"),memedid)
                    db.commit()
                    reservesfinal.remove(active)
                    # pending consider KAROOOOOO
                    avails.append(reservedbooks.pop())
            strfin = ""
            for entry in reservesfinal:
                strfin = strfin+entry+','
            stravailfinal = ""
            for entry in avails:
                stravailfinal  = stravailfinal + entry + ','
            strfin2 = ""
            for entry in reservedbooks:
                strfin2 = strfin2 + entry + ','
            print(stravailfinal)
            print(strfin2)
            if(len(stravailfinal)==0):
                stravailfinal = None
            if(len(strfin)==0):
                newactive = {
                    'newact' : None,
                    'newavail' : stravailfinal,
                    'newstr' : None,
                    'isbn' : ISBN,
                    'noOfCopies' : len(avails)
                }
                cursor.execute(("UPDATE RESERVATIONS SET ActiveReservations = %(newstr)s , AvailableUIDs = %(newavail)s , ActiveReservedUIDs = %(newact)s, NumberOfCopiesAvailable = %(noOfCopies)s WHERE ISBN = %(isbn)s"),newactive)
                db.commit()
            else:
                newactive = {
                    'newstr' : strfin,
                    'isbn' : ISBN,
                    'newavail' : stravailfinal,
                    'newact' : strfin2,
                    'noOfCopies' : len(avails)
                }
                cursor.execute(("UPDATE RESERVATIONS SET ActiveReservations = %(newstr)s , AvailableUIDs = %(newavail)s , ActiveReservedUIDs = %(newact)s, NumberOfCopiesAvailable = %(noOfCopies)s WHERE ISBN = %(isbn)s"),newactive)
                db.commit()
        if False:
            isbn = {
            'ISBN': ISBN
            }
            cursor.execute(("SELECT AvailableUIDs,NumberOfCopiesAvailable from RESERVATIONS where ISBN = %(ISBN)s"),isbn)
            stri = ""
            for row in cursor:
                stri = row["AvailableUIDs"]
            avails = stri.split(',')
            avails = avails[0:-1]
            avails = list(int(x) for x in avails)
            if(len(avails)==0):
                print("Book currently not available, you can make a reservation!")
            else:
                print(avails)
         
    def IssueBook(self, book: Book):
        pass
    def ReserveBook(self, ISBN: str):
        pass
    @abstractmethod
    def CanIssue(self):
        pass
