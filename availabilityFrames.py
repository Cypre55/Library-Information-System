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

        response = [{"UID": "1", "RackNo": "1"},
                 {"UID": "2", "RackNo": "2"}
                ]
        cols = ('UID', 'Rack No.')
        ttk.Style().configure("Treeview", background=orange,
                foreground=white, fieldbackground=lightorange)
        self.listBox = ttk.Treeview(self, columns=cols, show='headings')
        for col in cols:
            self.listBox.heading(col, text=col)   
        for book in books:
            self.listBox.insert("", "end", values=(book["Title"], book["UID"], book["DueDate"]))

        self.listBox.grid(column=0, row=4)
        

class ClaimFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

class PendingFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

class ReserveFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)

class NoReserveFrame(Frame):
    def __init__(self, master, member, response):
        super().__init__(master)