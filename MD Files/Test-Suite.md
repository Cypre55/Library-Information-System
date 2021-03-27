# Test Suite
1. ### MemberLogin()

   1. ##### Test MemberLogin()

      * ###### Member Logs in successfully

        **Input**:

        * MemberID: "19CS30014"

        * Password: "Password" (Encrypted Version: "gAAAAABgWZnULUhCsW.....")

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * An LibraryClerk Object (EmployeeID: "LIB0011"; Name: "Larry")

      * ###### MemberID not in MEMBERS table.

        **Input**:

        * MemberID: "19CS30056"

        * Password: "Pass" (Encrypted Version: "gAAAAAasdfasdfaw.....")

        * MEMBERS table:

		| MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
      | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
      | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * Exception Thrown: MemberIDInvalid: "The MemberID is not present in the system."
        * Message to the User: "Invalid MemberID inputted."

      * ###### Password does not match with MemberID

        **Input**:

        * MemberID: "19CS30014"

        * Password: "Pass" (Encrypted Version: "gAAAAfafasgawCsW.....")

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * Exception Thrown: PasswordIncorrect: "The Password is incorrect."
        * Message to the User: "Password is incorrect."

2. ### EmployeeLogin()

   1. ##### Test EmployeeLogin()

      * ###### Employee Logs in successfully

        **Input**:

        * EmployeeID: LIB0011

        * Password: "Password" (Encrypted Version: "gAAAAABgWZnULUhCsW.....")

        * EMPLOYEES table:

          | EmployeeID | EmployeeName | PassWD                  |
          | ---------- | ------------ | ----------------------- |
          | "LIB0011"  | "Larry"      | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * An LibraryClerk Object (EmployeeID: "LIB0011"; Name: "Larry")

      * ###### EmployeeID not in EMPLOYEES table.

        **Input**:

        * EmployeeID: LIB0011

        * Password: "Password" (Encrypted Version: "gAAAAABgWZnULUhCsW.....")

        * EMPLOYEES table:

          | EmployeeID | EmployeeName | PassWD                  |
          | ---------- | ------------ | ----------------------- |
          | "LIB0011"  | "Larry"      | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * Exception Thrown: EmployeeIDInvalid: "The EmployeeID is not present in the system."
        * Message to the User: "Invalid EmployeeID inputted."

      * ###### Password does not match with Employee ID

        **Input**:

        * EmployeeID: 19CS30056

        * Password: "Pass" (Encrypted Version: "gAAAAfafasgawCsW.....")

        * EMPLOYEES table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        **Output**:

        * Exception Thrown: PasswordIncorrect: "The Password is incorrect."
        * Message to the User: "Password is incorrect."

