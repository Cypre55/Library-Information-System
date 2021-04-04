from tkinter import *
from colors import *

class AddMemberFrame(Frame):
    def __init__(self, master, librarian):
        super().__init__(master)
        self.master = master
        self.librarian = librarian

        self.config(bg=lightorange, padx=380, pady=270) 

        self.memberID = StringVar()
        self.name = StringVar()
        self.password = StringVar()
        self.type = StringVar()
        self.optionList = ["UG", "PG", "RS", "FM"]
        self.type.set(self.optionList[0])

        self.titleLabel = Label(self, text="Add Member")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.memberIDFrame = Frame(self)
        self.memberIDFrame.config(bg=lightorange)
        self.memberIDLabel = Label(self.memberIDFrame, text = " Member ID: ")
        self.memberIDLabel.config(font=(12), bg=orange, fg=white, width=10)
        self.memberIDLabel.grid(column=0, row=0, padx=10)
        self.memberIDEntry = Entry(self.memberIDFrame, textvariable = self.memberID, show="*")
        self.memberIDEntry.grid(column=1, row=0)
        self.memberIDEntry.config(bg=lightorange, fg=white)
        self.memberIDFrame.grid(column=0, row=1, pady=10)

        self.nameFrame = Frame(self)
        self.nameFrame.config(bg=lightorange)
        self.nameLabel = Label(self.nameFrame, text = " Name: ")
        self.nameLabel.config(font=(12), bg=orange, fg=white, width=10)
        self.nameLabel.grid(column=0, row=0, padx=10)
        self.nameEntry = Entry(self.nameFrame, textvariable = self.name, show="*")
        self.nameEntry.grid(column=1, row=0)
        self.nameEntry.config(bg=lightorange, fg=white)
        self.nameFrame.grid(column=0, row=2, pady=10)

        self.passFrame = Frame(self)
        self.passFrame.config(bg=lightorange)
        self.passLabel = Label(self.passFrame, text = " Password: ")
        self.passLabel.config(font=(12), bg=orange, fg=white, width=10)
        self.passLabel.grid(column=0, row=0, padx=10)
        self.passEntry = Entry(self.passFrame, textvariable = self.password, show="*")
        self.passEntry.grid(column=1, row=0)
        self.passEntry.config(bg=lightorange, fg=white)
        self.passFrame.grid(column=0, row=3, pady=10)

        self.opt = OptionMenu(self, self.type, *self.optionList, command=self.SetType)
        self.opt.config(font=(12), bg=orange, fg=label_fg)
        self.opt.grid(column=0, row=4, pady=10)

        self.addMemberButton = Button(self, bg=orange, fg=white, text="Add Member to the System", command=self.AddMember)
        self.addMemberButton.grid(column=0, row=5)

        self.errorLabel = Label(self, text="")
        self.errorLabel.config(font=(12), bg=orange, fg=white)

        # self.DisplayError("HI")


    def SetType(self, selection):
        self.type.set(selection)

    def AddMember(self):
        self.RemoveError()
        print("Adding Member")
        print(self.type.get())

    def DisplayError(self, message): 
        self.errorLabel.grid_forget()
        self.errorLabel.config(text=message)
        self.errorLabel.grid(column=0, row=6, pady=10)

    def RemoveError(self):
        self.errorLabel.grid_forget()

