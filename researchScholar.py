from libraryMember import LibraryMember


class ResearchScholar(LibraryMember):
    __maxBooksAllowed = 6
    __maxMonthsAllowed = 3

    def __init__(self):
        LibraryMember.__init__()

    def CanIssue(self):
        return (self._numberOfBooksIssued < self.__maxBooksAllowed)