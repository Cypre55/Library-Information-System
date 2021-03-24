from libraryMember import LibraryMember


class FacultyMember(LibraryMember):
    __maxBooksAllowed = 10
    __maxMonthsAllowed = 6

    def __init__(self):
        LibraryMember.__init__()
        pass

    def CanIssue(self):
        return (self._numberOfBooksIssued < self.__maxBooksAllowed)