import mysql.connector as mysql
import settings
db = mysql.connect(
    host = "localhost",
    user = settings.user,
    passwd = "1234",
    database = "lis"
)
cursor = db.cursor(dictionary = True)

from bookHandler import SplitTableEntry

from underGraduateStudent import UnderGraduateStudent
from postGraduateStudent import PostGraduateStudent
from researchScholar import ResearchScholar
from facultyMember import FacultyMember

def GetBookInfoFromUID(uid):
    findBook = ("SELECT * FROM BOOKS")
    cursor.execute(findBook)
    found = False
    correctRow = {}
    for row in cursor:
        if row["UniqueID"] == uid:
            correctRow = row
            found = True
    db.commit()
    if not found:
        raise ValueError("UniqueID not found.")

    return correctRow

def GetLibraryMember(memberID):
    findMember = ("SELECT * FROM MEMBERS")
    cursor.execute(findMember)
    found = False
    correctRow = {}
    for row in cursor:
        if row["MemberID"] == memberID:
            correctRow = row
            found = True
    db.commit()
    if not found:
        raise ValueError("Invalid MemberID inputted.")

    if correctRow["MemberType"] == "UG":
        return UnderGraduateStudent(correctRow['MemberName'], correctRow['MemberID'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "PG":
        return PostGraduateStudent(correctRow['MemberName'], correctRow['MemberID'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "RS":
        return ResearchScholar(correctRow['MemberName'], correctRow['MemberID'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])
    if correctRow["MemberType"] == "FM":
        return FacultyMember(correctRow['MemberName'], correctRow['MemberID'], SplitTableEntry(correctRow['ListOfBooksIssued']), correctRow['ReservedBook'])

def GetTreeSize(tree, item=""):
    children = tree.get_children()
    # for child in children:
    #     children += GetTreeSize(tree, child)
    return len(children)