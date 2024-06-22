#This is the screen where all ATM options will display, once the customer has already registered or signed in

import tkinter as tk
from tkinter import Label, Entry, Frame, Button
from PIL import ImageTk, Image
import time
import sys
from SignInScreen import *

# Variables
user_balance = 100
correct_pin = '1996'
transactions = ['NA'] * 10

# Functions
def create_window(window_identifier):
    new_window = tk.Toplevel()
    new_window.title("ATM")  
    new_window.resizable(width=False, height=False)
    new_window.geometry("799x900+600+200")
    new_window.lift()

    frame = tk.Frame(master=new_window, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create the Image Background
    img = ImageTk.PhotoImage(Image.open("AllinOneBankandATM/ATM Image.png"))     
    label = Label(frame, image=img)                                         
    label.image = img  
    label.pack()

    new_window.mainloop()

    return new_window

#change_pin_window = create_window("change_pin_window")  This is how to create a new window


def save_transactions(transactions):
    with open("transactions.txt", "w") as file:
        for transaction in transactions:
            file.write(transaction + "\n")
    print("Transactions saved successfully.")


def display_balance():
        display_balance_window = create_window("display_balance_window")

        Label(display_balance_window, text=f'Your balance is ${user_balance}', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)

        display_balance_window.after(5000, display_balance_window.destroy)
        save_transactions()


def withdraw_funds():
    withdraw_funds_window = create_window("withdraw_funds_window")
    def enter_quantity():
        enter_quantity_window = create_window('enter_quantity_window')

        Label(withdraw_funds_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
        quantity_entry = Entry(enter_quantity_window, font=('Calibri', 15), width=4)

        entered_quantity = int(quantity_entry.get())

        if entered_quantity <= user_balance:
            succesfull_withdrawn_window = create_window('succesfull_withdrawn_window')
            Label(succesfull_withdrawn_window, text='Withdrawn Succesful!', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            succesfull_withdrawn_window.after(5000, succesfull_withdrawn_window.destroy)
        else: 
            unsuccesfull_withdrawn_window = create_window('unsuccesfull_withdrawn_window')
            Label(succesfull_withdrawn_window, text='Sorry, you don´t have enough funds... Please try again', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            unsuccesfull_withdrawn_window.after(5000, unsuccesfull_withdrawn_window.destroy)            

    Label(withdraw_funds_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
    Button(withdraw_funds_window, text="10", font=('Calibri', 12), width=5, height=1, command=user_balance - 10).place(x=430, y=425)
    Button(withdraw_funds_window, text="20", font=('Calibri', 12), width=5, command=user_balance - 20).place(x=240, y=425)
    Button(withdraw_funds_window, text="50", font=('Calibri', 12), width=5, height=1, command=user_balance - 50).place(x=430, y=460)
    Button(withdraw_funds_window, text="100", font=('Calibri', 12), width=5, command=user_balance - 100).place(x=240, y=460)
    Button(withdraw_funds_window, text="Other", font=('Calibri', 12), width=15, height=1, command=enter_quantity).place(x=430, y=495)
    Button(withdraw_funds_window, text="Return to Main Menu", font=('Calibri', 12), width=15, command=main_menu_window).place(x=240, y=495)
    Button(withdraw_funds_window, text="Return Card", font=('Calibri', 12), width=15, height=1, command=withdraw_funds_window.destroy).place(x=430, y=530)
    save_transactions()

    

def deposit_funds():
    deposit_funds_screen = create_window('deposit_funds_window')
    def deposit():
        deposit_window = create_window('deposit_window')
        def deposit_quantity():
            deposit_quantity_window = create_window('deposit_quantity_window')

            Label(deposit_quantity_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            quantity_deposited_entry = Entry(deposit_quantity_window, font=('Calibri', 15), width=4)
            enter_button = Button(deposit_quantity_window, text="Enter", command=deposit_quantity_window, width=10).place(x=480, y=535)
            cancel_button = Button(deposit_quantity_window, text="Cancel", command=deposit_quantity_window.destroy, width=10).place(x=240, y=535)

            deposited_quantity = int(quantity_deposited_entry.get())

            succesfull_deposit_window = create_window('succesfull_withdrawn_window')
            Label(succesfull_deposit_window, text=f'Succesfully deposited ${deposited_quantity}', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            succesfull_deposit_window.after(3000, succesfull_deposit_window.destroy)

        Label(deposit_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
        Button(deposit_window, text="10", font=('Calibri', 12), width=5, height=1, command=user_balance + 10).place(x=430, y=425)
        Button(deposit_window, text="20", font=('Calibri', 12), width=5, command=user_balance + 20).place(x=240, y=425)
        Button(deposit_window, text="50", font=('Calibri', 12), width=5, height=1, command=user_balance + 50).place(x=430, y=460)
        Button(deposit_window, text="100", font=('Calibri', 12), width=5, command=user_balance + 100).place(x=240, y=460)
        Button(deposit_window, text="Other", font=('Calibri', 12), width=15, height=1, command=deposit_quantity).place(x=430, y=495)

    Button(deposit_funds_screen, text="Deposit", font=('Calibri', 12), width=5, height=1, command=deposit).place(x=430, y=425)
    Button(deposit_funds_screen, text="Return to Main Menu", font=('Calibri', 12), width=5, command=user_balance - 20).place(x=240, y=425)
    Button(deposit_funds_screen, text="Return Card", font=('Calibri', 12), width=5, height=1, command=deposit_funds_screen.quit).place(x=430, y=460)
    save_transactions()

    

def print_transactions():
    print_transactions_window = create_window("Print Transactions")
    for i in range(min(10, len(transactions))):
        transaction = transactions[i]
        Label(print_transactions_window, text=f'Transaction {i+1}: {transaction}', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=50, y=50 + i*30)
    save_transactions()


def change_pin():
    change_pin_window = create_window("change_pin_window")
    def check_pin():
        global correct_pin
        entered_pin = int(pin_entry.get())  # Retrieve the PIN entered by the user in tkinter entry
        #change_pin_window.destroy()
        if entered_pin == correct_pin:   
            correct_pin_window = create_window('correct_pin_window') 
            def pin_succesfully_changed():
                pin_succesfully_changed_window = create_window('pin_succesfully_changed_window')
                Label(pin_succesfully_changed_window, text="PIN succesfully changed!", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
                pin_succesfully_changed_window.after(3000, pin_succesfully_changed_window.destroy)
            Label(correct_pin_window, text="Enter your PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
            pin_entry = Entry(correct_pin_window, font=('Calibri', 15), width=4, show="*").place(x=370, y=450)
            enter_button = Button(correct_pin_window, text="Enter", command=pin_succesfully_changed, width=10).place(x=480, y=535)
            cancel_button = Button(correct_pin_window, text="Cancel", command=correct_pin_window.destroy, width=10).place(x=240, y=535)

        else: 
            incorrect_pin_window = create_window('incorrect_pin_window')
            Label(incorrect_pin_window, text="Your PIN is not correct, please reenter...", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            incorrect_pin_window.after(3000, incorrect_pin_window.destroy)
            enter_button = Button(incorrect_pin_window, text="Enter", command=check_pin, width=10).place(x=480, y=535)
            cancel_button = Button(incorrect_pin_window, text="Cancel", command=incorrect_pin_window.destroy, width=10).place(x=240, y=535)
    
    Label(change_pin_window, text="Enter your PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
    pin_entry = Entry(change_pin_window, font=('Calibri', 15), width=4, show="*").place(x=370, y=450)
    enter_button = Button(change_pin_window, text="Enter", command=check_pin, width=10).place(x=480, y=535)
    cancel_button = Button(change_pin_window, text="Cancel", command=change_pin_window.destroy, width=10).place(x=240, y=535)
    save_transactions()

def transfer_funds():
    transfer_funds_window = create_window('transfer_funds_window')
    def succesfully_transferred_funds():
        succesfully_transferred_funds_window = create_window("succesfully_transferred_funds_window")
        Label(succesfully_transferred_funds_window, text="Funds succesfully Transferred!", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
        succesfully_transferred_funds_window.after(5000, succesfully_transferred_funds_window.destroy)

    Label(transfer_funds_window, text="Amount:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
    Entry(transfer_funds_window, font=('Calibri', 15), width=4).place(x=370, y=450)
    Label(transfer_funds_window, text="Recipient:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=500)
    Entry(transfer_funds_window, font=('Calibri', 15), width=4).place(x=370, y=550)
    Label(transfer_funds_window, text="BIC:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=600)
    Entry(transfer_funds_window, font=('Calibri', 15), width=4).place(x=370, y=650)
    Label(transfer_funds_window, text="Bank Account:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=700)
    Entry(transfer_funds_window, font=('Calibri', 15), width=4).place(x=370, y=750)
    enter_button = Button(transfer_funds_window, text="Enter", command=succesfully_transferred_funds, width=10).place(x=480, y=535)
    cancel_button = Button(transfer_funds_window, text="Cancel", command=transfer_funds_window.destroy, width=10).place(x=240, y=535)
    save_transactions()

def return_card():
    correct_pin_window.quit()