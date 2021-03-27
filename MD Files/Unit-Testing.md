
# IEEE TEST PLAN TEMPLATE

## Test Plan Identifier

##### LIS-TESTPLAN-1

## REFERENCES 

##### Software Requirement Specification
##### Use Case Diagram

##### Class Diagram

## INTRODUCTION 

##### This is the Unit-Test plan for Library Information System Version 1.0

##### This plan will aim at providing details for the testing of the different methods used in the functioning of LMS both for a user as well as a software developer
##### The explanation for developers will be more details and for users will include a brief outline

## TEST ITEMS (FUNCTIONS) 

##### 1. The Constructors for all the Classes
###### 1.1 Book

###### 1.2 UnderGraduateStudent

###### 1.3 PostGraduateStudent
###### 1.4 ResearchScholar
###### 1.5 FacultyMember

###### 1.6 BookHandler
###### 1.7 LibraryClerk

###### 1.8 Librarian
###### 1.9 ActiveReservation

##### 2. The Singleton Nature of the Singleton Classes

##### 3. Member Functions of all Classes

##### 4. Functions outside the classes

##### 5. Utility Functions

## FEATURES TO BE TESTED

##### 1. Issue Of a Book

##### 2. Return Of a Book
##### 3. Reservation Of a Book
##### 4. Removing Expired Reservations

##### 5. Update Pending Reservations
##### 6. Penalty Calculation

##### 7. Add a new Member

##### 8. Remove a Member

##### 9. Login

##### 10. Check Issue statistics of Books

##### 11. Add New Book

##### 12. Remove Old/Damaged Books

## FEATURES NOT TO BE TESTED

##### 1. Graphic User Interface will not be tested manually.

## ITEM PASS/FAIL CRITERIA

##### We will provide Golden outputs for the appropriate tests.

##### We will provide appropriate Exception classes for the exceptions

##### Match with Golden Output/Exception class will be a PASS, otherwise would be a FAIL

##### Efficacy would be judged by % of tests passes

## SUSPENSION CRITERIA AND RESUMPTION REQUIREMENTS 

##### Stop tests when some required package compatibility fails

## TEST DELIVERABLES

##### Test Plan Document
##### Test Suite Document

## Unit Testing

### MemberLogin()

###### General Input

  * Member ID

  * Password

  ###### General Output

  * Constructed Object of the User

###### Scenarios

  * Member Logins in successfully
  * Member ID not in database
  * Password does not match with Member ID

### EmployeeLogin()

###### General Input

  * Employee ID

  * Password

  ###### General Output

  * Constructed Object of the User

  ###### Scenarios

  * Employee Logins in successfully
  * Employee ID not in database
  * Password does not match with Employee ID

### Library Member

* ##### Test Getter Functions

  ###### General Input

  LibraryMember

  ###### General Output

  Specific to the Function (Returns value of field we want to get)

  ###### Scenarios

  * Getting the Member ID of the Member
  * Getting the Name of the Member
  * Getting the Number of Books Issued by the Member

* ##### Test CheckAvailabilityOfBook()

  ###### General Input

  * LibraryMember
  * ISBN of the books
  * Database entry in the RESERVATIONS table for the corresponding ISBN. 

  ###### General Output  

  * Book UIDs when available(depending on reservation status of the Library Member).

    OR

  * Status of Reservation if user has a reservation.

  ###### Scenarios

  * The selected ISBN doesn't exist in the RESERVATIONS table.
  * Some copies are available and the user doesn't have any active reservation.
  * Some copies are available and the user has an active reservation.
  * Some copies are available and the user has an expired active reservation.
  * All copies are lent and the user neither has a pending reservation nor an active reservation.
  * All copies are lent and the user is in pending reservation and without other active reservations.
  * All copies are lent and the user is in pending reservation and with other active reservations.
  * All copies are lent and the user is in pending reservation and some active reservation has expired.
  * All copies are lent and the user is in pending reservation and some active reservation has expired and user is now in active reservation.
  * All copies are lent and the user is in active reservation.
  * All copies are lent and the user's active reservation has expired.

