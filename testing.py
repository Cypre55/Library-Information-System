import copy
from abc import ABC, abstractmethod
from book import Book
from activeReservation import ActiveReservation
from bookHandler import BookHandler, SplitTableEntry, JoinTableEntry, UpdateReminders
from underGraduateStudent import UnderGraduateStudent
from postGraduateStudent import PostGraduateStudent
from researchScholar import ResearchScholar
from facultyMember import FacultyMember
from libraryMember import LibraryMember
from libraryClerk import LibraryClerk
from datetime import date, datetime, timedelta
from librarian import Librarian
import mysql.connector as mysql
import settings
db = mysql.connect(
    host = "localhost",
    user = settings.user,
    passwd = "1234",
    database = "lis"
)
#db.autocommit = True
cursor = db.cursor(dictionary = True)
def delete():
    cursor.execute("TRUNCATE TABLE BOOKS")
    cursor.execute("TRUNCATE TABLE RESERVATIONS")
    cursor.execute("TRUNCATE TABLE MEMBERS")
    db.commit()

#1. MemberLogin()

#Member logs in successfully
#Member not in members table
#Password does not match

#2. EmployeeLogin()

#Employee logs in successfully
#Employee not in members table
#Password does not match

#3. Library Member
#Getter Function
# student = UnderGraduateStudent("Harry","19CS30014",[],"")
# if(student.GetName()=="Harry"):
#     print("Getter Function Name Test for Library Members: PASS")
# else:
#     print("Getter Function Name Test for Library Members: PASS")
# if(student.GetMemberID()=="19CS30014"):
#     print("Getter Function MemberID Test for Library Members: PASS")
# else:
#     print("Getter Function MemberID Test for Library Members: PASS")
# student = UnderGraduateStudent("Harry","19CS30014",['7'],"")
# if(student.GetNumberOfBookIssued()==1):
#     print("Getter Function Number of Books Test for Library Members: PASS")
# else:
#     print("Getter Function Number of Books Test for Library Members: PASS")
# delete()
#CheckAvailabilityOfBook()
# ###
# student = UnderGraduateStudent("Harry","19CS30014",[],"988-0789032742")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742', NULL, '1,',NULL,'2021-04-08*19CS30014,','3,',0)"))
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','Harry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789102742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','Harry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# result = student.CheckAvailabilityOfBook("988-0789032742")
# if(result == (['3'],['5'])):
#     print("Check availability when member has active reservation in ISBN : PASS")
# else:
#     print("Check availability when member has active reservation in ISBN : FAIL")
# delete()

# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742', NULL,'1,','19CS30014,',NULL,NULL,0)"))
# db.commit()
# print(student.CheckAvailabilityOfBook("988-0789032742"))
# result = student.CheckAvailabilityOfBook("988-0789032742")
# # cursor.execute("INSERT INTO BOOKS VALUES (3,'988-0789032742','Harry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE 2021-1-1,0)")
# # db.commit()
# if(result=='Your Reservation is still pending. Pls wait for a few more days'):
#     print("Check availability when member has pending reservation in ISBN : PASS")
# else:
#     print("Check availability when member has pending reservation in ISBN : FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "999-6666689999")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742', '7,2,','1,',NULL,NULL,NULL,2)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','Harry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0781032742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0781032742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0781032742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0781032742','Parry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','Harry Potter and the Chamber Of Secrets-by-J.K.Rowling',5,DATE '2021-1-1',0)"))
# db.commit()
# result=student.CheckAvailabilityOfBook("988-0789032742")
# if(result==(['7','2'],['5','5'])):
#     print("Check availability when member has no reservation in ISBN but copies are available: PASS")
# else:
#     print("Check availability when member has no reservation in ISBN but copies are available: FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014", [] , None)
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,NULL,NULL,0)"))
# db.commit()
# result=student.CheckAvailabilityOfBook("988-0789032742")
# if(result=='Sorry this book is not available currently, Would you like to reserve this book?'):
#     print("Check availability when member has no reservation in ISBN and no copies are available: PASS")
# else:
#     print("Check availability when member has no reservation in ISBN and no copies are available: FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "999-6666689999")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,NULL,NULL,0)"))
# db.commit()
# result=student.CheckAvailabilityOfBook("988-0789032742")
# print(result)
# if(result=='Sorry this book is not available currently, and you already have a reservation'):
#     print("Check availability when member has a reservation in different ISBN and no copies are available: PASS")
# else:
#     print("Check availability when member has a reservation in different ISBN and no copies are available: FAIL")
# delete()
# ###

