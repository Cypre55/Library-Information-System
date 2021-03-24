from libraryClerk import LibraryClerk
from libraryMember import LibraryMember
from underGraduateStudent import UnderGraduateStudent
from cryptography.fernet import Fernet
from datetime import date, datetime, timedelta
import mysql.connector as mysql
import base64
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "lis"
)

def encode_message(message):
    key2 = open("secret.key", "rb").read()
    fernet = Fernet(key2)
    encMessage = fernet.encrypt(message.encode())
    return encMessage
def decode_message(encMessage):
    key2 = open("secret.key", "rb").read()
    fernet = Fernet(key2)
    decMessage = fernet.decrypt(encMessage)
    return decMessage.decode()
cursor = db.cursor(dictionary = True)
cursor.execute('SELECT * FROM MEMBERS')
for row in cursor:
    print(decode_message(bytes((row["PassWd"]),'utf-8')))
class Librarian(LibraryClerk):
    __reminder = False
    
    def __init__(self, employeeID, name):
        LibraryClerk.__init__(self, employeeID, name)
    
    def AddMember(self, libraryMember: LibraryMember, passwd):
        addMember = ("INSERT INTO MEMBERS "
                   "VALUES (%(MemberID)s, %(MemberName)s, %(MemberType)s, %(ListOfBooksIssued)s, %(ReservedBook)s, %(GotReminder)s, %(PassWd)s)")
        print(str(type(libraryMember)))
        type_shortHand = {
            '<class \'underGraduateStudent.UnderGraduateStudent\'>':'UG',
            '<class \'postGraduateStudent.PostGraduateStudent\'>':'PG',
            '<class \'researchScholar.ResearchScholar\'>':'RS',
            '<class \'facultyMember.FacultyMember\'>':'FM'
        }
        dataMember = {
            'MemberID': libraryMember.GetMemberID(),
            'MemberName': libraryMember.GetName(),
            'MemberType': type_shortHand[str(type(libraryMember))],
            'ListOfBooksIssued': None,
            'ReservedBook' : None,
            'GotReminder' : 0,
            'PassWd' : encode_message(passwd)
        }
        cursor.execute(addMember, dataMember)
        db.commit()
    
    def RemoveMember(self, libraryMember: LibraryMember):
        deleteMembers = ("DELETE FROM MEMBERS "
                         "WHERE MemberID = %(MemberID)s")
        memberID = {
            'MemberID' : libraryMember.GetMemberID()
        }
        cursor.execute(deleteMembers, memberID)
        db.commit()
    
    def SendRemindertoMember(self):
        pass
    
    def CheckBookIssueStats(self):
        checkStats = ("SELECT UniqueID FROM BOOKS "
                      "WHERE DATEDIFF(%(CurrDate)s, LastIssued) > %(DifferenceInDays)s")
        currDate = {
            'CurrDate' : date.today(),
            'DifferenceInDays' : 1826
        }
        cursor.execute(checkStats, currDate)
        obsoleteBooks = []
        for row in cursor:
            obsoleteBooks.append("{UniqueID}".format(UniqueID=row['UniqueID']))
        print(obsoleteBooks)
    def DisposeBook(self, UID):
        disposeBook = ("UPDATE BOOKS "
                       "SET IsDisposed=1 "
                       "WHERE UniqueID=%(UniqueID)s")
        dataBook = {
            'UniqueID': UID
        }
        cursor.execute(disposeBook, dataBook)
        db.commit()
lib=Librarian(1,"fds")