* ##### Test IssueBook()

  ###### General Input

  * LibraryMember
  * SBN of book to be issued.
  * Database entry in RESERVATIONS table for the book.
* Database entry in MEMBERS table for the member.
  
###### General Output  

  * Database record in MEMBERS Table updated with the new Book added to the Issued list.
  * Number of Issued books is increased.
* BOOKS and RESERVATIONS Table is updated.
  
  ###### Scenarios
  * User tries to claim a book they have already issued e*
  * User has exhausted their permitted number of issues e*
  * User claims a reserved book.
  * User issues an available book.

* ##### Test ReserveBook()

  ###### General Input

  * LibraryMember
  * ISBN of book to be reserved.
  * Database entry in RESERVATIONS table for the book.
  * Database entry in MEMBERS table for the member.

  ###### General Output  

  * Database record in MEMBERS Table is updated with included the new reservation.

  * RESERVATIONS Table is updated.

  ###### Scenarios

  * The book is available e*

  * The book is unavailable and user has made no reservation for any book. 

  * The book is unavailable and user has pending/active reservations for some other case.

  * The book is unavailable and user has an active reservation for this book.

  * The book is unavailable and user has a pending reservation for this book.

* ##### Test CheckForReminder()

  ###### General Input

  * LibraryMember object

  ###### General Output  

  * Whether the member has been reminded or not

  ###### Scenarios

  * The librarian has called the send reminder function.
  * The librarian has not called the send reminder function.

* ##### Test SearchBook()

  ###### General Input

  * LibraryMember object
* Search String
  
###### General Output  

* Search Results
  
###### Scenarios

  * No book in the system matches with the search string
  * Some subset of books in the system matches with search string
  
* ##### Test UpdateFromDatabase()

  <Updates the data members of LibraryMember from the database. reservedBook is made NULL if reservation expired>

  ###### General Input

  * LibraryMember

  ###### General Output  

  * Database records in MEMBERS updated
  * RESERVATIONS Table is updated with the expired reservation entry deleted

### UnderGraduateStudent

* ##### Test Constructor

  ###### General Input

  Scenario 1:

  * Member ID
  * Name of the Member

  Scenario 2:

  - Member ID
  - Name of the Member
  - Database Entries in the MEMBERS table corresponding to the Member ID
  - Number of Books Issued (calculable)

  ###### General Output

  * Correctly constructed UnderGraduateStudent Object

  ###### Scenarios

  * Librarian wants to add a new Member, Library Clerk wants to process Return
  * Existing Member wants to Login

* ##### Test CanIssue()

  ###### General Input

  * UnderGraduateStudent

  ###### General Output  

  * Returns whether the user can issue another book or not

  ###### Scenarios

  * The user has exhausted his limit of book.
  * The user has not exhausted his limit of book.

### PostGraduateStudent

* ##### Test Constructor

  ###### General Input

  Scenario 1:

  * Member ID
  * Name of the Member

  Scenario 2:

  - Member ID
  - Name of the Member
  - Database Entries in the MEMBERS table corresponding to the Member ID
  - Number of Books Issued (calculable)

  ###### General Output

  * Correctly constructed PostGraduateStudent Object

  ###### Scenarios

  * Librarian wants to add a new Member, Library Clerk wants to process Return
  * Existing Member wants to Login

* ##### Test CanIssue()

  ###### General Input

  * PostGraduateStudent

  ###### General Output  

  * Returns whether the user can issue another book or not

  ###### Scenarios

  * The user has exhausted his limit of book.
  * The user has not exhausted his limit of book.

### ResearchScholar