# #Test IssueBook()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  ['1'] , "")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742','7,','1,3,',NULL,NULL,NULL,1)"))
# db.commit()
# result = student.IssueBook(Book('1','988-0789032742'))
# if(result==None):
#     print("Error when member tries to issue book they have already issued: PASS")
# else:
#     print("Error when member tries to issue book they have already issued: FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  ['1','8'] , None)
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742','7,','1,3,',NULL,NULL,NULL,1)"))
# db.commit()
# result = student.IssueBook(Book('7','988-0789032742'))
# if(result==None):
#     print("Error when member tries to issue book after exceeding limit: PASS")
# else:
#     print("Error when member tries to issue book after exceeding limit: FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,'2021-04-08*19CS30014,','7,',0)"))
# db.commit()
# result = student.IssueBook(Book('7','988-0789032742'))
# print(result)
# if(result==1):
#     print("Member Claims a reserved book: PASS")
# else:
#     print("Member Claims a reserved book: FAIL")
# delete()
# ###
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742','7,','1,3,',NULL,NULL,NULL,1)"))
# db.commit()
# result = student.IssueBook(Book('7','988-0789032742'))
# if(result==1):
#     print("Member Claims an available book: PASS")
# else:
#     print("Member Claims an available book: FAIL")
# delete()
###

#Test ReserveBook()

# student = UnderGraduateStudent("Harry", "19CS30014",  [] , None)
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742','7,','1,3,',NULL,NULL,NULL,1)"))
# db.commit()
# print('r')
# f = False
# try:
#     print(student.ReserveBook("988-0789032742"))
#     student.ReserveBook("988-0789032742")
# except ValueError:
#     f = True
#     print("Error when Member tries to reserve an available book: PASS")
# if f == False:
#     print("Error when Member tries to reserve an available book: FAIL")

# delete()
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , None)
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,NULL,NULL,0)"))
# db.commit()
# student.ReserveBook("988-0789032742")
# print(student.GetReservedBook())
# if(student.GetReservedBook() == "988-0789032742"):
#     print("Member reserves an unavilable book: PASS")
# else:   
#     print("Member reserves an unavilable book:: FAIL")

# delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,NULL,NULL,0)"))
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "999-6666689999")
# f = False
# try:
#     result = student.ReserveBook("988-0789032742")
# except ValueError:
#     f=True
#     print("Error when Member reserves an unavilable book when they already have a reservation for some other book: PASS")
# if f==False:    
#     print("Error when Member reserves an unavilable book when they already have a reservation for some other book: FAIL")

# delete()
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,'2021-04-03*19CS30014,','3,',0)"))
# f = False
# try:
#     student.ReserveBook("988-0789032742")
# except ValueError:
#     f = True
#     print("Error when Member reserves an unavilable book when they already have an active reservation for this book: PASS")
# if f == False:
#     print("Error when Member reserves an unavilable book when they already have an active reservation for this book: FAIL")

# delete()

# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,','19CS30014',NULL,NULL,0)"))
# try:
#     student.ReserveBook("988-0789032742")
# except ValueError:
#     f = True
#     print("Error when Member reserves an unavilable book when they already have a pending reservation for this book: PASS")
# if f == False:
#     print("Error when Member reserves an unavilable book when they already have a pending reservation for this book: FAIL")
# db.commit()
#delete()

#Test CheckForReminder()

#delete()
# cursor.execute(("INSERT INTO BOOKS VALUES (7,'988-0789032742','James-Bond-by-Bond-James',1, DATE '2021-3-1',0)"))
# db.commit()
# #cursor.execute(("INSERT INTO MEMBERS VALUES ('19CS30014','Harry','UG','7,',NULL,1,'password')"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("19CS30014","Harry",[],None)
# librarian.AddMember(student,'potato')
# student.IssueBook(Book('7','988-0789032742',date(2021,3,1)))
# lastdate = {
#             'date' : date(2021,3,1),
#             'uid' :  7
#         }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# librarian.SendReminderToMember()
# db.commit()
# listrem = student.CheckForReminder()
# if  len(listrem)!=0 :
#     print("Correct message and reminder sent when librarian sends a reminder and member has overdue books: PASS")
# else:  
#     print("Correct message and reminder sent when librarian sends a reminder and member has overdue books: FAIL")
# db.commit()
#delete()
# cursor.execute(("INSERT INTO BOOKS VALUES (7,'988-0789032742','James-Bond-by-Bond-James',1, DATE '2021-4-4',0)"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# librarian = Librarian("LIB0001","Neha")
# librarian.AddMember(student,'potato')
# db.commit()
# student.IssueBook(Book('7','988-0789032742',date.today()))
# db.commit()
# librarian.SendReminderToMember()
# db.commit()
# listrem = student.CheckForReminder()
# db.commit()
# if  len(listrem) ==0 :
#     print("Reminder made to 0 when librarian sends reminder  but member has no overdue books: PASS")
# else:  
#     print("Reminder made to 0 when librarian sends reminder  but member has no overdue books: FAIL")
# db.commit()
#delete()
# cursor.execute(("INSERT INTO BOOKS VALUES (7,'988-0789032742','James-Bond-by-Bond-James',1, DATE '2021-3-1',0)"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# librarian = Librarian("LIB0001","Neha")
# librarian.AddMember(student,'potato')
# db.commit()
# listrem = student.CheckForReminder()
# if  len(listrem)==0:
#     print("Reminder made to 0 when librarian does not send reminder: PASS")
# else:  
#     print("Reminder made to 0 when librarian does not send reminder: FAIL")
# db.commit()


#Test Search Book

# #COMES UNDER GUI TESTING
# print("Search when no book is system matches: PASS")
# print("Search when no book in system matches: FAIL")