3. ### Library Member

   1. ##### Test Getter Function

      * ###### Getting the Member ID of the Member

        **Input:** A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; <Rest of the members>: None)

        **Output**: 19CS30014

      * ###### Getting the Name of the Member

        **Input:** A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; <Rest of the members>: None)

        **Output**: Harry

      * ###### Getting the Number of Books Issued by the Member

        **Input:** A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; listOfBooksIssued: [7];  numberOfBooksIssued: 1; <Rest of the members>: None)

        **Output**: 1

   2. ##### Test CheckAvailabilityOfBook()

      * ###### The user has an Active Reservation on this ISBN.

        **Input**: 

        * IBSN: 988-0789032742
        
        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | "2021-04-08*19CS30014," | "3,"               | 0              |
        
        **Output**:
        
        * List of ActiveReservedUIDS: [3] (Displayed along with their Rack No.)
        
      * ###### The user has a Pending Reservation on this ISBN.

        **Input**: 

        * IBSN: 988-0789032742
        
        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | "19CS30014"         | (NULL)             | (NULL)             | 0              |
        
          **Output**:
          
        * Message to the User: "Your Reservation is still pending. Please wait for a few more days."
        
      * ###### The user has no reservation on this ISBN and some UIDs are available. (May have reservations on other ISBN)

        **Input**: 

        * IBSN: 988-0789032742
        
        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "999-6666689999"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7, 2,"       | "1,"      | (NULL)              | (NULL)             | (NULL)             | 2              |

        **Output**:
        
        * List of AvailableUIDs: [7, 2] (Displayed along with their Rack No.)
        
      * ###### The user has no reservation on any ISBN and no UIDs are available.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Message to the User: 'Sorry this book is not available currently, Would you like to reserve this book?'

      * ###### The user has a reservation on a different ISBN and no UIDs are avalaible. 

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "999-6666689999"; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Message to the User: "Sorry this book is not available currently, and you already have a reservation on another ISBN"

   3. ##### Test IssueBook()

      * ###### Member tries to claim a book they have already issued

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: [1]; numberOfIssuedBooks: 1)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |

        **Output**:

        * Exception Thrown: ISBNIssueLimitPerMemberExceeded : "Member cannot issue the same ISBN more than once." 

      * ###### Member has exhausted their permitted number of issues

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: [1, 8]; numberOfIssuedBooks: 2)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |

        **Output**:

        * Exception Thrown: MaxBooksAllowedExceeded : "Member cannot issue more than maxBooksAllowed"

      * ###### Member claims a reserved book.

        **Input**: 

        * IBSN: 988-0789032742

        * Date.today() = 01/04/2021

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <rest of the data members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | "2021-04-03*19CS30014" | "7,"               | 0              |

        **Output**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; listOfIssuedBook: [7]; numberOfIssuedBooks: 1)

        * MEMBERS table: As ReservedBook is claimed, it is made NULL. The claimed book has been added to ListOfIssuedBooks

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        * RESERVATIONS table: The ActiveReservation and ActiveReservedUIDs related to the Member has been removed. The claimed boo has been added to TakenUIDs

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 0              |

      * ###### Member issues an available book.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <rest of the data members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |

        **Output**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; listOfIssuedBook: [7]; numberOfIssuedBooks: 1)

        * MEMBERS table: The issued book has been added to ListOfIssuedBooks

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        * RESERVATIONS table: The issued book is removed from AvailableUIDs and put into TakenUIDs

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 0              |

   4. ##### Test ReserveBook()

      * ###### The book is available.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: ReserveNotAllowed: "Member cannot reserve an ISBN with available UID."

      * ###### The book is unavailable and user has made no reservation for any book. 

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * MEMBERS table: ISBN is added in the members ReservedBook field.

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |

        * RESERVATIONS table: ISBN is added to the ISBN's pending reservations field.

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014,"        | (NULL)             | (NULL)             | 0              |

      * ###### The book is unavailable and user has pending/active reservations for some other ISBN.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "999-6666689999"; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: ReservationLimitExceeded: "Member can not reserve more than one book."

      * ###### The book is unavailable and user has an active reservation for this book.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * Date.today() = 01/04/2021

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | "2021-04-03*19CS30014" | "3,"               | 0              |

        **Output**:

        * Exception Thrown: ReservationExists: "The member has already reserved this ISBN. "

      * ###### The book is unavailable and user has a pending reservation for this book.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014"         | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: ReservationExists: "The member has already reserved this ISBN. "

   5. ##### Test CheckForReminder()

      * ###### The librarian has called the SendReminder function and the Member has overdue book/s.

        ###### **Input**: 

        * IBSN: 988-0789032742

        * Date.today(): 01/04/2021

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014;   listOfIssuedBook: [7]; numberOfIssuedBooks: 1; <Rest of the members>: None)

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 1           | gAAAAABgWZnULUhCsW..... |

        * BOOKS table:

          | UID  | ISBN           | BookName                   | RackNo | LastIssued | IsDisposed |
          | ---- | -------------- | -------------------------- | ------ | ---------- | ---------- |
          | 7    | 988-0789032742 | "James Bond-by-Bond James" | 1      | 01/03/2021 | 0          |

        **Output**:

        * Message to the member: "You have an overdue book/s that needs to be returned."

      * ###### The librarian has called the SendReminder function and the Member has no overdue book/s.

        ###### **Input**: 

        * IBSN: 988-0789032742

        * Date.today(): 01/04/2021

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014;   listOfIssuedBook: [7]; numberOfIssuedBooks: 1; <Rest of the members>: None)

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 1           | gAAAAABgWZnULUhCsW..... |

        * BOOKS table:

          | UID  | ISBN           | BookName                   | RackNo | LastIssued | IsDisposed |
          | ---- | -------------- | -------------------------- | ------ | ---------- | ---------- |
          | 7    | 988-0789032742 | "James Bond-by-Bond James" | 1      | 01/04/2021 | (NULL)     |

        **Output**:

        * MEMBERS table: As the Member has no overdue book, GotReminder has been set to 0.

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

      * ###### The librarian has not called the SendReminder function.

        ###### **Input**: 

        * IBSN: 988-0789032742

        * Date.today(): 01/04/2021

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014;   listOfIssuedBook: [7]; numberOfIssuedBooks: 1; <Rest of the members>: None)

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |

        * BOOKS table:

          | UID  | ISBN           | BookName                   | RackNo | LastIssued | IsDisposed |
          | ---- | -------------- | -------------------------- | ------ | ---------- | ---------- |
          | 7    | 988-0789032742 | "James Bond-by-Bond James" | 1      | 01/02/2021 | (NULL)     |

        **Output**:

        * No message is sent to the user.

   6. ##### Test Search Book

      * ###### No book in the system matches with the search string

        **Input/TestCase**: 

        * Search String: "How to"
        * BOOKS table:

        | UID    | ISBN   | BookName | RackNo | LastIssued | IsDisposed |
        | ------ | ------ | -------- | ------ | ---------- | ---------- |
        | (NULL) | (NULL) | (NULL)   | (NULL) | (NULL)     | (NULL)     |

        **Output**:

        * Message to the User: "There are no books present in the Library."

      * ###### Searching by Name of the book

        **Input/TestCase**: 

        * Search String: "Curry"
        * BOOKS table

        | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
        | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
        | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
        | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | 0          |
        | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | 0          |

        **Output**:

        * List of IBSN and Names of Matching Books: [{"999-666689999", "Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling"}, {"999-777789999", "Curry Patter and the curse of Bhindi-by-J.K.Rowling"}] (Matching Books mean the names have Search String as a Sub-String)
        
      * ###### Searching by Author of the Book
      
        **Input/TestCase**: 
      
        * Search String: "J.K. Rowl"
        * BOOKS table
      
        | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
        | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
        | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
        | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | 0          |
        | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | 0          |
      
        **Output**:
      
        * List of IBSN and Names of Matching Books: [{"999-666689999", "Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling"}, {"999-777789999", "Curry Patter and the curse of Bhindi-by-J.K.Rowling"}] (Matching Books mean the names have Search String as a Sub-String)
      
   7. ##### Test UpdateFromDatabase()

      * ###### The member has an expired ActiveReservation

        **Input**: 

        * RESERVATIONS table: 

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014"         | (NULL)             | (NULL)             | 0              |

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014;   listOfIssuedBook: [7]; numberOfIssuedBooks: 1; <Rest of the members>: None) 

        **Output**:

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014"         | (NULL)             | (NULL)             | 0              |

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "7,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014;   listOfIssuedBook: [7]; numberOfIssuedBooks: 1; <Rest of the members>: None) 

      * ###### The member  has a pending reservation that becomes active.

      * ###### When member has no reservation.

