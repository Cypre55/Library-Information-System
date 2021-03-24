import datetime
class Book():
    def __init__(self, UID, ISBN, dateOfIssue, dueDate):
        self.__UID = UID
        self.__ISBN = ISBN
        self.__dateOfIssue = dateOfIssue
        self.__dueDate = dueDate
