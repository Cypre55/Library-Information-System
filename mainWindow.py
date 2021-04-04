from tkinter import *
from colors import *
from loginWindow import LoginWindow
from memberHomeWindow import MemberHomeWindow

class MainWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Library Information System")
        self.master.geometry('1500x900')
        self.master.config(bg=orange)

        self.title = Label(self.master, text="Library Information System", padx=700, pady=10)
        self.title.config(width=10, font=(12), bg=orange, fg=white)
        self.title.grid(column=0, row=0)
        self.currWindow = ""
        # self.ShowLogin()
        # self.currWindow.grid_forget()
        self.ShowMemberHome()

    def ShowLogin(self):
        if self.currWindow:
            self.currWindow.grid_forget()
        if not hasattr(self, 'login'):
            self.login = LoginWindow(self.master, self)
        self.currWindow = self.login
        self.login.grid(column=0, row=1)

    def RemoveLogin(self):
        if hasattr(self, 'login'):
            self.login.grid_forget()

    def ShowMemberHome(self):
        if self.currWindow:
            self.currWindow.grid_forget()
        if hasattr(self, 'memberHome'):
            del self.memberHome
        self.memberHome = MemberHomeWindow(self.master, self)
        self.currWindow = self.memberHome
        self.memberHome.grid(column=0, row=1)

root = Tk()
app = MainWindow(root)
root.mainloop()