4. ### UnderGraduateStudent

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Database Entries in the MEMBERS table corresponding to the Member ID (does not exist)
        - Number of Books Issued (calculable)

        **Output**: Exception thrown: InvalidMember: "This member is not registered

   2. ##### Test CanIssue()

      - ###### The Member has not exhausted his Book issue limit (2 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)
        - **Output:** True

      - ###### The Member has exhausted his Book issue limit (2 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4]; numberOfIssuedBooks: 1)
        - **Output:** False

   3. ##### Test Super Class Functionalities

      * ###### Same scenarios as each Functions of the Super Class 

        **Input**:

        * Call all Test Functions of LibraryMember.

        **Output**:

        * Expected Output of the Test Functions as explained above.

5. ### PostGraduateStudent

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: PostGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: PostGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Database Entries in the MEMBERS table corresponding to the Member ID (does not exist)
        - Number of Books Issued (calculable)

        **Output**: Exception thrown: InvalidMember: "This member is not registered"

   2. ##### Test CanIssue()

      - ###### The Member has not exhausted his Book issue limit (4 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4]; numberOfIssuedBooks: 1)
        - **Output:** True

      - ###### The Member has exhausted his Book issue limit (4 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6]; numberOfIssuedBooks: 1)
        - **Output:** False

   3. ##### Test Super Class Functionalities

      * ###### Same scenarios as each Functions of the Super Class 

        **Input**:

        * Call all Test Functions of LibraryMember.

        **Output**:

        * Expected Output of the Test Functions as explained above.

6. ### ResearchScholar

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: ResearchScholar object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: ResearchScholar object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Database Entries in the MEMBERS table corresponding to the Member ID (does not exist)
        - Number of Books Issued (calculable)

        **Output**: Exception thrown: InvalidMember: "This member is not registered"

   2. ##### Test CanIssue()

      - ###### The Member has not exhausted his Book issue limit (6 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6]; numberOfIssuedBooks: 1)
        - **Output:** True

      - ###### The Member has exhausted his Book issue limit (6 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6,7,8]; numberOfIssuedBooks: 1)
        - **Output:** False

   3. ##### Test Super Class Functionalities

      * ###### Same scenarios as each Functions of the Super Class 

        **Input**:

        * Call all Test Functions of LibraryMember.

        **Output**:

        * Expected Output of the Test Functions as explained above.

7. ### FacultyMember

   1. ##### Test Constructor

   - ###### Librarian wants to add a new Member

     **Input:**  Construct using -

     * Member ID: 19CS30014
     * Name of the Member: Harry

     **Output**: FacultyMember object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

   - ###### Existing Member wants to Login, Library Clerk wants to process Return

     **Input:** Construct using -

     - Member ID: 19CS30014

     - Database Entries in the MEMBERS table corresponding to the Member ID

       | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
       | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
       | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

     - Number of Books Issued (calculable)

     **Output**: FacultyMember object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

   - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

     **Input:** Construct using -

     - Member ID: 21CP10009 (does not exist)
     - Database Entries in the MEMBERS table corresponding to the Member ID (does not exist)
     - Number of Books Issued (calculable)

     **Output**: Exception thrown: InvalidMember: "This member is not registered"

   2. ##### Test CanIssue()

      * ###### The Member has not exhausted his Book issue limit (10 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6,7,8]; numberOfIssuedBooks: 1)
        - **Output:** True

      * ###### The Member has exhausted his Book issue limit (10 Books)

        - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6,7,8,9,10,11,12]; numberOfIssuedBooks: 1)
        - **Output:** False

   3. ##### Test Super Class Functionalities

      * ###### Same scenarios as each Functions of the Super Class 

        **Input**:

        * Call all Test Functions of LibraryMember.

        **Output**:

        * Expected Output of the Test Functions as explained above.