class DeleteMemberFrame(Frame):
    def __init__(self, master, librarian):
        super().__init__(master)
        self.master = master
        self.librarian = librarian

        self.config(bg=lightorange, padx=370, pady=350) 

        self.memberID = StringVar()

        self.titleLabel = Label(self, text="Delete Member")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.memberIDFrame = Frame(self)
        self.memberIDFrame.config(bg=lightorange)
        self.memberIDLabel = Label(self.memberIDFrame, text = " Member ID: ")
        self.memberIDLabel.config(font=(12), bg=orange, fg=white, width=10)
        self.memberIDLabel.grid(column=0, row=0, padx=10)
        self.memberIDEntry = Entry(self.memberIDFrame, textvariable = self.memberID, show="*")
        self.memberIDEntry.grid(column=1, row=0)
        self.memberIDEntry.config(bg=lightorange, fg=white)
        self.memberIDFrame.grid(column=0, row=1, pady=10)

        self.addMemberButton = Button(self, bg=orange, fg=white, text="Delete Member from the System", command=self.DeleteMember)
        self.addMemberButton.grid(column=0, row=5)

        self.errorLabel = Label(self, text="")
        self.errorLabel.config(font=(12), bg=orange, fg=white) 

    def DeleteMember(self):
        self.RemoveError()
        print("Deleting Member")

    def DisplayError(self, message): 
        self.errorLabel.grid_forget()
        self.errorLabel.config(text=message)
        self.errorLabel.grid(column=0, row=6, pady=10)

    def RemoveError(self):
        self.errorLabel.grid_forget()       


class SendReminderFrame(Frame):
    def __init__(self, master, librarian):
        super().__init__(master)
        self.master = master
        self.librarian = librarian

        self.config(bg=lightorange, padx=340, pady=350) 

        self.titleLabel = Label(self, text="Send Reminders")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text="All members with overdue books will be sent a notiication.")
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        self.sendReminderButton = Button(self, bg=orange, fg=white, text="Send Reminders", command=self.SendReminder)
        self.sendReminderButton.grid(column=0, row=2)

        self.errorLabel = Label(self, text="")
        self.errorLabel.config(font=(12), bg=orange, fg=white) 

    def SendReminder(self):
        self.RemoveError()
        print("Sent Reminders")
    
    def DisplayError(self, message): 
        self.errorLabel.grid_forget()
        self.errorLabel.config(text=message)
        self.errorLabel.grid(column=0, row=3, pady=10)

    def RemoveError(self):
        self.errorLabel.grid_forget() 

class CheckIssueStats(Frame):
    def __init__(self, master, librarian):
        super().__init__(master)
        self.master = master
        self.librarian = librarian

        self.config(bg=lightorange, padx=340, pady=250)

        self.notIssued = self.GetNotIssued()

        self.titleLabel = Label(self, text="Check Issue Statistics")
        self.titleLabel.config(font=(40), bg=orange, fg=white)
        self.titleLabel.grid(column=0, row=0, pady=10)

        self.messageLabel = Label(self, text="Here's the list of books that haven't been return in 5 years.\n Select one by one and press Dispose")
        self.messageLabel.config(font=(40), bg=orange, fg=white)
        self.messageLabel.grid(column=0, row=1, pady=10)

        self.notIssuedFrame = Frame(self)
        self.notIssuedFrame.config(bg=lightorange)
        self.scroll = Scrollbar(self.notIssuedFrame)
        self.scroll.pack(side = RIGHT, fill = Y)

        self.notIssuedListbox = Listbox(self.notIssuedFrame, yscrollcommand = self.scroll.set, font = ("Arial", 10), selectbackground=orange,
                foreground=white, background=lightorange)
        self.notIssuedListbox.pack(side = LEFT, fill = BOTH)
        self.scroll.config(command = self.notIssuedListbox.yview)

        self.UpdateList()

        self.notIssuedFrame.grid(column=0, row=2, pady=10)

        self.disposeButton = Button(self, bg=orange, fg=white, text="Dispose Book", command=self.SendReminder)
        self.disposeButton.grid(column=0, row=3)

        self.errorLabel = Label(self, text="")
        self.errorLabel.config(font=(12), bg=orange, fg=white) 

    def GetNotIssued(self):
        return []

    def UpdateList(self):
        self.notIssuedListbox.delete(0,END)
        for book in self.notIssued:
            self.notIssuedListbox.insert(END, book)

    def SendReminder(self):
        self.RemoveError()
        print("Book Disposed")
    
    def DisplayError(self, message): 
        self.errorLabel.grid_forget()
        self.errorLabel.config(text=message)
        self.errorLabel.grid(column=0, row=4, pady=10)

    def RemoveError(self):
        self.errorLabel.grid_forget()         

