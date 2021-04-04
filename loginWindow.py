from tkinter import *
from colors import *
from loginFunctions import *

class LoginWindow(Frame):
    def __init__(self, master, mainWindow):
        super().__init__(master)
        self.master = master
        self.mainWindow = mainWindow

        self.bg = lightorange

        self.config(bg=self.bg)

        self.optionList = ["Member", "Employee"]
        self.variable = StringVar(self.master)
        self.variable.set(self.optionList[0])

        self.opt = OptionMenu(self, self.variable, *self.optionList, command=self.ChangeLogin)
        self.opt.config(font=(12), bg=orange, fg=label_fg)
        self.opt.grid(column=0, row=0, padx=670, pady=130)

        self.id = ""
        self.password = ""

        self.loginFrame = Frame(self)
        self.loginFrame.config(bg=orange, padx=100, pady=50)

        self.idFrame = Frame(self.loginFrame)
        self.passFrame = Frame(self.loginFrame)
        
        self.MemberInfo()
        
        self.idEntry = Entry(self.idFrame, textvariable = self.id)
        self.idEntry.grid(column=1, row=0)
        self.idEntry.config(bg=lightorange, fg=white)
        
        self.passLabel = Label(self.passFrame, text = " Password: ")
        self.passLabel.config(font=(12), bg=orange, fg=white)
        self.passLabel.grid(column=0, row=0)
        
        self.passEntry = Entry(self.passFrame, textvariable = self.password)
        self.passEntry.grid(column=1, row=0)
        self.passEntry.config(bg=lightorange, fg=white)
        
        self.idFrame.grid(column=0,row=1, pady=10)
        
        self.passFrame.grid(column=0, row=2, pady=10)

        self.loginButton = Button(self.loginFrame, bg=orange, fg=white, text="Login", command=self.Login)
        self.loginButton.grid(column=0, row=3, pady=10)

        self.errorLabel = Label(self.loginFrame, text="")
        self.errorLabel.config(font=(12), bg=orange, fg=white)
        # self.errorLabel.grid(column=0, row=4, pady=10)
        
        self.loginFrame.grid(column=0, row=1, pady=110)

        self.exitButton = Button(self, bg=orange, fg=white, text="Exit", command=exit)
        self.exitButton.grid(column=0, row=4, pady=10)

        # self.DisplayError("OOPS!!!")

    def ChangeLogin(self, selection):
        if selection == "Member":
            self.MemberInfo()
        else:
            self.EmployeeInfo()

    def MemberInfo(self):
        if hasattr(self, 'employeeLabel'):
            self.employeeLoginLabel.grid_forget()
            self.employeeLabel.grid_forget()
        if not hasattr(self, 'memberLabel'):
            self.memberLoginLabel = Label(self.loginFrame, text="MEMBER LOGIN")
            self.memberLoginLabel.config(font=(12), bg=orange, fg=white, padx=50, pady=10)
            self.memberLabel = Label(self.idFrame, text = " MemberID: ")
            self.memberLabel.config(width=10, font=(12), bg=orange, fg=white)
        self.memberLoginLabel.grid(column=0, row =0)
        self.memberLabel.grid(column=0, row=0)

    def EmployeeInfo(self):
        if hasattr(self, 'memberLabel'):
            self.memberLabel.grid_forget()
            self.memberLoginLabel.grid_forget()
        if not hasattr(self, 'employeeLabel'):
            self.employeeLoginLabel = Label(self.loginFrame, text="EMPLOYEE LOGIN")
            self.employeeLoginLabel.config(font=(12), bg=orange, fg=white, padx=50, pady=10)
            self.employeeLabel = Label(self.idFrame, text = " EmployeeID: ")
            self.employeeLabel.config(width=10, font=(12), bg=orange, fg=white)
        self.employeeLoginLabel.grid(column=0, row =0)
        self.employeeLabel.grid(column=0, row=0)

    def Login(self):
        if self.variable.get() == "Member":
            try:
                MemberLogin(self.id, self.password)
            except ValueError as e:
                self.DisplayError(e)
                # print(ValueError.message)
            self.mainWindow.ShowMemberHome()
            self.RemoveError()
        else:
            self.DisplayError("OOPS!!!")
            print("HELLO")

    def DisplayError(self, message):
        self.errorLabel.config(text=message)
        self.errorLabel.grid(column=0, row=4, pady=10)

    def RemoveError(self):
        self.errorLabel.grid_forget()
