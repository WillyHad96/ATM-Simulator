#This is the screen where the user can register and create a Card acount

# import tkinter as tk
# from tkinter import Label, Entry, Frame, Button
# from PIL import ImageTk, Image
# #import time
# #import sys

class User():
    def __init__(self, name, number, expiry_date, cvc, PIN):
        self.name = name
        self.number = number
        self.expiry_date = expiry_date
        self.cvc = cvc
        self.PIN = PIN

    def show_details(self):
        print("Personal Details:")
        print("")
        print("Name: ", self.name)
        print("Card Number: ", self.number)
        print("Expiry Date: ", self.expiry_date)
        print("CVC: ", self.cvc)
        print("PIN: ", self.PIN)



class Card(User):
    def __init__(self, PIN):
        super().__init__(self, PIN)
        self.balance = 0

    def deposit (self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account Balance has been updated: $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds / Balance Available: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account Balance has been updated: $",self.balance)

    def view_balance(self):
        self.show_details()
        print("Account Balance has been updated: $",self.balance)

# johan = Card('Johan', 1111 1111 1111 1111, 05/01, 123, 1234)
# johan.deposit(50)
# johan.withdraw(30)
# johan.view_balance()

#Functions

def register():
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age =  StringVar()
    temp_gender =  StringVar()
    temp_password = StringVar() 

    register_window = create_window("register_window")

    def finish_reg():
    name = temp_name.get()
    age = temp_name.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="All fields required * ")
        return
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exist")
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.close()
            notif.config(fg="green", text="Account has been created")

    Label(register_window, text="Name on Card:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
    Entry(register_window, font=('Calibri', 12), width=10).place(x=370, y=450)
    Label(register_window, text="Card Number:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=500)
    Entry(register_window, font=('Calibri', 12), width=10).place(x=370, y=550)
    Label(register_window, text="Expiry Date:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=600)
    Entry(register_window, font=('Calibri', 15), width=4).place(x=370, y=650)
    Label(register_window, text="CVC:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=700)
    Entry(register_window, font=('Calibri', 15), width=3).place(x=370, y=750)
    Label(register_window, text="PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=700)
    Entry(register_window, font=('Calibri', 15), width=4).place(x=370, y=750)
    enter_button = Button(register_window, text="Enter", command=finish_reg, width=10).place(x=480, y=535)
    cancel_button = Button(register_window, text="Cancel", command=register_window.destroy, width=10).place(x=240, y=535)


