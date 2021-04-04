from tkinter import *
from tkinter import ttk
from colors import *
from availabilityWindow import *
from helperFrames import ScrollableFrame
from bookHandler import SplitTableEntry, JoinTableEntry

class ProfileFrame(Frame):
    def __init__(self, master, member):
        super().__init__(master)
        self.master = master
        self.member = member

        self.config(bg = lightorange, pady=210)

        self.titleLabel = Label(self, text="Your Profile")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.nameFrame = Frame(self)
        self.nameFrame.config(bg=lightorange)
        self.nameLabel = Label(self.nameFrame, text="Name: " + self.member._name) 
        self.nameLabel.config(font=(12), bg=orange, fg=white)
        self.nameLabel.grid(column=0, row=0, padx = 5, pady = 5)
        self.blanknameLabel = Label(self.nameFrame, bg=lightorange)
        self.blanknameLabel.grid(column=1, row=0, padx=440)
        # self.memberNameLabel = Label(self.nameFrame, text="Chappidi Yoga Satwik")
        # self.memberNameLabel.config(font=(12), bg=orange, fg=white)
        # self.memberNameLabel.grid(column=1, row=0, padx = 5, pady = 5)
        self.nameFrame.grid(column=0, row=1)

        self.memberTypeFrame = Frame(self)

        self.IDFrame = Frame(self)
        self.IDFrame.config(bg=lightorange)
        self.IDLabel = Label(self.IDFrame, text="Member ID: " + self.member._memberID)
        self.IDLabel.config(font=(12), bg=orange, fg=white)
        self.IDLabel.grid(column=0, row=0, padx = 5, pady = 5)
        self.blankIDLabel = Label(self.IDFrame, bg=lightorange)
        self.blankIDLabel.grid(column=1, row=0, padx=460)
        # self.memberIDLabel = Label(self.IDFrame, text="19CS30013")
        # self.memberIDLabel.config(font=(12), bg=orange, fg=white)
        # self.memberIDLabel.grid(column=1, row=0, padx = 5, pady = 5)
        self.IDFrame.grid(column=0, row=2)
        
        self.issuedFrame = Frame(self)
        self.issuedFrame.config(bg=lightorange)
        self.issuedLabel = Label(self.issuedFrame, text="Issued Books:")
        self.issuedLabel.config(font=(12), bg=orange, fg=white)
        self.issuedLabel.grid(column=0, row=0, padx = 5, pady = 5)
        self.blankissuedLabel = Label(self.issuedFrame, bg=lightorange)
        self.blankissuedLabel.grid(column=1, row=0, padx=470)
        self.issuedFrame.grid(column=0, row=3)
        # Show List of Issued books
        books = [{"Title": "Curry Patter", "UID": "1", "DueDate": "01/07/2021"},
                 {"Title": "Harry Potter", "UID": "2", "DueDate": "01/08/2021"}
                ]
        cols = ('Title', 'UID', 'Due Date')
        ttk.Style().configure("Treeview", background=orange,
                foreground=white, fieldbackground=lightorange)
        self.listBox = ttk.Treeview(self, columns=cols, show='headings')
        for col in cols:
            self.listBox.heading(col, text=col)   
        for book in books:
            self.listBox.insert("", "end", values=(book["Title"], book["UID"], book["DueDate"]))

        self.listBox.grid(column=0, row=4)

        self.reservedFrame = Frame(self)
        self.reservedFrame.config(bg=lightorange)
        self.reservedLabel = Label(self.reservedFrame, text="Reserved Book: " + str(self.member._reservedBook))
        self.reservedLabel.config(font=(12), bg=orange, fg=white)
        self.reservedLabel.grid(column=0, row=0, padx = 5, pady = 5)
        self.blankreservedLabel = Label(self.reservedFrame, bg=lightorange)
        self.blankreservedLabel.grid(column=1, row=0, padx=400)
        self.reservedFrame.grid(column=0, row=5)




class SearchFrame(Frame):
    def __init__(self, master, member):
        super().__init__(master)
        self.master = master
        self.member = member
        
        self.config(bg = lightorange, pady=230, padx=250)

        self.searchLabel = Label(self, text="Search by Name/Author")
        self.searchLabel.config(font=(12), bg=orange, fg=white)
        self.searchLabel.grid(column=0, row=0, padx=10, pady=10)
        
        self.searchString = StringVar()
        self.searchString.trace("w", lambda name, index, mode, sv=self.searchString: self.SearchBook(sv))

        self.searchEntry = Entry(self, textvariable = self.searchString)
        self.searchEntry.grid(column=0, row=1, ipady=5, ipadx=200)
        self.searchEntry.config(bg=lightorange, fg=white)

        self.resultsFrame = Frame(self)
        self.resultsFrame.config(bg=lightorange)
        self.resultsFrame.grid(column=0, row=2, pady=10, padx=10)

        self.resultsScrollable = ScrollableFrame(self.resultsFrame)
        self.resultsScrollable.config(bg=lightorange)
        self.resultsScrollable.grid(column=0, row=0)

        # self.counter = 0
        self.results = []
        self.resultFrames = []


    def SearchBook(self, searchString):
        # print(searchString.get())
        self.results.append(searchString.get())
        self.UpdateResults()
        pass

    def UpdateResults(self):
        if self.resultFrames:
            del self.resultFrames
            self.resultFrames = []

        for i in range(len(self.results)):
            frame = Frame(self.resultsScrollable.scrollable_frame)
            frame.config(bg=lightorange)
            label = Label(frame, text=self.results[i])
            label.config(font=(12), bg=orange, fg=white, width=23)
            label.grid(column=0, row=0)

            button = Button(frame, text="Check Availability", command= lambda x=self.results[i]: self.CheckAvailability(x), bg=orange, fg=white)
            button.grid(column=1, row=0)
            frame.grid(column=0, row=i)
            self.resultFrames.append(frame)
            del frame

    def CheckAvailability(self, book):
        response = self.member.CheckAvailabilityOfBook(book.__ISBN)
        if isinstance(response, str):
            if self.member._reservedBook == book.__ISBN:
                pass
            elif self.member._reservedBook != None:
                pass
            else:
                pass
        elif isinstance(response, tuple):
            if self.member._reservedBook == book.__ISBN:
                pass
            else:
                pass