# #COMES UNDER GUI TESTING
# print("Search by Name: PASS")
# print("Search by Name: FAIL")

# #COMES UNDER GUI TESTING
# print("Search by Author: PASS")
# print("Search by Author: FAIL")


#Test UpdateFromDatabase()
#delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,'2021-03-29*19CS30014','7,',0)"))
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# librarian.AddMember(student,'potato')
# db.commit()
# student.UpdateFromDatabase()
# db.commit()
# if(student.GetReservedBook()==None):   
#     print("Update database when member has expired active reservation: PASS")
# else:
#     print("Update database when member has expired active reservation: FAIL")
# db.commit()


# delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,','19CS30014','2021-03-29*19CS30037','7,',0)"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , "988-0789032742")
# librarian = Librarian("LIB0001","Neha")
# librarian.AddMember(student,'potato')
# db.commit()
# student2 = UnderGraduateStudent("Harriet", "19CS30037",  [] , "988-0789032742")
# librarian.AddMember(student2,'potato')
# db.commit()
# student.UpdateFromDatabase()
# student2.UpdateFromDatabase()
# if(student2.GetReservedBook()==None):
#     print("Update database when member has pending reservation which becomes active reservation: PASS")
# else:
#     print("Update database when member has pending reservation which becomes active reservation: FAIL")


# delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,NULL,NULL,0)"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  [] , None)
# librarian = Librarian("LIB0001","Neha")
# librarian.AddMember(student,'potato')
# db.commit()
# student.UpdateFromDatabase()
# if(student.GetReservedBook()==None):
#     print("Update database when member has no reservation: PASS")
# else:
#     print("Update database when member has no reservation: FAIL")


#4. UnderGraduateStudent

#Test Constructor
# student = UnderGraduateStudent("Harry", "19CS30014",[],None)
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014"):
#     print("create object when new member is added: PASS")
# else:
#     print("create object when new member is added: FAIL")


# student = UnderGraduateStudent("Harry", "19CS30014",['7'],"988-0789032742")
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014" and student.GetReservedBook()=="988-0789032742"):
#     print("create object when existing member is logged in: PASS")
# else:
#     print("create object when existing member is logged in: FAIL")
# ##
# #print("throw error when invalid member is trying to log in: PASS")
# #print("throw error when invalid member is trying to log in: FAIL")
# ##

# #Test Can issue
# student = UnderGraduateStudent("Harry", "19CS30014",  ['3'] , "988-0789032742")
# val = student.CanIssue()
# if val == True:
#     print("Issue when member has not yet exhausted his limit: PASS")
# else:
#     print("Issue when member has not yet exhausted his limit: FAIL")

# student = UnderGraduateStudent("Harry", "19CS30014",  ['3','4'] , "988-0789032742")
# val = student.CanIssue()
# if val==False:
#     print("Error when member issues after having exhausted his limit: PASS")
# else:
#     print("Error when member issues after having exhausted his limit: FAIL")

# #5. PostGraduateStudent

# #Test Constructor
# student = PostGraduateStudent("Harry", "19CS30014", [] ,None)
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014"):
#     print("create object when new member is added: PASS")
# else:
#     print("create object when new member is added: FAIL")

# student = UnderGraduateStudent("Harry", "19CS30014",['3'],"988-0789032742")
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014" and student.GetReservedBook()=="988-0789032742"):
#     print("create object when existing member is logged in: PASS")
# else:
#     print("create object when existing member is logged in: FAIL")

# #print("throw error when invalid member is trying to log in: PASS")
# #print("throw error when invalid member is trying to log in: FAIL")

# #Test Can issue
# student = PostGraduateStudent("Harry", "19CS30014",  ['3'] , "988-0789032742")
# val = student.CanIssue()
# if  val == True:
#     print("Issue when member has not yet exhausted his limit: PASS")
# else:
#     print("Issue when member has not yet exhausted his limit: FAIL")

# student = PostGraduateStudent("Harry", "19CS30014",  ['3','4','5','6'] , "988-0789032742")
# val = student.CanIssue()
# if  val == False:
#     print("Error when member issues after having exhausted his limit: PASS")
# else:
#     print("Error when member issues after having exhausted his limit: FAIL")


# #6. Research Scholar

# #Test Constructor
# student = ResearchScholar("Harry", "19CS30014",[],None)
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014"):
#     print("create object when new member is added: PASS")
# else:
#     print("create object when new member is added: FAIL")

# student = ResearchScholar("Harry", "19CS30014",  ['7'] ,None)
# if(student.GetName()=="Harry" and student.GetMemberID()=="19CS30014" and student.GetReservedBook()==None):
#     print("create object when existing member is logged in: PASS")
# else:
#     print("create object when existing member is logged in: FAIL")

# #print("throw error when invalid member is trying to log in: PASS")
# #print("throw error when invalid member is trying to log in: FAIL")

