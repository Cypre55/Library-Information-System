# Library-Information-System

## Software Pre-requisites
- Python 3 or above
- MySQL with Connector/Python
- Tkinter

## Creating the Database
- Set Up MySQL on your local machine, with all the necessary permissions. [Helpful Link](https://stackoverflow.com/questions/21714869/error-1044-42000-access-denied-for-root-with-all-privileges)
- Enter host, user, passwd in src/settings.py
- Log into the MySQL CLI and run:

```mysql
CREATE DATABASE lis;
exit;
```

* Now to load the schema in the terminal:

```bash
mysql -u <user> -p lis < LIS.sql # Present at the root of this repository

# You will be prompted for the password
```

* You can now populate the database and begin using the software.

## Running the Tests
- Run `python testing.py` on the terminal  in the `src` directory to run the Unit Tests given in the Test Plan
- All the tables except `EMPLOYEES` are emptied completely before starting the tests
- Before running each test, the tables (except `EMPLOYEES`) are emptied and new entries are added as needed for testing
- After the tests are all ran, the tables (except `EMPLOYEES`) are again empty 
- A Test Compliance Report called `testReport.txt` gets generated on running the tests
## Running the Application
- Run `python mainWindow.py` in the `src` directory to run the application
## Things to Know
- The `EMPLOYEES` table always contains one librarian and one library clerk when application is running
- The `EmployeeID` of the Librarian is `LIB0001` always
- The `EmployeeID` of the Library Clerk is `LIB0068`
- New employees can be added through MySQL commands if needed
- Please remember your Library Member password as there is no Change Password feature
## Basic Use Cases
### Librarian
- Add/Remove Members
- Dispose Books
- Check Issue Statistics of all Books
- Send Reminders
### Library Clerk
- Add Books
- Delete those Books that are disposed by librarian
- Process Return of Book by a Library Member
### Library Member
- Issue Book
- Reserve Unavailable Book
- Search Book in Library