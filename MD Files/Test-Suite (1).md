# Test Suite

1. ### Library Member

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
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | "2021-04-08*19CS30014," | "3,"               | 2              |
        
        **Output**:
        
        * List of ActiveReservedUIDS: [3] (Displayed along with their Rack No.)
        
      * ###### The user has a Pending Reservation on this ISBN.

        **Input**: 

        * IBSN: 988-0789032742
        
        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | "19CS30014"         | (NULL)             | (NULL)             | 2              |
        
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
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: : "Member cannot issue the same ISBN more than once."  ----------------------------------------------------

      * ###### Member has exhausted their permitted number of issues

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: [1, 8]; numberOfIssuedBooks: 1)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7,"          | "1,3,"    | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: MaxBooksAllowedExceeded : "Member cannot issue more than maxBooksAllowed"

      * ###### Member claims a reserved book.

      * ###### Member issues an available book.

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

        * Exception Thrown: : "Member cannot reserve an ISBN with available UID."  ----------------------------------------------------

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

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
          | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

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

        * Exception Thrown: : "" ------------------------------------------------------

      * ###### The book is unavailable and user has a pending reservation for this book.

        **Input**: 

        * IBSN: 988-0789032742

        * A UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,3,"    | "19CS30014"         | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Exception Thrown: : "" ---------------------------------------------

   5. ##### Test Check Reminder

      * ###### The librarian has called the send reminder function.
      * ###### The librarian has not called the send reminder function.

   6. ##### Test Search Book

      * ###### No book in the system matches with the search string

        **Input**: 

        * Search String: How to
        * BOOKS table

        | UID    | ISBN   | BookName | RackNo | LastIssued | IsDiposed |
        | ------ | ------ | -------- | ------ | ---------- | --------- |
        | (NULL) | (NULL) | (NULL)   | (NULL) | (NULL)     | (NULL)    |

        **Output**:

        * Message to the User: "There are no books present in the Library."

      * ###### Some subset of books in the system matches with search string 

        **Input**: 

        * Search String: "Curry"
        * BOOKS table

        | UID  | ISBN          | BookName                                                     | RackNo | LastIssued | IsDiposed |
        | ---- | ------------- | ------------------------------------------------------------ | ------ | ---------- | --------- |
        | 1    | 999-666689999 | Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling | 1      | (NULL)     | (NULL)    |
        | 2    | 999-777789999 | Curry Patter and the curse of Bhindi-by-J.K.Rowling          | 2      | (NULL)     | (NULL)    |
        | 3    | 999-888889999 | Harry Potter and the Director's Curse-by-Vikram Seth         | 3      | (NULL)     | (NULL)    |

        **Output**:

        * List of IBSN and Names of Matching Books: [{"999-666689999", "Curry Patter and the adventures of Aloo Sabzi-by-J.K.Rowling"}, {"999-777789999", "Curry Patter and the curse of Bhindi-by-J.K.Rowling"}] (Matching Books mean the names have Search String as a Sub-String)

7. ### UnderGraduateStudent

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Name of the Member: Harry

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Name of the Member: Harry
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

3. ### PostGraduateStudent

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: PostGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Name of the Member: Harry

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: PostGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Name of the Member: Harry
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

4. ### ResearchScholar

   1. ##### Test Constructor

      - ###### Librarian wants to add a new Member

        **Input:**  Construct using -

        * Member ID: 19CS30014
        * Name of the Member: Harry

        **Output**: ResearchScholar object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

      - ###### Existing Member wants to Login, Library Clerk wants to process Return

        **Input:** Construct using -

        - Member ID: 19CS30014

        - Name of the Member: Harry

        - Database Entries in the MEMBERS table corresponding to the Member ID

          | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
          | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
          | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

        - Number of Books Issued (calculable)

        **Output**: ResearchScholar object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

      - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

        **Input:** Construct using -

        - Member ID: 21CP10009 (does not exist)
        - Name of the Member: Harry
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

