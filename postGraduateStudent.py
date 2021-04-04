from libraryMember import LibraryMember


class PostGraduateStudent(LibraryMember):
    __maxBooksAllowed = 4
    __maxMonthsAllowed = 1

    def __init__(self, *args):
        LibraryMember.__init__(self, *args)

    def CanIssue(self):
        return (self._numberOfBooksIssued < self.__maxBooksAllowed)