# #Test Can issue
# student = ResearchScholar("Harry", "19CS30014",  [] , None)
# val  = student.CanIssue()
# if val == True:
#     print("Issue when member has not yet exhausted his limit: PASS")
# else:
#     print("Issue when member has not yet exhausted his limit: FAIL")
# student = ResearchScholar("Harry", "19CS30014",  ['3','4','5','6','7','8'] , "988-0789032742")
# val  = student.CanIssue()
# if val == False:
#     print("Error when member issues after having exhausted his limit: PASS")
# else:
#     print("Error when member issues after having exhausted his limit: FAIL")

#7. Faculty Member

#Test Constructor
# student = FacultyMember("Harry", "19CS30014",  [] , None)
# if(student.GetName()=="Harry" and student.GetMemberID() == "19CS30014"):
#     print("create object when new member is added: PASS")
# else:
#     print("create object when new member is added: FAIL")

# student = FacultyMember("Harry", "19CS30014",  ['7'] , None)
# if(student.GetName()=="Harry" and student.GetMemberID() == "19CS30014"):
#     print("create object when existing member is logged in: PASS")
# else:
#     print("create object when existing member is logged in: FAIL")

# #print("throw error when invalid member is trying to log in: PASS")
# #print("throw error when invalid member is trying to log in: FAIL")

# #Test Can issue
# student = FacultyMember("Harry", "19CS30014",  ['3'] , "988-0789032742")
# val = student.CanIssue()
# if val == True:
#     print("Issue when member has not yet exhausted his limit: PASS")
# else :
#     print("Issue when member has not yet exhausted his limit: FAIL")

# student = FacultyMember("Harry", "19CS30014",  ['3','4','5','6','7','8','9','10','11','12'] , "988-0789032742")
# val = student.CanIssue()
# if val == False:
#     print("Error when member issues after having exhausted his limit: PASS")
# else:
#     print("Error when member issues after having exhausted his limit: FAIL")

#8. Library Clerk
#Test Constructor

# print("Correct Object Constructed when valid login: PASS")
# print("Correct Object Constructed when valid login: FAIL")

# print("Error thrown when invalid login: PASS")
# print("Error thrown when invalid login: FAIL")

#delete()
# #Add Book
clerk = LibraryClerk("LIB0011","John")
clerk.AddBook(['988-0789032742','Motu and Patnu','Narendra Modi',1,date(2021,4,1)])
clerk.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date(2010,4,1)])
clerk.AddBook(['988-0789032742','Motu and Patnu','Narendra Modi',3,date(2010,4,1)])
clerk.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',1,date(2021,4,1)])
clerk.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date(2010,4,1)])
clerk.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',3,date(2010,4,1)])
db.commit()
student = PostGraduateStudent("Harry","19CS10073",[],None)
student.IssueBook(Book('1','988-0789032742',date.today()))
student.IssueBook(Book('3','988-0789032742',date.today()))
student2 = UnderGraduateStudent("Harry","19CS30014",[],None)
student2.ReserveBook("988-0789032742")
db.commit()
bookDetails = ["988-0789032742","Motu and Patnu","Narendra Modi",7]
clerk.AddBook(bookDetails)
bH=BookHandler.Create()
bH.OpenBook("988-0789032742")
if(('7' in BookHandler.GetActiveReservedUIDs())):
    print("Reservations Correctly updated when same ISBN already present with pending reservations, Book added to database: PASS")
else:
    print("Reservations Correctly updated when same ISBN already present with pending reservations, Book added to database: FAIL")
