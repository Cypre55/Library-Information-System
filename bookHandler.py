import mysql.connector as mysql
from book import Book
from activeReservation import ActiveReservation
from datetime import date, datetime, timedelta
import mysql.connector as mysql
import settings
db = mysql.connect(
    host = "localhost",
    user = settings.user,
    passwd = "1234",
    database = "lis"
)
cursor = db.cursor(dictionary = True)

# changes
## make all fucntions non static maybe
## no member called currUID
## changes in the arguments of a lot of functions
## might want to pass LIbrary member to IssueBook etc and make changes to its data members then update database using its own method
class BookHandler:
    __instance = None
    __currUID = None
    __currISBN = None
    __available = []
    __taken = []
    __waitList = []
    __readyToClaimUsers = []
    __readyToClaimUIDs = []
    __numberOfCopies = 0
    
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
    def OpenBook(book : Book):
        if (isinstance(book,str)):
            BookHandler.__currISBN = book
        elif(isinstance(book,Book)):
            BookHandler.__currISBN = book.GetISBN()
            BookHandler.__currUID = str(book.GetUID())
        # else handle exception

        selectISBN = ("SELECT * FROM RESERVATIONS WHERE ISBN = %(ISBN)s")
        isbn = {
            'ISBN' : BookHandler.__currISBN
        }
        cursor.execute(selectISBN, isbn)
        for row in cursor:
            print(row)
            BookHandler.__available = SplitTableEntry(row['AvailableUIDs'])
            BookHandler.__taken = SplitTableEntry(row['TakenUIDs'])
            BookHandler.__waitList = SplitTableEntry(row['PendingReservations'])
            
            activeReservationPair = [x.split('*') for x in SplitTableEntry(row['ActiveReservations'])]
            claimByDateYMD = [x[0].split('-') for x in activeReservationPair]
            claimByDateYMD = [date(int(x[0]), int(x[1]), int(x[2])) for x in claimByDateYMD]
            memberID = [x[1] for x in activeReservationPair]
            for i in range(len(memberID)):
                BookHandler.__readyToClaimUsers.append(ActiveReservation(memberID[i], claimByDateYMD[i]))
            
            BookHandler.__readyToClaimUIDs = SplitTableEntry(row['ActiveReservedUIDs'])
            BookHandler.__numberOfCopies = row['NumberOfCopiesAvailable']

    @staticmethod
    def UpdateBook():
        deleteMemberReservation = ("UPDATE MEMBERS SET ReservedBook = NULL WHERE MemberID = %(MemberID)s")
        member = {
            'MemberID' : None
        }
        for entry in BookHandler.__readyToClaimUsers:
            member['MemberID'] = entry.memberID
            if entry.claimByDate < date.today():
                cursor.execute(deleteMemberReservation, member)
                db.commit()
                if len(BookHandler.__waitList): # if pending reservations, then make them active
                    newActive = BookHandler.__waitList.pop(0)
                    BookHandler.__readyToClaimUsers.append(ActiveReservation(newActive, (datetime.now()+timedelta(days = 7)).date()))
                else:
                    reservationFree = BookHandler.__readyToClaimUIDs.pop()
                    BookHandler.__available.append(reservationFree)
        BookHandler.__readyToClaimUsers = [item for item in BookHandler.__readyToClaimUsers if item.claimByDate >= date.today()]
        BookHandler.__numberOfCopies = len(BookHandler.__available)
    
    @staticmethod
    def UpdateDatabase():
        BookHandler.__numberOfCopies = len(BookHandler.__available)
        readyToClaimUsers = list(map(lambda x: str(x.claimByDate)+'*'+x.memberID, BookHandler.__readyToClaimUsers))        
        
        updateReservationTable = ("UPDATE RESERVATIONS SET AvailableUIDs = %(AvailableUIDs)s, TakenUIDs = %(TakenUIDs)s, PendingReservations = %(PendingReservations)s, ActiveReservations = %(ActiveReservations)s, ActiveReservedUIDs = %(ActiveReservedUIDs)s, NumberOfCopiesAvailable = %(NumberOfCopiesAvailable)s WHERE ISBN = %(ISBN)s")
        dataReservation = {
            'ISBN' : BookHandler.__currISBN,
            'AvailableUIDs' : JoinTableEntry(BookHandler.__available),
            'TakenUIDs' : JoinTableEntry(BookHandler.__taken),
            'PendingReservations' : JoinTableEntry(BookHandler.__waitList),
            'ActiveReservations' : JoinTableEntry(readyToClaimUsers),
            'ActiveReservedUIDs' : JoinTableEntry(BookHandler.__readyToClaimUIDs),
            'NumberOfCopiesAvailable' : BookHandler.__numberOfCopies
        }
        print('test12')
        print(BookHandler.__taken)
        # print(dataReservation)
        cursor.execute(updateReservationTable, dataReservation)
        db.commit()
    
    @staticmethod
    def IssueSelected(memberID: str):
        BookHandler.__taken.append(BookHandler.__currUID)
        if(BookHandler.__currUID in BookHandler.__available):
            print('reached1')
            BookHandler.__available.remove(BookHandler.__currUID)
        elif(BookHandler.__currUID in BookHandler.__readyToClaimUIDs):
            
            BookHandler.__readyToClaimUIDs.remove(BookHandler.__currUID)
            BookHandler.__readyToClaimUsers = [x for x in BookHandler.__readyToClaimUsers if x.memberID != memberID]
            cursor.execute(str("UPDATE MEMBERS SET ReservedBook = NULL WHERE MemberId = \""+memberID+"\""))
        lastdate = {
            'date' : date.today(),
            'uid' : BookHandler.__currUID
        }
        cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
        db.commit()
        print(BookHandler.__taken)
        BookHandler.UpdateDatabase()

            # handle the changes to the library member's reservedbook here
        # handle the changes to the library member here
        # handle the cahnges to the particular UID here (last issued)
    @staticmethod
    def ReturnSelected(memberID: str):
        BookHandler.__taken.remove(str(BookHandler.__currUID))
        if len(BookHandler.__waitList) ==0:
            BookHandler.__available.append(BookHandler.__currUID)
        else:
            BookHandler.__readyToClaimUIDs.append(BookHandler.__currUID)
            memberActivated = BookHandler.__waitList.pop(0)
            newActive = ActiveReservation(memberActivated, (datetime.now()+timedelta(days = 7)).date())
            BookHandler.__readyToClaimUsers.append(newActive)
        BookHandler.UpdateDatabase()

    @staticmethod
    def ReserveSelected(memberID : str):
        BookHandler.__waitList.append(memberID)
        BookHandler.UpdateDatabase()
    def CloseBook(self):
        self.UpdateDatabase()
        BookHandler.__currISBN = None
        BookHandler.__available = []
        BookHandler.__taken = []
        BookHandler.__waitList = []
        BookHandler.__readyToClaimUsers = []
        BookHandler.__readyToClaimUIDs = []
        BookHandler.__numberOfCopies = None

    @staticmethod
    def GetActiveReservedUIDs():
        return BookHandler.__readyToClaimUIDs

    @staticmethod
    def GetAvailableUIDs():
        return BookHandler.__available

    @staticmethod
    def IsActive(memberID: str):
        return memberID in [x.memberID for x in BookHandler.__readyToClaimUsers] 
    
    @staticmethod
    def IsAvailable(ISBN: str):
        return ISBN in BookHandler.__available

    @staticmethod
    def AddToPending(memberID: str):
        BookHandler.__waitList.append(memberID)
    
def SplitTableEntry(s: str):
    if(s is None):
        return []
    return s.split(',')[0:-1]

def JoinTableEntry(l):
    if(len(l) == 0):
        return None
    return ','.join(l) + ','

# bk = BookHandler.Create()
# bk.OpenBook('918-0789532743')
# bk.UpdateBook()
# bk.CloseBook()
