from tkinter import *
from colors import *
from tkinter import ttk

class AvailableFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

        self.config(bg = lightorange, pady=0)

        self.titleLabel = Label(self, text="Available Books")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text="The following copies of the book are available.\n Please select one to issue.")
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        response = ([1, 2], [1, 2])
        cols = ('UID', 'Rack No.')
        ttk.Style().configure("Treeview", background=orange,
                foreground=white, fieldbackground=lightorange)
        self.listBox = ttk.Treeview(self, columns=cols, show='headings', selectmode="browse")
        for col in cols:
            self.listBox.heading(col, text=col)   
        for i in range(len(response[0])):
            self.listBox.insert("", "end", values=(response[0][i], response[1][i]))

        self.listBox.grid(column=0, row=2, padx=10, pady=10)
        
        # self.listBox.bind("<<TreeviewSelect>>", self.onTreeSelect)
        self.buttonFrame = Frame(self)
        self.buttonFrame.config(bg=lightorange)
        self.issueButton = Button(self.buttonFrame, bg=orange, fg=white, text="Issue Book", command=self.IssueBook)
        self.issueButton.grid(column=0, row=0, padx=10, pady=10)
        self.cancelButton = Button(self.buttonFrame, bg=orange, fg=white, text="Go Back", command=self.master.destroy)
        self.cancelButton.grid(column=1, row=0)
        self.buttonFrame.grid(column=0,row=3, padx=10, pady=10)

    def IssueBook(self):
        print(self.listBox.item(self.listBox.selection()[0], "value"))
        

class ClaimFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

        self.config(bg = lightorange, pady=0)

        self.titleLabel = Label(self, text="Claim Available Books")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text="You have an active reservation for this book.\n Please select one to issue.")
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        response = ([1, 2], [1, 2])
        cols = ('UID', 'Rack No.')
        ttk.Style().configure("Treeview", background=orange,
                foreground=white, fieldbackground=lightorange)
        self.listBox = ttk.Treeview(self, columns=cols, show='headings')
        for col in cols:
            self.listBox.heading(col, text=col)   
        for i in range(len(response[0])):
            self.listBox.insert("", "end", values=(response[0][i], response[1][i]))

        self.listBox.grid(column=0, row=2, padx=10, pady=10)

        self.buttonFrame = Frame(self)
        self.buttonFrame.config(bg=lightorange)
        self.claimButton = Button(self.buttonFrame, bg=orange, fg=white, text="Claim Book", command=self.ClaimBook)
        self.claimButton.grid(column=0, row=0, padx=10, pady=10)
        self.cancelButton = Button(self.buttonFrame, bg=orange, fg=white, text="Go Back", command=self.master.destroy)
        self.cancelButton.grid(column=1, row=0)
        self.buttonFrame.grid(column=0,row=3, padx=10, pady=10)

    def ClaimBook(self):
        print(self.listBox.item(self.listBox.selection()[0], "value"))
        

class PendingFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

        self.config(bg = lightorange, pady=0)

        self.titleLabel = Label(self, text="Pending Reservation")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text=response)
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        self.buttonFrame = Frame(self)
        self.buttonFrame.config(bg=lightorange)
        # self.claimButton = Button(self.buttonFrame, bg=orange, fg=white, text="Claim Book", command=self.ClaimBook)
        # self.claimButton.grid(column=0, row=0, padx=10, pady=10)
        self.cancelButton = Button(self.buttonFrame, bg=orange, fg=white, text="Go Back", command=self.master.destroy)
        self.cancelButton.grid(column=0, row=0)
        self.buttonFrame.grid(column=0,row=2, padx=10, pady=10)

class ReserveFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

        self.config(bg = lightorange, pady=0)

        self.titleLabel = Label(self, text="Reserve Book")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text=response)
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        self.buttonFrame = Frame(self)
        self.buttonFrame.config(bg=lightorange)
        self.reserveButton = Button(self.buttonFrame, bg=orange, fg=white, text="Reserve Book", command=self.ReserveBook)
        self.reserveButton.grid(column=0, row=0, padx=10, pady=10)
        self.cancelButton = Button(self.buttonFrame, bg=orange, fg=white, text="Go Back", command=self.master.destroy)
        self.cancelButton.grid(column=1, row=0)
        self.buttonFrame.grid(column=0,row=2, padx=10, pady=10)

    def ReserveBook(self):
        pass

class NoReserveFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

        self.config(bg = lightorange, pady=0)

        self.titleLabel = Label(self, text="Reserve Book")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text=response)
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        self.buttonFrame = Frame(self)
        self.buttonFrame.config(bg=lightorange)
        # self.claimButton = Button(self.buttonFrame, bg=orange, fg=white, text="Claim Book", command=self.ClaimBook)
        # self.claimButton.grid(column=0, row=0, padx=10, pady=10)
        self.cancelButton = Button(self.buttonFrame, bg=orange, fg=white, text="Go Back", command=self.master.destroy)
        self.cancelButton.grid(column=0, row=0)
        self.buttonFrame.grid(column=0,row=1, padx=10, pady=10)