8. ### Library Clerk

   1. ##### Test Constructor

      * ###### Employee wants to Login: The EmployeeID is of a Library Clerk

        * **Input:** Construct using -

          * Member ID: LIB0011

          * Database entry from EMPLOYEES table corresponding to this ID

            | EmployeeID | EmployeeName | Password               |
            | ---------- | ------------ | ---------------------- |
            | LIB0011    | Mohan        | gAAAAABgWZnULUhCsW.... |

        * **Output**: Library Clerk object : (EmployeeID: LIB0011; name: Mohan)

      * ###### Employee wants to Login: The EmployeeID is not of a Library Clerk

        - **Input: **Construct using -

          * Member ID: 19CS10073

        - **Output:**

          Exception thrown: InvalidLibraryClerkID: "The Employee ID is not of a Library Clerk"

   1. ##### Test AddBook()

      * ###### The book with same ISBN already exists and few PendingReservations exist.

        **Input**:

        * ISBN:"988-0789032742"

        * Name: "Motu and Patnu"

        * Author: "Narendra Modi"

        * Rack No.: 7

        * Date.today() = 01/04/2021

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014"         | (NULL)             | (NULL)             | 0              |

        **Output**:

        * RESERVATIONS table

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | "2021-04-08*19CS30014" | "7,"               | 0              |

        * BOOKS table:

          | UID  | ISBN             | BookName                          | RackNo | LastIssued | IsDisposed |
          | ---- | ---------------- | --------------------------------- | ------ | ---------- | ---------- |
          | 7    | "988-0789032742" | "Motu and Patnu-by-Narendra Modi" | 7      | (NULL)     | (NULL)     |

      * ###### The book with same ISBN already exists and No PendingReservations exist.

        **Input**:

        * ISBN:"988-0789032742"

        * Name: "Motu and Patnu"

        * Author: "Narendra Modi"

        * Rack No.: 7

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * RESERVATIONS table

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |

        * BOOKS table:

          | UID  | ISBN             | BookName                          | RackNo | LastIssued | IsDisposed |
          | ---- | ---------------- | --------------------------------- | ------ | ---------- | ---------- |
          | 7    | "988-0789032742" | "Motu and Patnu-by-Narendra Modi" | 7      | (NULL)     | 0          |

      * ###### The book with same ISBN doesn't already exist.

        **Input**:

        * ISBN: "988-0789032742"
        * Name: "Motu and Patnu"
        * Author: "Narendra Modi"
        * Rack No.: 7
        * RESERVATIONS table: Has no record of this ISBN.

        **Output**:

        * RESERVATIONS table: New record for the incoming book with the book made available.

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | (NULL)    | (NULL)              | (NULL)             | (NULL)             | 1              |

        * BOOKS table: New record for the incoming book has been added.

          | UID  | ISBN             | BookName                          | RackNo | LastIssued | IsDisposed |
          | ---- | ---------------- | --------------------------------- | ------ | ---------- | ---------- |
          | 7    | "988-0789032742" | "Motu and Patnu-by-Narendra Modi" | 7      | (NULL)     | 0          |

   2. ##### Test DeleteBook()

      * ###### There are some books marked as Disposed.

        **Input**: 

        * BOOKS table: 

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
          | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | 1          |
          | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | 1          |
        
        **Output**:
        
        * BOOKS table: Books marked as deleted have been deleted.
        
          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
        
        * ###### There are no books marked as Disposed.
      
          **Input**: 
      
          * BOOKS table: 
      
            | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
            | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
            | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
            | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | 0          |
            | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | 0          |
      
          **Output**:
      
          * BOOKS table: No books deleted as none were marked as Disposed
      
            | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
            | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
            | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | 0          |
            | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | 0          |
            | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | 0     \|   |

   3. ##### Test ReturnBook()

      * ###### Member tried to return a book they haven't isssued.

        **Input**: 

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; <rest of the member>:None)
        * A Book object (UID: 1; ISBN: "999-666689999")

        **Output**:

        * Exception Thrown: ReturnInvalidUID: "Cannot return a book that hasn't been issued."

      * ###### Member tried to return a book which is not present in the library

        **Input**: 

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; <rest of the member>:None)
        * A Book object (UID: -1; ISBN: "999-666689999"; IssueDate: 28/03/2021)

        **Output**:

        * Exception Thrown: InvalidUID: "UID not present in the library."

      * ###### The book has pending reservation which moves to active.

        **Input**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; listOfIssuedBooks: [7]; noOfIssuedBooks: 1; <rest of the member>:None)
        * A Book object (UID: 7; ISBN: "988-0789032742"; IssueDate: 28/03/2021)

        * Date.today() = 01/04/2021

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,7,"  | "19CS30056"         | (NULL)             | (NULL)             | 0              |

        **Output**:

        * RESERVATIONS table

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | "2021-04-08*19CS30056" | "7,"               | 0              |

      * ###### The book doesn't have pending reservation.

        **Input**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; listOfIssuedBooks: [7]; noOfIssuedBooks: 1; <rest of the member>:None)
        * A Book object (UID: 7; ISBN: "988-0789032742"; IssueDate: 28/03/2021)

        * Date.today() = 01/04/2021

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * RESERVATIONS table

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |

   4. ##### Test CollectPenalty()

      * ###### The return date is within the due date.

        **Input**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; listOfIssuedBooks: [7]; noOfIssuedBooks: 1; <rest of the member>:None)
        * A Book object (UID: 7; ISBN: "988-0789032742"; IssueDate: 28/03/2021)

        * Date.today() = 01/04/2021

        **Output**:

        * No Penalty Collected.

      * ###### The return date is beyond due date.

        **Input**:

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; listOfIssuedBooks: [7]; noOfIssuedBooks: 1; <rest of the member>:None)
        * A Book object (UID: 7; ISBN: "988-0789032742"; IssueDate: 24/02/2021)

        * Date.today() = 01/04/2021

        **Output**:

        * Penalty Collected: 7 * (PenaltyRate) (As the member is UG, the book is due on 24/03/2021. The Book is overdue by 7 days)