bookDetails = ['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date.today()]
clerk.AddBook(bookDetails)
bH.CloseBook()
bH.OpenBook('999-666689999')
if('8' in BookHandler.GetAvailableUIDs()):
    print("Reservations Correctly updated when same ISBN already present with no pending reservations, Book added to database: PASS")
else:
    print("Reservations Correctly updated when same ISBN already present with no pending reservations, Book added to database: FAIL")

bookDetails = ['999-666689000','Reopen IIT KGP','Dead Students',2,date.today()]
clerk.AddBook(bookDetails)
db.commit()
cursor.execute("SELECT * FROM BOOKS")
bH.CloseBook()
bH.OpenBook('999-666689000')
if('9' in bH.GetAvailableUIDs()):
    print("Reservations Correctly updated when same ISBN not already present : PASS")
else:
    print("Reservations Correctly updated when  same ISBN not already present : FAIL")
bH.CloseBook()
#delete()

# #Delete Book
# clerk = LibraryClerk("LIB0011","Neha")
# clerk.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date(2021,4,1)])
# clerk.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date(2010,4,1)])
# clerk.AddBook(['999-666689999','Harry Potter and the Directors Curse','Vikram Seth',3,date(2010,4,1)])
# unique = {
#         'uid' :  1
#     }
# cursor.execute("UPDATE BOOKS SET IsDisposed=0 WHERE UniqueID  = %(uid)s", unique)
# db.commit()
# unique = {
#         'uid' :  2
#     }
# cursor.execute("UPDATE BOOKS SET IsDisposed=1 WHERE UniqueID  = %(uid)s", unique)
# db.commit()
# unique = {
#         'uid' :  3
#     }
# cursor.execute("UPDATE BOOKS SET IsDisposed=1 WHERE UniqueID  = %(uid)s", unique)
# db.commit()
# clerk.DeleteBook()
# cursor.execute("SELECT UniqueID FROM BOOKS")
# cnt=0
# for row in cursor:
#     cnt+=1
# if(cnt==1):
#    print("Correctly Deleted ALL Disposed Books from Databases: PASS")
# else:
#    print("Correctly Deleted ALL Disposed Books from Databases: FAIL")
# delete()

# #Return Book

# student = UnderGraduateStudent("Harry", "19CS30014",  [] , None)
# book = Book('1',"999-666689999",date.today())
# clerk = LibraryClerk("LIB0011","John")
# f = False
# try :
#     clerk.ReturnBook(student, book)
# except ValueError:
#     f=True
#     print("Error thrown when member tries to return a book they have not issued: PASS")
# if(f==False):
#     print("Error thrown when member tries to return a book they have not issued: FAIL")

# student = UnderGraduateStudent("Harry", "19CS30014",  [] , None)
# book = Book('-1',"999-666689999",date.today())
# clerk = LibraryClerk("LIB0011","John")
# f = False
# try :
#     clerk.ReturnBook(student, book)
# except ValueError:
#     f=True
#     print("Error thrown when member tries to return a book not in the library: PASS")
# if(f==False):
#     print("Error thrown when member tries to return a book not in the library: FAIL")

# delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742', NULL,'1,3,7,','19CS30056,',NULL,NULL,0)"))
# db.commit()
# cursor.execute(("INSERT INTO MEMBERS VALUES ('19CS30014','Harry','UG','7,',NULL,0,'password')"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# book = Book(7,'988-0789032742',date.today())
# clerk = LibraryClerk("LIB0011","John")
# clerk.ReturnBook(student,book)
# print(student.GetNumberOfBookIssued())
# if(student.GetNumberOfBookIssued()==0):
#     print("Correct Updates when returned book has pending reservations: PASS")
# else:
#     print("Correct Updates when returned book has pending reservations: FAIL")
# delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742', NULL,'1,3,7,',NULL,NULL,NULL,0)"))
# db.commit()
# cursor.execute(("INSERT INTO MEMBERS VALUES ('19CS30014','Harry','UG','7,',NULL,0,'password')"))
# db.commit()
# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# book = Book(7,'988-0789032742',date.today())
# clerk = LibraryClerk("LIB0011","John")
# clerk.ReturnBook(student,book)
# print(student.GetNumberOfBookIssued())
# if(student.GetNumberOfBookIssued()==0):
#     print("Correct Updates when returned book has no pending reservations: PASS")
# else:
#     print("Correct Updates when returned book has no pending reservations: FAIL")


# #Collect Penalty

# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# #passing todays date as issue date as that will never have penalty
# book = Book('7',"988-0789032742",date.today())
# clerk = LibraryClerk("LIB0011","John")
# if(clerk.CollectPenalty(student,book)==0):
#     print("No penalty collected when returned on time: PASS")
# else:
#     print("No penalty collected when returned on time: FAIL")


# student = UnderGraduateStudent("Harry", "19CS30014",  ['7'] , None)
# #passing todays date as issue date as that will never have penalty
# book = Book('7',"988-0789032742",date(2021,2,24))
# clerk = LibraryClerk("LIB0011","John")
# print(clerk.CollectPenalty(student,book))
# if(clerk.CollectPenalty(student,book)):
#     print("Penalty collected when not returned on time: PASS")
# else:
#     print("Penalty collected when not returned on time: FAIL")
# delete()

#Librarian

#Constructor

# f = True
# try:
#     Librarian("LIB0001","John")
# except ValueError:
#     f=False
# if(f):
#     print("Correctly did construction of Librarian object with correct ID: PASS")
# else:
#     print("Correctly did construction of Librarian object with correct ID: FAIL")
# delete()
# f = False
# try:
#     Librarian("LIB0068","Priyanka")
# except ValueError:
#     f=True
# if(f):
#     print("Correctly blocked construction of Librarian object with incorrect ID: PASS")
# else:
#     print("Correctly blocked construction of Librarian object with incorrect ID: FAIL")
# delete()
# Super class functionalities
# Tested above for Library Clerk

# #Add Member
# f=False
# lib=Librarian("LIB0001","John")
# student = PostGraduateStudent("Harry","19CS40014",[],None)
# try:
#     lib.AddMember(student,'password')
# except ValueError:
#     f=True
# if(f==False):
#     print("Correctly Added when Member Does not exist already: PASS")
# else:
#     print("Correctly Added when Member Does not exist already: FAIL")
# delete()

# # try to add the same member again
# f=False
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# try:
#     lib.AddMember(student,'password')
# except ValueError:
#     f=True
# if(f==True):
#     print("Error when Librarian tries to add a member who already exists: PASS")
# else:
#     print("Error when Librarian tries to add a member who already exists: FAIL")
# delete()

# f=False
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("","19CS30014",[],"")
# try:
#     lib.AddMember(student,'password')
# except ValueError:
#     f=True
# if(f==True):
#     print("Error when required argument name missing : PASS")
# else:
#     print("Error when required argument name missing : FAIL")
# delete()

# f=False
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("Harry","",[],"")
# try:
#     lib.AddMember(student,'password')
# except ValueError as err:
#     f=True
# if(f==True):
#     print("Error when required argument member ID missing : PASS")
# else:
#     print("Error when required argument member ID missing : FAIL")

# delete()
# handled during login
# print("Error when type missing : PASS")
# print("Error when type missing : FAIL")
# handled during login
# print("Error when password missing : PASS")
# print("Error when password missing : FAIL")

# delete()
#Delete members
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# lib.AddMember(student,'potatoes')
# db.commit()
# student = UnderGraduateStudent("Harry","19CS30014",[],"")
# lib.RemoveMember(student)
# flag = False
# cursor.execute("SELECT * FROM MEMBERS")

# for row in cursor:
#     if row["MemberID"]=="19CS30014":
#         flag = True
# if(flag==False):
#     print("Deleting Existing member : PASS")
# else:
#     print("Deleting existing member : FAIL")

# delete()
# lib=Librarian("LIB0001","John")
# f = False
# student = UnderGraduateStudent("Harry","19CS30014",[],"")
# try:  
#     lib.RemoveMember(student)
# except ValueError:
#     f=True
#     print("Error when Deleting non-Existing member : PASS")
# if(f==False):
#     print("Error when Deleting non-existing member : FAIL")

# delete()
# f=False
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# lib.AddMember(student,'potatoes')
# cursor.execute(("UPDATE MEMBERS SET ListOfBooksIssued = '1,' WHERE MemberID = '19CS30014'"))
# db.commit()
# try:
#     lib.RemoveMember(student)
# except ValueError:
#     f=True
#     print("Error when Deleting member with dues : PASS")
# if(f==False):
#     print("Error when Deleting member with dues : FAIL")
# delete()

# Sending reminders
# lib=Librarian("LIB0001","John")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# lib.AddMember(student,'potatoes')
# cursor.execute(("UPDATE MEMBERS SET ListOfBooksIssued = '1,' WHERE MemberID = '19CS30014'"))
# db.commit()
# lib.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date(2020,4,1)])
# lastdate = {
#         'date' : date(2020,4,1),
#         'uid' :  1
#     }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# lib.SendReminderToMember()
# cursor.execute(("SELECT * FROM MEMBERS"))
# flag  = False
# for row in cursor:
#     if(row["MemberID"]=='19CS30014'):
#         if(row["GotReminder"]==1):
#             flag=True
# if flag == True:
#     print("Send reminders to all members: PASS")
# else:
#     print("Send reminders to all members: FAIL")
# delete()




#Check issue statistics
# librarian = Librarian("LIB0001","Neha")
# librarian.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date(2021,4,1)])
# lastdate = {
#         'date' : date(2021,4,1),
#         'uid' :  1
#     }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# librarian.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date(2010,4,1)])
# lastdate = {
#         'date' : date(2010,4,1),
#         'uid' :  2
#     }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# librarian.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date(2010,4,1)])
# lastdate = {
#         'date' : date(2010,4,1),
#         'uid' :  3
#     }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# obsolete = (librarian.CheckBookIssueStats())
# print(obsolete)
# if(obsolete[0]=='2' and obsolete[1]=='3'):
#     print("Showing valid Output when some books have not been issued in the last 5 years: PASS")
# else:
#     print("Showing valid Output when some books have not been issued in the last 5 years: FAIL")



#delete()
# librarian = Librarian("LIB0001","Neha")
# librarian.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date.today()])
# db.commit()
# librarian.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date.today()])
# db.commit()
# librarian.AddBook(['999-666689999','Curry Patter and the curse of Bhindi','J.K.Rowling',2,date.today()])
# db.commit()
# obsolete = (librarian.CheckBookIssueStats())
# if(len(obsolete)==0):
#     print("Showing valid Output when all books have been issued in the last 5 years: PASS")
# else:
#     print("Showing valid Output when all books have been issued in the last 5 years: FAIL")


#Test Dispose Book
# librarian = Librarian("LIB0001","Neha")
# f= False
# try:
#     librarian.DisposeBook("10")
# except  ValueError:
#     f=True
#     print("Error when disposing a book whose UID does not exist: PASS")
# if f==False:
#     print("Error when disposing a book whose UID does not exist: FAIL")
# delete()
# librarian = Librarian("LIB0001","Neha")
# librarian.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date.today()])
# db.commit()
# f= False
# try:
#     librarian.DisposeBook("1")
# except  ValueError:
#     f = True
#     print("Error when disposing a book which has been issued in the last 5 years: PASS")
# if f == False:
#     print("Error when disposing a book which has been issued in the last 5 years: FAIL")


#delete()
# librarian = Librarian("LIB0001","Neha")
# librarian.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date(2021,4,1)])
# lastdate = {
#         'date' : date(2010,4,1),
#         'uid' :  1
#     }
# cursor.execute("UPDATE BOOKS SET LastIssued = %(date)s WHERE UniqueID  = %(uid)s", lastdate)
# db.commit()
# librarian.DisposeBook('1')
# cursor.execute("SELECT * FROM BOOKS WHERE UniqueID = 1")
# flag = False
# for rows in cursor:
#     if(rows["IsDisposed"]==1):
#         flag = True
# if flag == True:
#     print("disposing a book which has not been issued in the last 5 years: PASS")
# else:
#     print("disposing a book which has not been issued in the last 5 years: FAIL")


#Book Handler

#Open Book
#delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('999-666689999','7,9,','1,',NULL,NULL,NULL,2)"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# librarian.AddBook(['999-666689999','Curry Patter and the adventures of Aloo Sabzi','J.K.Rowling',1,date(2021,4,1)])
# goldenoutput = ["1","999-666689999",['7','9'],['1'],[],[],[],2]
# 
# bH = BookHandler.Create()
# bH.CloseBook()
# bH.OpenBook("999-666689999")
# print(BookHandler.available)
# if(BookHandler.currISBN == "999-666689999" and BookHandler.available == ['7','9'] and BookHandler.taken == ['1'] and BookHandler.numberOfCopies == 2):
#     print("Correct Data Members when only ISBN provided: PASS")
# else:
#     print("Correct Data Members when only ISBN provided: FAIL")
# 
# bH = BookHandler.Create()
# bH.CloseBook()
# bH.OpenBook(Book("1","999-666689999",date.today()))
# if(BookHandler.currISBN == "999-666689999" and BookHandler.available == ['7','9'] and BookHandler.taken == ['1'] and BookHandler.numberOfCopies == 2 and BookHandler.currUID=='1'):
#     print("Correct Data Members ISBN and UID provided: PASS")
# else:
#     print("Correct Data Members ISBN and UID provided: FAIL")
#delete()
# 
# bh = BookHandler.Create()
# 
# bh2 = BookHandler.Create()
# if(bh == bh2):
#     print("Singleton Class Check: PASS")
# else:
#     print("Singleton Class Check: FAIL")
# bh.CloseBook()
#Update Book
#delete()

# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,','19CS10074,19CS30056,','2021-04-01*19CS30014,','3,',0)"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],'988-0789032742')
# librarian.AddMember(student,'potato')
# cursor.execute(("UPDATE MEMBERS SET ReservedBook = '988-0789032742' WHERE MemberID = '19CS30014'"))
# db.commit()
# flag1 = False
# flag2 = False
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook('988-0789032742')
# db.commit()
# bh.UpdateBook()
# db.commit()
# print("AFTER UPDATE BOOK")
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM MEMBERS")
# for row in cursor:
#     if(row['MemberID']=='19CS30014'):
#         if(row["ReservedBook"]==None):
#             flag1 = True
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     if(row['ISBN']=='988-0789032742'):
#         if(row["ActiveReservedUIDs"]=='3,'):
#             flag2 = True
# if flag1 == True and flag2 == True:
#     print("Update Carried out correctly when pending reservation are there, some active reservations expired: PASS")
# else:
#     print("Update Carried out correctly when pending reservation are there, some active reservations expired: FAIL")


#delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,','19CS10074,19CS30056,',NULL,NULL,0)"))
# db.commit()
# flag2 = False
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook('988-0789032742')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     if(row['ISBN']=='988-0789032742'):
#         if(row["ActiveReservedUIDs"]==None):
#             flag2 = True
# if flag2 == True:
#     print("Update Carried out correctly when pending reservation are there, no reservations expired: PASS")
# else:
#     print("Update Carried out correctly when pending reservation are there, no reservations expired: FAIL")



#delete()

# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,'2021-04-01*19CS30014,','3,',0)"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],'988-0789032742')
# librarian.AddMember(student,'potato')
# cursor.execute(("UPDATE MEMBERS SET ReservedBook = '988-0789032742' WHERE MemberID = '19CS30014'"))
# db.commit()
# flag1 = False
# flag2 = False
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook('988-0789032742')
# db.commit()
# bh.UpdateBook()
# db.commit()
# print("AFTER UPDATE BOOK")
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM MEMBERS")
# for row in cursor:
#     if(row['MemberID']=='19CS30014'):
#         if(row["ReservedBook"]==None):
#             flag1 = True
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     if(row['ISBN']=='988-0789032742'):
#         if(row["ActiveReservedUIDs"]==None):
#             flag2 = True
# if flag1 == True and flag2 == True:
#     print("Update Carried out correctly when no pending reservation are there, some active reservations expired: PASS")
# else:
#     print("Update Carried out correctly when no pending reservation are there, some active reservations expired: FAIL")

#delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,',NULL,NULL,NULL,0)"))
# db.commit()
# flag2 = False
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook('988-0789032742')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     if(row['ISBN']=='988-0789032742'):
#         if(row["ActiveReservedUIDs"]==None):
#             flag2 = True
# if flag2 == True:
#     print("Update Carried out correctly when no pending reservation are there, no active reservations expired: PASS")
# else:
#     print("Update Carried out correctly when no pending reservation are there, no active reservations expired: FAIL")



#Issue Selected Book



#delete()
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook(Book('1',"988-0789032742",date.today()))
# db.commit()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'7,3,',NULL,'2021-04-01*19CS30014,','1,',0)"))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','XYZ',1,DATE '2001-04-01',0)"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],'988-0789032742')
# librarian.AddMember(student,'potato')
# cursor.execute(("UPDATE MEMBERS SET ReservedBook = '988-0789032742' WHERE MemberID = '19CS30014'"))
# db.commit()
# flag2 = False
# bh.IssueSelected('19CS30014')
# db.commit()
# bh.UpdateBook()
# db.commit()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     if(row['ISBN']=='988-0789032742'):
#         if(row["ActiveReservedUIDs"]==None):
#             flag2 = True
# if flag2 == True:
#     print("Book succesfully issued from Ready-To-CLaim reserved Books section : PASS")
# else:
#     print("Book succesfully issued from Ready-To-CLaim reserved Books section : FAIL")



##delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742','1,3,',NULL,NULL,'2021-04-01*19CS30032,','7,',2)"))
# db.commit()
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook(Book('1',"988-0789032742",date.today()))
# db.commit()
# cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','XYZ',1,DATE '2020-04-01',0)"))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],'988-0789032742')
# librarian.AddMember(student,'potato')
# db.commit()
# flag2 = False
# bh.UpdateBook()
# db.commit()
# bh.IssueSelected('19CS30014')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     print(row)
#     if(row['ISBN']=='988-0789032742'):
#         if(row["AvailableUIDs"]=='3,7,' and row["TakenUIDs"]=='1,'):
#             flag2 = True
# if flag2 == True:
#     print("Book succesfully issued from Available Books section : PASS")
# else:
#     print("Book succesfully issued from Available Books section : FAIL")

#Return Book


##delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,','19CS30017,',NULL,NULL,0)"))
# db.commit()
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook(Book('1',"988-0789032742",date.today()))
# db.commit()
# # cursor.execute(("INSERT INTO BOOKS VALUES (NULL,'988-0789032742','XYZ',1,DATE '2020-04-01',0)"))
# # db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",['1'],None)
# librarian.AddMember(student,'potato')
# db.commit()
# flag2 = False
# bh.UpdateBook()
# db.commit()
# bh.ReturnSelected('19CS30014')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     print(row)
#     if(row['ISBN']=='988-0789032742'):
#         if(row["TakenUIDs"]=='3,' and row["AvailableUIDs"]==None):
#             flag2 = True
# if flag2 == True:
#     print("Book succesfully returned when there is a pending reservation for it : PASS")
# else:
#     print("Book succesfully returned when there is a pending reservation for it : FAIL")


##delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,NULL,NULL,0)"))
# db.commit()
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook(Book('1',"988-0789032742",date.today()))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# librarian.AddMember(student,'potato')
# db.commit()
# flag2 = False
# bh.UpdateBook()
# db.commit()
# bh.ReturnSelected('19CS30014')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     print(row)
#     if(row['ISBN']=='988-0789032742'):
#         if(row["TakenUIDs"]=='3,' and row["AvailableUIDs"]=='1,'):
#             flag2 = True
# if flag2 == True:
#     print("Book succesfully returned when there is no pending reservation for it : PASS")
# else:
#     print("Book succesfully returned when there is no pending reservation for it : FAIL")




#Reserve Selected Book


#delete()
# cursor.execute(("INSERT INTO RESERVATIONS VALUES ('988-0789032742',NULL,'1,3,',NULL,NULL,NULL,0)"))
# db.commit()
# bh = BookHandler.Create()
# bh.CloseBook()
# bh.OpenBook(Book('1',"988-0789032742",date.today()))
# db.commit()
# librarian = Librarian("LIB0001","Neha")
# student = UnderGraduateStudent("Harry","19CS30014",[],None)
# librarian.AddMember(student,'potato')
# db.commit()
# flag2 = False
# bh.UpdateBook()
# db.commit()
# bh.ReserveSelected('19CS30014')
# db.commit()
# bh.UpdateBook()
# db.commit()
# bh.UpdateDatabase()
# db.commit()
# cursor.execute("SELECT * FROM RESERVATIONS")
# for row in cursor:
#     print(row)
#     if(row['ISBN']=='988-0789032742'):
#         if(row["TakenUIDs"]=='1,3,' and row["PendingReservations"]=='19CS30014,'):
#             flag2 = True
# if flag2 == True:
#     print("Book succesfully reserved : PASS")
# else:
#     print("Book succesfully reserved : FAIL")
# bH.CloseBook()



#Book 
#constructor
# b = Book('1','988-0789032742', date.today())
# if(b.GetISBN()=='988-0789032742' and b.GetUID()=='1' and b.GetDateOfIssue()==date.today()):
#     print("Book is created properly : PASS")
# else:
#     print("Book is created properly : FAIL")


#Active Reservation
#constructor
# newActive = ActiveReservation("19CS30014",date(2021,4,1))
# if newActive.claimByDate == date(2021,4,1) and newActive.memberID == "19CS30014":
#     print("ActiveReservation is created properly : PASS")
# else:
#     print("ActiveReservation is created properly : FAIL")
