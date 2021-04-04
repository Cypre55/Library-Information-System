from datetime import date, datetime, timedelta
from cryptography.fernet import Fernet
import mysql.connector as mysql
print()
# db = mysql.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "1234",
#     database = "lis"
# )
# cursor = db.cursor(dictionary = True)

# add_book = ("INSERT INTO BOOKS "
#             "VALUES (%(UniqueID)s, %(ISBN)s, %(BookName)s, %(RackNumber)s, %(IssueDate)s, %(IsDisposed)s)")

# data_book = {
#   'UniqueID': None,
#   'ISBN': '988-0789032742',
#   'BookName': 'Harry Potter and the Director\'s Curse by J.K.Rowling',
#   'RackNumber': 3,
#   'IssueDate' : date(2020, 1, 3),
#   'IsDisposed' : 0
# }
# search_key = 'c'
# search_key = '\'%' + search_key + '%\''
# search_books = "SELECT * FROM BOOKS WHERE BookName LIKE "
# cursor.execute(search_books + search_key)
# for row in cursor:
#     print("* {ISBN}".format(ISBN=row['ISBN']))
# search_key = 'ha'
# search_key = '\'%' + search_key + '%\''
# cursor.execute(search_books + search_key)
# for row in cursor:
#     print("* {BookName}".format(BookName=row['BookName']))
# # 
# # cursor.execute('SELECT * FROM BOOKS') 
# # for row in cursor:
# #     print ("%s", %(row["BookName"]))
# cursor.execute(add_book, data_book)
# db.commit()
# #print(cursor.rowcount, "record inserted")