5. ### FacultyMember

   1. ##### Test Constructor

   - ###### Librarian wants to add a new Member

     **Input:**  Construct using -

     * Member ID: 19CS30014
     * Name of the Member: Harry

     **Output**: FacultyMember object (name: Harry; memberID: 19CS30014; reservedBook: None; listOfIssuedBook: None; numberOfIssuedBooks: 0)

   - ###### Existing Member wants to Login, Library Clerk wants to process Return

     **Input:** Construct using -

     - Member ID: 19CS30014

     - Name of the Member: Harry

     - Database Entries in the MEMBERS table corresponding to the Member ID

       | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD                 |
       | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | ---------------------- |
       | "19CS30014" | "Harry"    | "UG"       | "3,"              | "988-0789032742" | 0           | gAAAAABgWZnULUhCsW.... |

     - Number of Books Issued (calculable)

     **Output**: FacultyMember object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3]; numberOfIssuedBooks: 1)

   - ###### Invalid Member wants to Login, Library Clerk wants to process Return for Invalid Member

     **Input:** Construct using -

     - Member ID: 21CP10009 (does not exist)
     - Name of the Member: Harry
     - Database Entries in the MEMBERS table corresponding to the Member ID (does not exist)
     - Number of Books Issued (calculable)

     **Output**: Exception thrown: InvalidMember: "This member is not registered"

   2. ##### Test CanIssue()

   - ###### The Member has not exhausted his Book issue limit (10 Books)

     - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6,7,8]; numberOfIssuedBooks: 1)
     - **Output:** True

   - ###### The Member has exhausted his Book issue limit (10 Books)

     - **Input:** UnderGraduateStudent object (name: Harry; memberID: 19CS30014; reservedBook:   "988-0789032742"; listOfIssuedBook:   [3,4,5,6,7,8,9,10,11,12]; numberOfIssuedBooks: 1)
     - **Output:** False

6. ### Library Clerk

      1. ##### Test Constructor

         * ###### Employee wants to Login: The EmployeeID is of a Library Clerk

           * **Input:** Construct using -

             * Member ID: LIB0011

             * Database entry from EMPLOYEES table corresponding to this ID

               | EmployeeID | EmployeeName | Password               |
               | ---------- | ------------ | ---------------------- |
               | LIB0011    | Mohan        | gAAAAABgWZnULUhCsW.... |

           * **Output**: Library Clerk object : (employeeID: LIB0011; name: Mohan)

         * ###### Employee wants to Login: The EmployeeID is not of a Library Clerk

           - **Input: **Construct using -

             * Member ID: 19CS10073

           - **Output:**

             Exception thrown: InvalidLibraryClerkID: "The Employee ID is not of a Library Clerk"

      2. ##### Test Add Book

         * ###### The book with same ISBN already exists.
         * ###### The book with same ISBN doesn't already exist. 

      3. ##### Test Delete Book

         * ###### The book exists in the library and has been make as disposed.
         * ###### The book exists in the library and has not been make as disposed.
         * ###### The book doesn't exist in the library.

      4. ##### Test Return Book

         * ###### The book has pending reservation which moves to active.
         * ###### The book doesn't have pending reservation.

      5. ##### Test Collect Penalty

         * ###### The return date is beyond due date.
         * ###### The return date is within the due date.

7. ### Librarian

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

         * ###### The EmployeeID is not the Librarian but is a Library Clerk

      2. ##### Test Super Class Functionalities

         * ###### Same scenarios as each Functions of the Super Class

      3. ##### Test Add Members

         * ###### The librarian wants to add a new member.

      4. ##### Test Delete Members

         * ###### There are some members in the library.
         * ###### There are no members in the library.

      5. ##### Test Sending Reminders

         * ###### No books are overdue.
         * ###### A few books are overdue.

      6. ##### Test Viewing Book Statistics

         * ###### All books have been issued in the last 5 years.
         * ###### Few books have not been issued in the last 5 years.

      7. ##### Test Dispose Book

         * ###### The Book object has currUID field.
         * ###### The Book object does not have currUID field. 

