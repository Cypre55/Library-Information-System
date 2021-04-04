import mysql.connector as mysql
import settings
db = mysql.connect(
    host = "localhost",
    user = settings.user,
    passwd = "1234",
    database = "lis"
)
cursor = db.cursor(dictionary = True)

from underGraduateStudent import UnderGraduateStudent
from postGraduateStudent import PostGraduateStudent
from researchScholar import ResearchScholar
from facultyMember import FacultyMember
from bookHandler import SplitTableEntry, JoinTableEntry
from librarian import Librarian, encode_message
from libraryClerk import LibraryClerk

def MemberLogin(memberID: str, password: str):
    if not memberID or not password:
        raise ValueError("Missing Arguments")
    
    findMember = ("SELECT * FROM MEMBERS")
    cursor.execute(findMember)
    found = False
    correctRow = {}
    for row in cursor:
        if row["MemberID"] == memberID:
            correctRow = row
            found = True
    
    if not found:
        raise ValueError("Invalid MemberID inputted.")

    # PassWord Auth
    encodedPassword = encode_message(password)
    if encodedPassword != correctRow["PassWD"]:
        raise ValueError("Incorrect Password inputted.")

    if correctRow["MemberType"] == "UG":
        return UnderGraduateStudent(correctRow['MemberID'], correctRow['MemberName'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "PG":
        return PostGraduateStudent(correctRow['MemberID'], correctRow['MemberName'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "RS":
        return ResearchScholar(correctRow['MemberID'], correctRow['MemberName'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "FM":
        return FacultyMember(correctRow['MemberID'], correctRow['MemberName'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])

    
def EmployeeLogin(employeeID: str, password: str):
    if not employeeID or not password:
        raise ValueError("Missing Arguments")
    
    findEmployee = ("SELECT * FROM EMPLOYEES")
    cursor.execute(findEmployee)
    found = False
    correctRow = {}
    for row in cursor:
        if row["EmployeeID"] == employeeID:
            correctRow = row
            found = True
    
    if not found:
        raise ValueError("Invalid EmployeeID inputted.")

    if employeeID == "LIB001":
        # PassCheck
        # Librarian(, )
        pass

    