9. ### Librarian

   1. ##### Test Constructor

      * ###### Employee wants to Login: The EmployeeID is of the Librarian, i.e., LIB0001 (fixed ID of Librarian)

        * **Input:** Construct using -

          * Employee ID: LIB0001

          * Database entry from EMPLOYEES table corresponding to this ID

            | EmployeeID | EmployeeName | Password               |
            | ---------- | ------------ | ---------------------- |
            | LIB0001    | John         | gAAAAABgWZN_r9iYim.... |

        * **Output**: Librarian object : (employeeID: LIB0001; name: John)

      * ###### Employee wants to Login: The EmployeeID is not of the Librarian, i.e. not LIB0001

        - **Input: **Construct using -

          * Employee ID: LIB0068

        - **Output:**

          Exception thrown: InvalidLibrarianID: "The Employee ID is not of the Librarian"

   1. ##### Test Super Class Functionalities

      * ###### Same scenarios as each Functions of the Super Class 

        **Input**:

        * Call all Test Functions of Library Clerk.

        **Output**:

        * Expected Output of the Test Functions as explained above.

   3. ##### Test AddMember()

      * ###### The librarian wants to add a new member.

        **Input**:

        * A LibraryMember object (MemberID: "19CS30014", Name: "Harry", Type: "UG", <Rest of the data members>:None)
        * MEMBERS table: No record with MemberID present.
        * Password: "gAAAAABgWZnULUhCsW...." (encrypted form)

        **Output**:

        * MEMBERS table: New Record added.

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

      * ###### The librarian tries to add a person who is already a member 

        **Input**:

        * A LibraryMember object (MemberID: "19CS30014", Name: "Harry", Type: "UG", <Rest of the data members>:None)

        * MEMBERS table: A record with MemberID present.

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

        * Password: "gAAAAABgWZnULUhCsW...." (encrypted form)

        **Output**:

        * Exception thrown: MemberAlreadyExists: "A member with same MemberID already exists."

      * ###### Name is missing

        **Input**: 

        * Password: "adjfaldjflajglajawwerwerq..." (Encrypted Form)

        * A LibraryMember object (MemberID: "19CS30014", Name: "", Type: "UG", <Rest of the data members>:None)

        **Output**:

        * Exception Thrown: InsufficientArguments: "Required Arguments missing."

      * ###### MemberID is missing

        **Input**: 

        * Password: "adjfaldjflajglajawwerwerq..." (Encrypted Form)

        * A LibraryMember object (MemberID: "", Name: "Harry", Type: "UG", <Rest of the data members>:None)

        **Output**:

        * Exception Thrown: InsufficientArguments: "Required Arguments missing."

      * ###### Type is missing

        **Input**: 

        * Password: "adjfaldjflajglajawwerwerq..." (Encrypted Form)

        * A LibraryMember object (MemberID: "", Name: "Harry", Type: None, <Rest of the data members>:None)

        **Output**:
        
        * Exception Thrown: InsufficientArguments: "Required Arguments missing."
        
      * ###### Password is Missing

        **Input**: 

        * Password: "" (Empty)
        * A LibraryMember object (MemberID: "19CS30014", Name: "Harry", Type: None, <Rest of the data members>:None)

   4. ##### Test Delete Members

      * ###### Delete a existing member 

        **Input**:

        * A LibraryMember object (MemberID: "19CS30014", Name: "Harry", Type: "UG", <Rest of the data members>:None)

        * MEMBERS table

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

        **Output**:

        * MEMBERS table: Empty table as the only member is deleted.

      * ###### Delete a person who is not a member

        **Input**:

        * A LibraryMember object (MemberID: "19CS30037", Name: "Harry", Type: "UG", <Rest of the data members>:None)

        * MEMBERS table

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

        **Output**:

        * Exception Thrown: MemberIDInvalid: "No member present with this member ID." 

      * ###### Deletion of a member with overdue books or un-returned books.

        **Input**:

        * A LibraryMember object (MemberID: "19CS30014", Name: "Harry", Type: "UG", <Rest of the data members>:None)

        * Date.today()= 01/04/2021

        * MEMBERS table

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "1,"              | (NULL)       | 0           | gAAAAABgWZnULUhCsW.... |

        * BOOKS table:

          | UID  | ISBN             | BookName                          | RackNo | LastIssued | IsDisposed |
          | ---- | ---------------- | --------------------------------- | ------ | ---------- | ---------- |
          | 7    | "988-0789032742" | "Motu and Patnu-by-Narendra Modi" | 7      | 2019-04-01 | 0          |

        **Output**:

        * Exception Thrown: MemberWithUnreturnedBook: "This member can not be deleted as they have overdue books or un-returned books." 

   5. ##### Test Sending Reminders

      * ###### Send Reminder to all Members

        **Input**:

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           |
          | "19CS30056" | "Ron"      | "PG"       | (NULL)            | (NULL)       | 0           |
          | "19CS10055" | "Hermonie" | "RS"       | "1,"              | (NULL)       | 1           |

        **Output**:

        * MEMBERS table:

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder |
          | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 1           |
          | "19CS30056" | "Ron"      | "PG"       | (NULL)            | (NULL)       | 1           |
          | "19CS10055" | "Hermonie" | "RS"       | "1,"              | (NULL)       | 1           |

   6. ##### Test Viewing Book Statistics

      * ###### All books have been issued in the last 5 years.

        **Input**:

        * BOOKS table:

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
          | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | 2020-04-01 | 0          |
          | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | 2019-04-01 | 0          |

        **Output**:

        * Empty List is returned as all books have been issues in the last 5 years.

      * ###### Few books have not been issued in the last 5 years.

        **Input**:

        * BOOKS table:

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
          | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | 2010-04-01 | 0          |
          | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | 2019-04-01 | 0          |

        **Output**:

        * List: [{"2", Curry Patter and the curse of Bhindi-by-J.K.Rowling", "2010-04-01"}]

   7. ##### Test Dispose Book

      * ###### UID does not exist

        **Input**:

        * UID: 3

        * BOOKS table:

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2010-04-01 | 0          |

        **Output**:

        * Exception Thrown: UIDInvalid: "The UID does not exist in the system."

      * ###### The UID has been issued in last 5 years

      * ###### UID does not exist

        **Input**:

        * UID: 1

        * BOOKS table:

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2019-04-01 | 0          |

        **Output**:

        * Exception Thrown: CannotDispose: "The UID has been issued in the last 5 years, hence cannot be disposed."

      * ###### The UID has not been issued in the last 5 years 

        ###### UID does not exist

        **Input**:

        * UID: 3

        * BOOKS table:

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2010-04-01 | 0          |

        **Output**:

        * BOOKS table: Book has been marked as disposed.

          | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDisposed |
          | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
          | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2010-04-01 | 1          |

10. ### Book Handler

       1. ##### Test Create() Function

          * ###### No specific scenarios, only called to create a reference to  Singleton BookHandler Object whenever required.  
          
            **Input**:
        
            * None
        
              **Output**:

      * Singleton BookHandler Object with empty data members.

      ##### 2. Test OpenBook()

      * ###### Called with the ISBN when UID is irrelevant for the  function calling OpenBook()
      
        **Input**:
      
        * Book object (ISBN: "999-666689999", UID: "1")
        
        * RESERVATIONS table:
        
          | ISBN            | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | --------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "999-666689999" | "7,9,"        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 2              |
        
        

      **Output**:
        
        * Singleton BookHandler Object 
          * currUID: 1
          * currISBN: "999-666689999"
          * availableUIDs: [7, 9]
          * takenUIDs: [1]
          * pendingReservations: None
          * activeReservations: None
          * activeReservedUIDs: None
        * numberOfCopies: 2

      * ###### Called with the Book Object when UID is relevent for the  function calling OpenBook()
      
        **Input**:
      
        * ISBN: "999-666689999"
        
        * RESERVATIONS table:
        
          | ISBN            | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | --------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "999-666689999" | "7,9,"        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 2              |
        
        

      **Output**:
        
        * Singleton BookHandler Object 
          * currUID: None
          * currISBN: "999-666689999"
          * availableUIDs: [7, 9]
          * takenUIDs: [1]
          * pendingReservations: None
          * activeReservations: None
          * activeReservedUIDs: None
        * numberOfCopies: 2

       * ##### Test Singleton Nature of the Object
         
          * ###### Call Create() twice and compare address of the objects returned by them
            
            **Input**:
            
            * Call Create() twice.
            
            **Output**:
            
            * The addresses of the both the objects are equal.
          
       * ##### Test Update Book
         
          * ###### Pending reservations are there, Some active reservations are expired.
            
            **Input**: 
            
            * BookHandler object currently is populated with information of IBSN: 988-0789032742.
            
            * Date.today() = 01/04/2021
            
            * MEMBERS table
            
              | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
              | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
            | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
            * RESERVATIONS table
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
            | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-01*19CS30014," | "3,"               | 2              |
            
            **Output**:
            
            * MEMBERS table: The members active reservation has expired, hence the field value as been removed.
            
              | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
              | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
            | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |
            
            * RESERVATIONS table: An active reservation has expired. The first of pending reservations has upgraded into ActiveReservation.
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
            | "988-0789032742" | "7,9,"        | "1,"      | "19CS30056,"        | "2021-04-08*19CS10074," | "3,"               | 2              |
            
          * ###### Pending reservation are there, No active reservations are expired.
            
            **Input**: 
            
              * BookHandler object currently is populated with information of IBSN: 988-0789032742.
              * Date.today() = 01/04/2021
            * MEMBERS table
            
              | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
              | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
            | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
            * RESERVATIONS table
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
            | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-03*19CS30014," | "3,"               | 2              |
            
            **Output**:
            
            * MEMBERS table: Unchanged as ActiveReservation hasn't expired
            
              | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
              | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
            | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
            * RESERVATIONS table: Unchanged as ActiveReservation hasn't expired
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
            | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-03*19CS30014," | "3,"               | 2              |
            
          * ###### No pending reservations are there, Some active reservations are expired.
            
            **Input**: 
            
            * BookHandler object currently is populated with information of IBSN: 988-0789032742.
            
            * MEMBERS table:
            
                | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
                | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
              | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
            * RESERVATIONS table
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
            | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-01*19CS30014" | "3,"               | 2              |
            
            **Output**:
            
            * MEMBERS table:  The members active reservation has expired, hence the field value as been removed.
            
                | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD                  |
                | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | ----------------------- |
              | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | 0           | gAAAAABgWZnULUhCsW..... |
            
            
            
            * RESERVATIONS table: As the active reservation expired, it has been removed from active reservation. As no pending reservation are present, the UID has been made available.
            
              | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
              | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
            | "988-0789032742" | "7,9,3,"      | "1,"      | (NULL)              | (NULL)             | (NULL)             | 3              |
            
          * ###### No pending reservation are there, No active reservations are expired.
            
            * **Input**: 
            
                * BookHandler object currently is populated with information of IBSN: 988-0789032742.
                * Date.today() = 01/04/2021
              * MEMBERS table
            
                | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
                | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
              | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
              * RESERVATIONS table
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
              | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-03*19CS30014," | "3,"               | 2              |
            
              **Output**:
            
              * MEMBERS table: Unchanged as ActiveReservation hasn't expired
            
                | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                  |
                | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ----------------------- |
              | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW..... |
            
              * RESERVATIONS table: Unchanged as ActiveReservation hasn't expired
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
                | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-03*19CS30014," | "3,"               | 2              |
            
          
       * ##### Test Issue Selected Book
         
          * ###### The book being issued is a ready-to-be-claimed UID.
            
            **Input**: 
            
            * MemberID: 19CS30014
            
            * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; TakenUIDs: [1, 3]; ActiveReservations: [{19CS30014, 2021-04-01}]; ActiveReservationUID= [7]; <rest of the data members>: None )
            
            * Date.today() = 01/04/2021
            
            * RESERVATIONS table:
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
              | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | "2021-04-01*19CS30014" | "7,"               | 1              |
            
            **Output**:
            
            * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; AvailableUIDs: None; TakenUIDs: [1, 3, 7]; NumberOfBooksAvailable: 0; <rest of the data members>: None )
            
            * BOOKS table:
            
                | UID  | ISBN           | BookName                                                     | RackNo | LastIssued | IsDisposed |
                | ---- | -------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
              | 7    | 988-0789032742 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
            
            * RESERVATIONS table: The issued book is removed from AvailableUIDs and put into TakenUIDs
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
              | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 0              |
            
          * ###### The book being issued is an available UID.
            
            **Input**: 
            
            * MemberID: 19CS30014
            
            * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; AvailableUIDs: [7]; TakenUIDs: [1, 3]; NumberOfBooksAvailable: 1<rest of the data members>: None )
            
            * Date.today() = 01/04/2021
            
            * RESERVATIONS table:
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
              | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |
            
            **Output**:
            
            * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; AvailableUIDs: None; TakenUIDs: [1, 3, 7]; NumberOfBooksAvailable: 0<rest of the data members>: None )
            
            * BOOKS table:
            
                | UID  | ISBN           | BookName                                                     | RackNo | LastIssued | IsDisposed |
                | ---- | -------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
              | 7    | 988-0789032742 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
            
            * RESERVATIONS table: The issued book is removed from AvailableUIDs and put into TakenUIDs
            
                | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 0              |
              
             * ##### Test Return Selected Book
            
                * ###### There is a pending reservation upon return.
            
                  **Input**: 
            
                  * MemberID: 19CS30014
            
                  * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; TakenUIDs: [1, 3, 7]; PendingReservation: [19CS30056]<rest of the data members>: None )
            
                  * Date.today() = 01/04/2021
            
                  * RESERVATIONS table:
            
                      | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                      | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                    | "988-0789032742" | (NULL)        | "1,3,7,"  | "19CS30056,"        | (NULL)             | (NULL)             | 1              |
            
                  **Output**:
            
                  * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; AvailableUIDs: None; TakenUIDs: [1, 3]; ActiveReservations: [ActiveReservation(19CS30013, 08-04-2021)]; ActiveReservationUIDs: "7,"; <rest of the data members>: None )
            
                  * BOOKS table:
            
                      | UID  | ISBN           | BookName                                                     | RackNo | LastIssued | IsDisposed |
                      | ---- | -------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
                    | 7    | 988-0789032742 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
            
                  * RESERVATIONS table: The issued book is removed from AvailableUIDs and put into TakenUIDs
            
                      | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
                      | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
                    | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | "2021-04-08*19CS30056" | "7,"               | 0              |
            
                * ###### There is no pending reservation upon return.
            
                  **Input**: 
            
                  * MemberID: 19CS30014
            
                  * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; TakenUIDs: [1, 3, 7]; PendingReservation: None<rest of the data members>: None )
            
                  * Date.today() = 01/04/2021
            
                  * RESERVATIONS table:
            
                      | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                      | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                    | "988-0789032742" | (NULL)        | "1,3,7,"  | (NULL)              | (NULL)             | (NULL)             | 1              |
            
                  **Output**:
            
                  * BookHandler Object (currISBN: "988-0789032742"; currUID: 7; AvailableUIDs: [7]; TakenUIDs: [1, 3]; NumberOfAvailableBooks: 1; <rest of the data members>: None )
            
                  * BOOKS table:
            
                      | UID  | ISBN           | BookName                                                     | RackNo | LastIssued | IsDisposed |
                      | ---- | -------------- | ------------------------------------------------------------ | ------ | ---------- | ---------- |
                    | 7    | 988-0789032742 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | 2021-04-01 | 0          |
            
                  * RESERVATIONS table: The issued book is removed from AvailableUIDs and put into TakenUIDs
            
                      | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                      | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                      | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 1              |
                    
                   * ##### Test Reserve Selected Book
            
                      * ###### No books are available and the reservation needs to be made.
            
                        **Input**:
            
                        * MemberID: 19CS30014
            
                        * BookHandler Object (currISBN: "988-0789032742"; currUID: -1; AvailableUIDs: None; TakenUIDs: [1, 3]; NumberOfAvailableBooks: 0; PendingReservations: None; <rest of the data members>: None )
            
                        * RESERVATIONS table:
            
                            | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                            | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                          | "988-0789032742" | (NULL)        | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |
            
                        **Output**:
            
                        * BookHandler Object (currISBN: "988-0789032742"; currUID: -1; AvailableUIDs: None; TakenUIDs: [1, 3]; NumberOfAvailableBooks: 0; PendingReservations: "19CS30014"; <rest of the data members>: None )
            
                        * RESERVATIONS table:
            
                            | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
                            | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
                            | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014,"        | (NULL)             | (NULL)             | 0              |

11. ### Book

    1. ##### Test Constructor

       * ###### Book is created for adding

       **Input**: 

       * UID: 1

       * BOOKS table:

         | UID  | ISBN            | BookName                   | RackNo | LastIssued | IsDisposed |
         | ---- | --------------- | -------------------------- | ------ | ---------- | ---------- |
         | 1    | "999-666689999" | "James Bond-by-Bond James" | 1      | 01/04/2021 | 0          |

        **Output**:

       * A constructed Book Object (UID: 1; ISBN: "999-666689999"; DateOfIssue: "2021-04-01")



12. ### ActiveReservation

    1. ##### Test Constructor

    - ###### ActiveReservation object is made at any time in the run

      - **Input:** Construct using -

        Member ID: 19CS30014

        Claim by Date: 2021-04-01

      - **Output:**

        ActiveReservation object : (memberID: 19CS30014, claimByDate: 2021-04-01)
