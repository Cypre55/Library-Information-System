from libraryClerk import LibraryClerk
from libraryMember import LibraryMember
from underGraduateStudent import UnderGraduateStudent
from cryptography.fernet import Fernet
from bookHandler import UpdateReminders
from datetime import date, datetime, timedelta
import mysql.connector as mysql
import base64
import settings
db = mysql.connect(
    host = "localhost",
    user = settings.user,
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
# cursor.execute('SELECT * FROM MEMBERS')
# for row in cursor:
#     print(decode_message(bytes((row["PassWd"]),'utf-8')))
class Librarian(LibraryClerk):
    __reminder = False
    
    def __init__(self, employeeID, name):
        if(employeeID!="LIB0001"):
            raise ValueError
        LibraryClerk.__init__(self, employeeID, name)
    
    def AddMember(self, libraryMember: LibraryMember, passwd):
        if(libraryMember.GetMemberID()==""):
            raise ValueError
        
        if(libraryMember.GetName()==""):
            raise ValueError
            
        mem = {
            'MemberID' : libraryMember.GetMemberID()
        }
        cursor.execute("SELECT MemberID FROM MEMBERS WHERE MemberID = %(MemberID)s", mem)
        for row in cursor:
            if(row['MemberID']==libraryMember.GetMemberID()):
                raise ValueError

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
        member = {
        'mem' : libraryMember.GetMemberID()
        }
        cursor.execute(("SELECT * FROM MEMBERS WHERE MemberID = %(mem)s"),member)
        cnt=0
        for row in cursor:
            cnt = cnt + 1
            if(row['ListOfBooksIssued']!=None):
                raise ValueError("This member can not be deleted as they have overdue books or un-returned books.")
        if(cnt==0):
            raise ValueError("No member present with this member ID.")
        
        deleteMembers = ("DELETE FROM MEMBERS "
                         "WHERE MemberID = %(MemberID)s")
        memberID = {
            'MemberID' : libraryMember.GetMemberID()
        }
        cursor.execute(deleteMembers, memberID)
        db.commit()
    
    def SendReminderToMember(self):
        cursor.execute("UPDATE MEMBERS SET GotReminder = 1")
        db.commit()
        cursor.execute(("SELECT * FROM MEMBERS"))
        row = cursor.fetchone()
        print(row)
        UpdateReminders()
    
    def CheckBookIssueStats(self):
        checkStats = ("SELECT * FROM BOOKS")
        cursor.execute(checkStats)
        obsoleteBooks = []
        print("REACHED")
        for row in cursor:
            print(row)
            dateissued = row["LastIssued"]
            if((date.today()-dateissued).days >= 1826):
                obsoleteBooks.append("{UniqueID}".format(UniqueID=row['UniqueID']))
        return obsoleteBooks
    def DisposeBook(self, UID):
        f = False
        f2 = True
        cursor.execute("SELECT * FROM BOOKS")
        for rows in cursor:
            if(str(rows["UniqueID"])==str(UID)):
                f = True
                dateissued = rows["LastIssued"]
                if((date.today()-dateissued).days < 1826):
                    f2 = False
        if f == False or f2 == False:
            raise ValueError("UID not in system")
        
        disposeBook = ("UPDATE BOOKS "
                       "SET IsDisposed = 1 "
                       "WHERE UniqueID=%(UniqueID)s")
        dataBook = {
            'UniqueID': UID
        }
        cursor.execute(disposeBook, dataBook)
        db.commit()
# lib=Librarian(1,"fds")