13. ### Book Handler

    1. ##### Test Create Function

       * ###### The BookHandler is needed to be called.

    2. ##### Test Open Book

       * ###### When book is opened by passing a book
       * ###### When book is opened by passing the ISBN

    3. ##### Test Singleton Nature of the Object

       * ###### Try to create two objects.
       * ###### Address of the object returned by Create is the same 

    4. ##### Test Update Book

       * ###### Pending reservations are there, Some active reservations are expired.

         **Input**: 

         * BookHandler object currently is populated with information of IBSN: 988-0789032742.

         * Date.today() = 01/04/2021

         * MEMBERS table

         | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
         | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
         | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

         * RESERVATIONS table

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
         | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-01*19CS30014," | "3,"               | 2              |

         **Output**:

         * MEMBERS table: The members active reservation has expired, hence the field value as been removed.

         | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD          |
         | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | --------------- |
         | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | (NULL)      | aakjfkjsadfkasd |

         * RESERVATIONS table: An active reservation has expired. The first of pending reservations has upgraded into ActiveReservation.

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
         | "988-0789032742" | "7,9,"        | "1,"      | "19CS30056,"        | "2021-04-08*19CS10074," | "3,"               | 2              |

       * ###### Pending reservation are there, No active reservations are expired.

         **Input**: 

         * BookHandler object currently is populated with information of IBSN: 988-0789032742.
         * Date.today() = 01/04/2021
         * MEMBERS table

         | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
         | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
         | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

         * RESERVATIONS table

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
         | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-03*19CS30014," | "3,"               | 2              |

         **Output**:

         * MEMBERS table: Unchanged as ActiveReservation hasn't expired

         | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
         | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
         | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

         * RESERVATIONS table: Unchanged as ActiveReservation hasn't expired

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations    | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ---------------------- | ----------------------- | ------------------ | -------------- |
         | "988-0789032742" | "7,9,"        | "1,"      | "19CS10074,19CS30056," | "2021-04-03*19CS30014," | "3,"               | 2              |

       * ###### No pending reservations are there, Some active reservations are expired.

         **Input**: 

         * BookHandler object currently is populated with information of IBSN: 988-0789032742.

         * MEMBERS table:

           | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
           | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
           | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

         * RESERVATIONS table

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations     | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ------------------- | ---------------------- | ------------------ | -------------- |
         | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-01*19CS30014" | "3,"               | 2              |

         **Output**:

         * MEMBERS table:  The members active reservation has expired, hence the field value as been removed.

           | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook | GotReminder | PassWD          |
           | ----------- | ---------- | ---------- | ----------------- | ------------ | ----------- | --------------- |
           | "19CS30014" | "Harry"    | "UG"       | (NULL)            | (NULL)       | (NULL)      | aakjfkjsadfkasd |

         

         * RESERVATIONS table: As the active reservation expired, it has been removed from active reservation. As no pending reservation are present, the UID has been made available.

         | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
         | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
         | "988-0789032742" | "7,9,3,"      | "1,"      | (NULL)              | (NULL)             | (NULL)             | 3              |

       * ###### No pending reservation are there, No active reservations are expired.

         * **Input**: 

           * BookHandler object currently is populated with information of IBSN: 988-0789032742.
           * Date.today() = 01/04/2021
           * MEMBERS table

           | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
           | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
           | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

           * RESERVATIONS table

           | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
           | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
           | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-03*19CS30014," | "3,"               | 2              |

           **Output**:

           * MEMBERS table: Unchanged as ActiveReservation hasn't expired

           | MemberID    | MemberName | MemberType | ListOfBooksIssued | ReservedBook     | GotReminder | PassWD          |
           | ----------- | ---------- | ---------- | ----------------- | ---------------- | ----------- | --------------- |
           | "19CS30014" | "Harry"    | "UG"       | (NULL)            | "988-0789032742" | (NULL)      | aakjfkjsadfkasd |

           * RESERVATIONS table: Unchanged as ActiveReservation hasn't expired

           | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
           | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
           | "988-0789032742" | "7,9,"        | "1,"      | (NULL)              | "2021-04-03*19CS30014," | "3,"               | 2              |

    5. ##### Test Reserve Selected Book

    * ###### The book has pending reservation which moves to active.
       * ###### The book doesn't have pending reservation.

14. ### Book

    1. ##### Test Constructor

       * ###### Book is created for adding
       
       * ###### Book is created for using with book handler
    
10. ### ActiveReservation

      1. ##### Test Constructor

         - ###### ActiveReservation object is made at any time in the run

           - **Input:** Construct using -

             Member ID: 19CS30014

             Claim by Date: 2021-04-01

           - **Output:**

             ActiveReservation object : (memberID: 19CS30014, claimByDate: 2021-04-01)