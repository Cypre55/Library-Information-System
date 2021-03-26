import datetime
class Book():
    def __init__(self, UID, ISBN, dateOfIssue, dueDate):
        self.__UID = UID
        self.__ISBN = ISBN
        self.__dateOfIssue = dateOfIssue
        self.__dueDate = dueDate

    def GetUID(self):
        return self.__UID
    def GetISBN(self):
        return self.__ISBN