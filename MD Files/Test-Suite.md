# Test Suite

1. ### Library Member

   1. ##### Test Getter Function

      * ###### Getting the Member ID of the Member

        **Input:** A LibraryMember object (name: Harry; memberID: 19CS30014; <Rest of the members>: None)

        ​	**Output**: 19CS30014

      * ###### Getting the Name of the Member

        **Input:** A LibraryMember object (name: Harry; memberID: 19CS30014; <Rest of the members>: None)

        ​	**Output**: Harry

      * ###### Getting the Number of Books Issued by the Member

        **Input:** A LibraryMember object (name: Harry; memberID: 19CS30014; listOfBooksIssued: [7];  numberOfBooksIssued: 1; <Rest of the members>: None)

        ​	**Output**: 1

   2. ##### Test CheckAvailabilityOfBook()

      * ###### The user has an Active Reservation on this ISBN.

        **Input**: 

        * IBSN: 988-0789032742
        
        * A LibraryMember object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations      | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ----------------------- | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | "2021-04-08*19CS30014," | "3,"               | 2              |

        **Output**:
        
      * List of ActiveReservedUIDS: [3]
        
      * ###### The user has a Pending Reservation on this ISBN.

        **Input**: 

        * IBSN: 988-0789032742
        
        * A LibraryMember object (name: Harry; memberID: 19CS30014; reservedBook: "988-0789032742"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | "19CS30014"         | (NULL)             | (NULL)             | 2              |

        **Output**:
        
      * Message to the User: "Your Reservation is still pending. Please wait for a few more days."
        
      * ###### The user has no reservation on this ISBN and some UIDs are available. (May have reservations on other ISBN)

        **Input**: 

        * IBSN: 988-0789032742
        
        * A LibraryMember object (name: Harry; memberID: 19CS30014; reservedBook: "999-6666689999"; <Rest of the members>: None)

        * RESERVATIONS table:
        
          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
        | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | "7, 2,"       | "1,"      | (NULL)              | (NULL)             | (NULL)             | 2              |

        **Output**:
        
        * List of AvailableUIDs: [7, 2]
        
      * ###### The user has no reservation on any ISBN and no UIDs are available.

        **Input**: 

        * IBSN: 988-0789032742

        * A LibraryMember object (name: Harry; memberID: 19CS30014; reservedBook: None; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Message to the User: 'Sorry this book is not available currently, Would you like to reserve this book?'

      * ###### The user has a reservation on a different ISBN and no UIDs are avalaible. 

        **Input**: 

        * IBSN: 988-0789032742

        * A LibraryMember object (name: Harry; memberID: 19CS30014; reservedBook: "999-6666689999"; <Rest of the members>: None)

        * RESERVATIONS table:

          | ISBN             | AvailableUIDs | TakenUIDs | PendingReservations | ActiveReservations | ActiveReservedUIDs | NumberOfCopies |
          | ---------------- | ------------- | --------- | ------------------- | ------------------ | ------------------ | -------------- |
          | "988-0789032742" | (NULL)        | "1,"      | (NULL)              | (NULL)             | (NULL)             | 0              |

        **Output**:

        * Message to the User: "Sorry this book is not available currently, and you already have a reservation on another ISBN"

   4. ##### Test Issue Book

      * ###### The book is unavailable and user has made no reservation for any book. 
      * ###### The book is unavailable and user has pending/active reservations for some other case.

      * ###### The book is unavailable and user has an active reservation for this book.
      * ###### The book is unavailable and user has a pending reservation for this book.

   5. ##### Test Reserve Book

      * ###### The book is unavailable and user has made no reservation for any book. 
      * ###### The book is unavailable and user has pending/active reservations for some other case.

      * ###### The book is unavailable and user has an active reservation for this book.
      * ###### The book is unavailable and user has a pending reservation for this book.

   7. ##### Test Check Reminder

      * ###### The librarian has called the send reminder function.
      * ###### The librarian has not called the send reminder function.

   8. ##### Test Search Book

      * ###### No book in the system matches with the search string
      
        | UID  | ISBN | BookName | RackNo | LastIssued | IsDiposed |
        | ---- | ---- | -------- | ------ | ---------- | --------- |
        |      |      |          |        |            |           |
      
      * ###### Some subset of books in the system matches with search string 

2. ### UnderGraduateStudent

3. ### PostGraduateStudent

4. ### ResearchScholar

5. ### FacultyMemeber

6. ### Library Clerk

   1. ##### Test Constructor

      * ###### When the library clerk logs in.

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

      * ###### The EmployeeID is the Librarian.
      * ###### The EmployeeID is not the Librarian but is a Library Clerk.
      * ###### The EmployeeID is not the Librarian but is a Library Member.

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

8. ### Book Handler

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

9. ### Book

   1. ##### Test Constructor

      * ###### Book is created for adding
      * ###### Book is created for using with book handler