* ##### Test Constructor

  ###### General Input

  Scenario 1:

  * Member ID
  * Name of the Member

  Scenario 2:

  - Member ID
  - Name of the Member
  - Database Entries in the MEMBERS table corresponding to the Member ID
  - Number of Books Issued (calculable)

  ###### General Output

  * Correctly constructed ResearchScholar Object

  ###### Scenarios

  * Librarian wants to add a new Member, Library Clerk wants to process Return
  * Existing Member wants to Login

* ##### Test CanIssue()

  ###### General Input

  * ResearchScholar

  ###### General Output

  * Returns whether the user can issue another book or not

  ###### Scenarios

  * The user has exhausted his limit of book.
  * The user has not exhausted his limit of book.

### FacultyMember

* ##### Test Constructor

  ###### General Input

  Scenario 1:

  * Member ID
  * Name of the Member

  Scenario 2:

  - Member ID
  - Name of the Member
  - Database Entries in the MEMBERS table corresponding to the Member ID
  - Number of Books Issued (calculable)

  ###### General Output

  * Correctly constructed FacultyMember Object

  ###### Scenarios

  * Librarian wants to add a new Member, Library Clerk wants to process Return
  * Existing Member wants to Login

* ##### Test CanIssue()

  ###### General Input

  * FacultyMember

  ###### General Output  

  * Returns whether the user can issue another book or not

  ###### Scenarios

  * The user has exhausted his limit of book.
  * The user has not exhausted his limit of book.

### Library Clerk

* ##### Test Constructor

  ###### General Input

  * EmployeeID
  * Database entry in EMPLOYEES table with the corresponding EmployeeID

  ###### General Output  

  * Fully Constructed Library Clerk

  ###### Scenarios

  * When the library clerk logs in.

* ##### Test AddBook()

  ###### General Input

  * A Book object

  ###### General Output  

  * BOOKS and RESERVATIONS tables are updated.

  ###### Scenarios

  * The book with same ISBN already exists.
  * The book with same ISBN doesn't already exist. 

* ##### Test DeleteBook()

  ###### General Input

  * A Book object

  ###### General Output  

  * BOOKS and RESERVATIONS tables are updated.

  ###### Scenarios

  * The book exists in the library and has been make as disposed.
  * The book exists in the library and has not been make as disposed.
  * The book doesn't exist in the library.

* ##### Test ReturnBook()

  ###### General Input

  * A Book object
  * The MemberID who is returning the book
  * Database entry in MEMBERS table with corresponding MemberID. 

  ###### General Output  

  * MEMBERS and RESERVATIONS tables are updated.

  ###### Scenarios

  * Member tries to return a book they havent issued e*
  * Member tries to return a book which is not present in the library e*
  * The book has pending reservation which moves to active.
  * The book doesn't have pending reservation.

* ##### Test CollectPenalty()

  ###### General Input

  * A Book object

  ###### General Output  

  * RESERVATIONS tables are updated.

  ###### Scenarios

  * The return date is beyond due date.
  * The return date is within the due date.

### Librarian

* ##### Test Constructor

  ###### General Input

  * EmployeeID
  * Database entry in EMPLOYEES table corresponding to the EmployeeID

  ###### General Output  

  * Fully Constructed Librarian

  ###### Scenarios

  * The EmployeeID is the Librarian.

  * The EmployeeID is not the Librarian but is a Library Clerk.
  * The EmployeeID is not the Librarian but is a Library Member e*

* ##### Test Super Class Functionalities

  ###### General Input

  * Specific to each function

  ###### General Output  

  * Specific to each function

  ###### Scenarios

  * Same scenarios as each Functions of the Super Class 

* ##### Test AddMember()

  ###### General Input

  * Library Member

  ###### General Output  

  * Database entry in the MEMBERS table for the new Library Member

  ###### Scenarios

  * The librarian tries to add a person who is already a member e*
  * The librarian wants to add a new member.

