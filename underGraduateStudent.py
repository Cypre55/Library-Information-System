from libraryMember import LibraryMember

class UnderGraduateStudent(LibraryMember):
    __maxBooksAllowed = 2
    __maxMonthsAllowed = 1

    def __init__(self, *args):
        LibraryMember.__init__(self, *args)

    def CanIssue(self):
        return (self._numberOfBooksIssued < self.__maxBooksAllowed)
# mem = UnderGraduateStudent(1, 'ret', None, None, 0)
# mem.SearchBook()
mem = UnderGraduateStudent('19CS30056', 'Neha', None, '988-0789032742', 0)
mem.UpdateReservationStatus()
print(mem.CheckAvailabilityOfBook('988-0789032742'))