* ##### Test DeleteMember()

  ###### General Input

  * Library Member
  * Database entry for the same Library Member in the MEMBERS table.

  ###### General Output  

  * Database entry of the Library Member is removed from MEMBERS table. 

  ###### Scenarios
  
  * Try to delete a person who is not a member e*
  * There are some members in the library.
  * There are no members in the library.

* ##### Test SendReminder()

  ###### General Input

  * None

  ###### General Output  

  * Librarian's reminder field is set accordingly.

  ###### Scenarios

  * No books are overdue.
  * A few books are overdue.

* ##### Test CheckBookIssueStatistics()

  ###### General Input

  * None

  ###### General Output  

  * List of all copies of books with date when they were last issued.

  ###### Scenarios

  * All books have been issued in the last 5 years.
  * Few books have not been issued in the last 5 years.

* ##### Test DisposeBook()

  ###### General Input

  * A Book Object

  ###### General Output  

  * Database entry in BOOKS table has been marked as disposed.

  ###### Scenarios
  * UID does not exist e*
  * The UID has not been issued in last 5 years e* 
  * The UID has been issued in the last 5 years e*


### Book Handler

* ##### Test Create Function

  ###### General Input

  * None

  ###### General Output  

  * Fully constructed Singleton BookHandler Object (Constructed only the first time, same instance is returned every time)

  ###### Scenarios

  * *<u>No specific scenarios, only called to create a reference to  Singleton BookHandler Object whenever required.</u>*   

* ##### Test OpenBook()

  <Reads a table entry in RESERVATIONS specific to an ISBN into the Data Members of BookHandler>

  ###### General Input

  * A Book Object

    OR

  * ISBN

  ###### General Output  

  * The BookHandler's data members are populated.

  ###### Scenarios

  * Called with the ISBN when UID is irrelevant for the  function calling OpenBook()
  * Called with the Book Object when UID is relevent for the  function calling OpenBook()
  
* ##### Test Singleton Nature of the object

  ###### General Input

  * None

  ###### General Output  

  * None

  ###### Scenarios

  * Call Create() twice and compare address of the objects returned by them
  
* ##### Test UpdateBook()

  <Deletes expired Active Reservation and updates other data members accordingly>

  ###### General Input

  * None

  ###### General Output  

  * Data members are updated
  * Database entry, corresponding to the Members whose active reservation expired, in MEMBERS table is updated

  ###### Scenarios

  * Pending reservations are there, Some active reservations are expired.
  * Pending reservation are there, No active reservations are expired.
  * No pending reservations are there, Some active reservations are expired.
  * No pending reservation are there, No active reservations are expired.

* ##### Test IssueSelected()

  <Issues the current book to a specific user>

  ###### General Input

  * MemberID
  
###### General Output  

* MEMBERS, BOOKS and RESERVATIONS table are updated.
  
###### Scenarios

* Member is claiming a book reserved to them.
* Member is issuing an available book
  
* ##### Test ReturnSelected()

  <Returns the current book>

  ###### General Input

  * MemberID

  ###### General Output  

  * MEMBERS, BOOKS and RESERVATIONS table are updated.

  ###### Scenarios

  * The book has pending reservation which moves to active.
  * The book doesn't have pending reservation.

* ##### Test ReserveSelected()

  <Reserve the current book for a member>

  ###### General Input
  
* MemberID
  
###### General Output  

* MEMBERS, BOOKS and RESERVATIONS table are updated.
  
###### Scenarios

  * The member doesn't have pending/active reservation for this/another book

### Book

* ##### Test Constructor

  ###### General Input

  * Book basic information
  
  OR
  
* Database entry of the book in BOOKS table.
  
###### General Output  

* MEMBERS, BOOKS and RESERVATIONS table are updated.
  
  ###### Scenarios
  
  * Book is created for adding
  * Book is created for using with BookHandler.
### Active Reservation

* ##### Test Constructor

  ###### General Input

  * Member ID
  
  * Date reservation became active.
  
###### General Output  

  * Object Created.

  ###### Scenarios

  * Active reservation is made at any time in the run
