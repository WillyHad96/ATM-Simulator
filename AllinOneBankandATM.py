#libraries
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
#First Commit

#variables
user_balance = 0
transactions = ["NA"]*10 
pin_value = 1111

# functions
        
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

    return new_window

def register():                             #REGISTER SCREEN
    global name
    global name
    global card_number
    global expiry_date
    global cvc
    global pin

    register_window = create_window("register_window")

    def save_card_info():
        global pin_value

        name_value = name.get()
        card_number_value = card_number.get()
        expiry_date_value = expiry_date.get()
        cvc_value = cvc.get()
        pin_value = int(pin.get())

        connection = sqlite3.connect("cardinfo.db")     #connect to database and create it if does not exist
        cursor = connection.cursor()                    

        cursor.execute("CREATE TABLE IF NOT EXISTS CardInfo(name TEXT, card_number INTEGER, expiry_date INTEGER, cvc INTEGER, pin INTEGER)")     #execute the SQL queries

        cursor.execute("INSERT INTO CardInfo VALUES (?,?,?,?,?)", (name_value, card_number_value, expiry_date_value, cvc_value, pin_value))     #insert the values into the table

        connection.commit()     #Close out the current transaction and applies the changes to the database
        connection.close()   #close the connection with the database
        register_window.destroy()

    Label(register_window, text="Name on Card:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=365, y=350)
    name = Entry(register_window, font=('Calibri', 10), width=20)
    name.place(x=340, y=375)
    Label(register_window, text="Card Number:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=365, y=400)
    card_number = Entry(register_window, font=('Calibri', 10), width=20)
    card_number.place(x=340, y=425)
    Label(register_window, text="Expiry Date:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=340, y=450)
    expiry_date = Entry(register_window, font=('Calibri', 12), width=5)
    expiry_date.place(x=350, y=475)
    Label(register_window, text="CVC:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=430, y=450)
    cvc = Entry(register_window, font=('Calibri', 12), width=3)
    cvc.place(x=435, y=475)
    Label(register_window, text="PIN:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=395, y=500)
    pin = Entry(register_window, font=('Calibri', 12), width=4)
    pin.place(x=390, y=525)
    enter_button = Button(register_window, text="Enter", command=save_card_info, width=10)
    enter_button.place(x=480, y=535)
    cancel_button = Button(register_window, text="Cancel", command=register_window.destroy, width=10)
    cancel_button.place(x=240, y=535)

def sign_in_screen():                       #SIGN IN SCREEN
    global sign_in_window
    global pin_entry
    # Create the Pop Up window
    sign_in_window = tk.Toplevel()
    sign_in_window.title("ATM")
    sign_in_window.resizable(width=False, height=False)
    sign_in_window.geometry("799x900+600+200")
    sign_in_window.lift()

    frame = tk.Frame(master=sign_in_window, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create the Image Background
    img = ImageTk.PhotoImage(Image.open("AllinOneBankandATM/ATM Image.png"))     
    label = Label(frame, image=img)                                         
    label.image = img  # Keep a reference to the image to prevent it from being garbage collected
    label.pack()

    # Labels and Entry
    Label(sign_in_window, text="Enter your PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
    pin_entry = Entry(sign_in_window, font=('Calibri', 15), width=4, show="*")
    pin_entry.place(x=370, y=450)

    # Functions
    def check_pin():
        global pin_entry
        global pin_value
        global correct_pin_window
        entered_pin = int(pin_entry.get())  # Retrieve the PIN entered by the user in tkinter entry
        #sign_in_window.destroy()
        if entered_pin == pin_value:
            correct_pin_window = Toplevel(sign_in_window)
            correct_pin_window.title("Correct PIN")
            correct_pin_window.geometry("799x900+600+200")
            correct_pin_window.resizable(width=False, height=False)
            correct_pin_window.lift(sign_in_window)

            # Create the Image Background
            img = ImageTk.PhotoImage(Image.open("AllinOneBankandATM/ATM Image.png"))
            label = Label(correct_pin_window, image=img)
            label.image = img  # Keep a reference to the image to prevent it from being garbage collected
            label.pack()

            # Buttons
            Button(correct_pin_window, text="Display Balance", font=('Calibri', 12), width=15, height=1, command=display_balance).place(x=430, y=425)
            Button(correct_pin_window, text="Withdraw Funds", font=('Calibri', 12), width=15, command=withdraw_funds).place(x=240, y=425)
            Button(correct_pin_window, text="Deposit Funds", font=('Calibri', 12), width=15, height=1, command=deposit_funds).place(x=430, y=460)
            Button(correct_pin_window, text="Print Transactions", font=('Calibri', 12), width=15, command=print_transactions).place(x=240, y=460)
            Button(correct_pin_window, text="Change PIN", font=('Calibri', 12), width=15, height=1, command=change_pin).place(x=430, y=495)
            Button(correct_pin_window, text="Transfer Funds", font=('Calibri', 12), width=15, command=transfer_funds).place(x=240, y=495)
            Button(correct_pin_window, text="Return Card", font=('Calibri', 12), width=15, height=1, command=return_card).place(x=430, y=530)

        else:
            incorrect_pin_window = Toplevel(sign_in_window)
            incorrect_pin_window.title("Incorrect PIN")
            incorrect_pin_window.geometry("799x900+600+200")
            incorrect_pin_window.resizable(width=False, height=False)
            incorrect_pin_window.lift(sign_in_window)

            # Create the Image Background
            img = ImageTk.PhotoImage(Image.open("AllinOneBankandATM/ATM Image.png"))
            label = Label(incorrect_pin_window, image=img)
            label.image = img  # Keep a reference to the image to prevent it from being garbage collected
            label.pack()

            Label(incorrect_pin_window, text="Your PIN is not correct, please reenter...", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)

            incorrect_pin_window.after(3000, incorrect_pin_window.destroy)


    # Button
    enter_button = Button(sign_in_window, text="Enter", command=check_pin, width=10)
    enter_button.place(x=480, y=535)
    cancel_button = Button(sign_in_window, text="Cancel", command=sign_in_window.destroy, width=10)
    cancel_button.place(x=240, y=535)

    # Run the Pop Up Window
    sign_in_window.mainloop()


def save_transaction(transaction):
    index_of_na = transactions.index('NA')
    transactions[index_of_na] = transaction


def display_balance():
        display_balance_window = create_window("display_balance_window")

        Label(display_balance_window, text=f'Your balance is ${user_balance}', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=340, y=430)

        display_balance_window.after(5000, display_balance_window.destroy)
        save_transaction("Balance Displayed")


def withdraw_funds():
    withdraw_funds_window = create_window("withdraw_funds_window")
    
    def enter_quantity():
        global quantity_entry
        enter_quantity_window = create_window('enter_quantity_window')

        def check_quantity():
            global user_balance
            entered_quantity = int(quantity_entry.get())
            if entered_quantity <= user_balance:
                user_balance -= entered_quantity
                save_transaction(f"Withdrawn ${entered_quantity}")
                successful_withdrawn_window = create_window('successful_withdrawn_window')
                Label(successful_withdrawn_window, text='Withdrawn Successful!', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=330, y=450)
                successful_withdrawn_window.after(3000, successful_withdrawn_window.destroy)
                enter_quantity_window.after(3001, enter_quantity_window.destroy)
                withdraw_funds_window.after(3002, withdraw_funds_window.destroy)
            else: 
                unsuccessful_withdrawn_window = create_window('unsuccessful_withdrawn_window')
                Label(unsuccessful_withdrawn_window, text='Sorry, you don\'t have enough funds... Please try again', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=250, y=450)
                unsuccessful_withdrawn_window.after(3000, unsuccessful_withdrawn_window.destroy) 

        Label(enter_quantity_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
        quantity_entry = Entry(enter_quantity_window, font=('Calibri', 15), width=5)
        quantity_entry.place(x=370, y=450)
        enter_button = Button(enter_quantity_window, text="Enter", command=check_quantity, width=10)
        enter_button.place(x=480, y=535)
        cancel_button = Button(enter_quantity_window, text="Cancel", command=enter_quantity_window.destroy, width=10)
        cancel_button.place(x=240, y=535)

    def withdraw(button_quantity):
        global user_balance
        if button_quantity <= user_balance:
            user_balance -= button_quantity
            save_transaction(f"Withdrawn ${button_quantity}")
            successful_withdrawn_window = create_window('successful_withdrawn_window')
            Label(successful_withdrawn_window, text='Withdrawn Successful!', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=330, y=450)
            successful_withdrawn_window.after(3000, successful_withdrawn_window.destroy)
            withdraw_funds_window.after(3001, withdraw_funds_window.destroy)
        else: 
            unsuccessful_withdrawn_window = create_window('unsuccessful_withdrawn_window')
            Label(unsuccessful_withdrawn_window, text='Sorry, you don\'t have enough funds... Please try again', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=250, y=450)
            unsuccessful_withdrawn_window.after(3000, unsuccessful_withdrawn_window.destroy) 


    Label(withdraw_funds_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=350, y=350)
    Button(withdraw_funds_window, text="10", font=('Calibri', 12), width=5, height=1, command=lambda: withdraw(10)).place(x=510, y=425)
    Button(withdraw_funds_window, text="20", font=('Calibri', 12), width=5, command=lambda: withdraw(20)).place(x=240, y=425)
    Button(withdraw_funds_window, text="50", font=('Calibri', 12), width=5, height=1, command=lambda: withdraw(50)).place(x=510, y=460)
    Button(withdraw_funds_window, text="100", font=('Calibri', 12), width=5, command=lambda: withdraw(100)).place(x=240, y=460)
    Button(withdraw_funds_window, text="200", font=('Calibri', 12), width=5, height=1, command=lambda: withdraw(200)).place(x=510, y=495)
    Button(withdraw_funds_window, text="Other", font=('Calibri', 12), width=5, height=1, command=enter_quantity).place(x=240, y=495)
    Button(withdraw_funds_window, text="Return to Main Menu", font=('Calibri', 12), width=18, command=withdraw_funds_window.destroy).place(x=240, y=530)
    Button(withdraw_funds_window, text="Return Card", font=('Calibri', 12), width=10, height=1, command=withdraw_funds_window.quit).place(x=470, y=530)



    

def deposit_funds():
    deposit_funds_screen = create_window('deposit_funds_window')
    def deposit():
        deposit_window = create_window('deposit_window')
        def deposit_other_quantity():
            deposit_other_quantity_window = create_window('deposit_other_quantity_window')
            Label(deposit_other_quantity_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=350, y=400)
            quantity_deposited_entry = Entry(deposit_other_quantity_window, font=('Calibri', 15), width=4)
            quantity_deposited_entry.place(x=370, y=450)
            def successfull_deposit():
                global user_balance
                deposited_quantity = int(quantity_deposited_entry.get())
                user_balance += deposited_quantity
                save_transaction(f"Deposited ${deposited_quantity}")
                successful_deposited_window = create_window('successful_deposited_window')
                Label(successful_deposited_window, text=f'Successful!y deposited ${deposited_quantity}!', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=330, y=450)
                successful_deposited_window.after(3000, successful_deposited_window.destroy)
                deposit_other_quantity_window.after(3001, deposit_other_quantity_window.destroy)
                deposit_window.after(3002, deposit_window.destroy)
                deposit_funds_screen.after(3003, deposit_funds_screen.destroy)
            enter_button = Button(deposit_other_quantity_window, text="Enter", command=successfull_deposit, width=10)
            enter_button.place(x=480, y=535)
            cancel_button = Button(deposit_other_quantity_window, text="Cancel", command=deposit_other_quantity_window.destroy, width=10)
            cancel_button.place(x=240, y=535)

        def deposit_amount(button_amount):
                global user_balance
                user_balance += button_amount
                save_transaction(f"Deposited ${button_amount}")
                successful_deposited_window = create_window('succesful_deposited_window')
                Label(successful_deposited_window, text=f'Successfully Deposited ${button_amount}!', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=330, y=450)
                successful_deposited_window.after(3000, successful_deposited_window.destroy)
                deposit_window.after(3001, deposit_window.destroy)
                deposit_funds_screen.after(3002, deposit_funds_screen.destroy)

        Label(deposit_window, text='How much?', font=('Calibri', 15, 'bold'), fg="white", bg="#164794").place(x=350, y=350)
        Button(deposit_window, text="10", font=('Calibri', 12), width=5, height=1, command=lambda:deposit_amount(10)).place(x=510, y=425)
        Button(deposit_window, text="20", font=('Calibri', 12), width=5, command=lambda:deposit_amount(20)).place(x=240, y=425)
        Button(deposit_window, text="50", font=('Calibri', 12), width=5, height=1, command=lambda:deposit_amount(50)).place(x=510, y=460)
        Button(deposit_window, text="100", font=('Calibri', 12), width=5, command=lambda:deposit_amount(100)).place(x=240, y=460)
        Button(deposit_window, text="200", font=('Calibri', 12), width=5, height=1, command=lambda:deposit_amount(200)).place(x=510, y=495)
        Button(deposit_window, text="Other", font=('Calibri', 12), width=5, height=1, command=deposit_other_quantity).place(x=240, y=495)
    Button(deposit_funds_screen, text="Deposit", font=('Calibri', 12), width=18, height=1, command=deposit).place(x=240, y=495)
    Button(deposit_funds_screen, text="Return to Main Menu", font=('Calibri', 12), width=18, command=deposit_funds_screen.destroy).place(x=240, y=530)
    Button(deposit_funds_screen, text="Return Card", font=('Calibri', 12), width=18, height=1, command=deposit_funds_screen.quit).place(x=405, y=530)

    

def print_transactions():
    print_transactions_window = create_window("Print Transactions")
    for i in range(min(10, len(transactions))):
        transaction = transactions[i]
        Label(print_transactions_window, text=f'Transaction {i+1}: {transaction}', font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=325, y=345 + i*22)
    print_transactions_window.after(5000, print_transactions_window.destroy)
    save_transaction("Printed List of Transactions")


def change_pin():
    change_pin_window = create_window("change_pin_window")
    pin_entry = Entry(change_pin_window, font=('Calibri', 15), width=4, show="*")
    pin_entry.place(x=370, y=450)
    
    def check_pin():
        entered_pin = int(pin_entry.get())
        if entered_pin == pin_value:
            correct_pin_window = create_window('correct_pin_window') 
            Label(correct_pin_window, text="Enter your new PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=320, y=400)
            new_pin_entry = Entry(correct_pin_window, font=('Calibri', 15), width=4, show="*")
            new_pin_entry.place(x=370, y=450)
            def pin_successfully_changed():
                global pin_value
                pin_value = int(new_pin_entry.get())  #Update PIN
                save_transaction("PIN updated")
                pin_successfully_changed_window = create_window('pin_successfully_changed_window')
                Label(pin_successfully_changed_window, text="PIN successfully changed!", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=320, y=450)
                pin_successfully_changed_window.after(3000, pin_successfully_changed_window.destroy)
                correct_pin_window.after(3001, correct_pin_window.destroy)
                change_pin_window.after(3002, change_pin_window.destroy)
                
            enter_button = Button(correct_pin_window, text="Enter", command=pin_successfully_changed, width=10)
            enter_button.place(x=480, y=535)
            cancel_button = Button(correct_pin_window, text="Cancel", command=correct_pin_window.destroy, width=10)
            cancel_button.place(x=240, y=535)
        else:
            incorrect_pin_window = create_window('incorrect_pin_window')
            Label(incorrect_pin_window, text="Your PIN is not correct, please reenter...", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=300, y=450)
            incorrect_pin_window.after(3000, incorrect_pin_window.destroy)
            pin_entry.delete(0, END)  # Clear the entry widget
    
    Label(change_pin_window, text="Enter your PIN:", font=('Calibri', 12, 'bold'), fg="white", bg="#164794").place(x=340, y=400)
    enter_button = Button(change_pin_window, text="Enter", command=check_pin, width=10)
    enter_button.place(x=480, y=535)
    cancel_button = Button(change_pin_window, text="Cancel", command=change_pin_window.destroy, width=10)
    cancel_button.place(x=240, y=535)

def transfer_funds():
    transfer_funds_window = create_window('transfer_funds_window')
    def succesfully_transferred_funds():
        save_transaction("Funds Transferred")
        succesfully_transferred_funds_window = create_window("succesfully_transferred_funds_window")
        Label(succesfully_transferred_funds_window, text="Funds succesfully transferred!", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=320, y=450)
        succesfully_transferred_funds_window.after(3000, succesfully_transferred_funds_window.destroy)
        transfer_funds_window.after(3001, transfer_funds_window.destroy)
        

    Label(transfer_funds_window, text="Amount:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=360, y=350)
    Entry(transfer_funds_window, font=('Calibri', 12), width=5).place(x=365, y=375)
    Label(transfer_funds_window, text="Recipient:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=357, y=400)
    Entry(transfer_funds_window, font=('Calibri', 12), width=20).place(x=305, y=425)
    Label(transfer_funds_window, text="Bank Account:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=350, y=450)
    Entry(transfer_funds_window, font=('Calibri', 12), width=20).place(x=305, y=475)
    Label(transfer_funds_window, text="BIC:", font=('Calibri', 10, 'bold'), fg="white", bg="#164794").place(x=375, y=500)
    Entry(transfer_funds_window, font=('Calibri', 12), width=6).place(x=362, y=525)

    enter_button = Button(transfer_funds_window, text="Enter", command=succesfully_transferred_funds, width=10)
    enter_button.place(x=480, y=535)
    cancel_button = Button(transfer_funds_window, text="Cancel", command=transfer_funds_window.destroy, width=10)
    cancel_button.place(x=240, y=535)

def return_card():
    correct_pin_window.quit()


 
# main program
# Create the Pop Up window                                   #SIGN IN AND REGISTER SCREEN
main_window = tk.Tk()
main_window.title("ATM")
main_window.resizable(width=False, height=False)
main_window.geometry("799x900+600+200")   

frame = tk.Frame(main_window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


# Create the Image Background
img = ImageTk.PhotoImage(Image.open("AllinOneBankandATM/ATM Image.png"))    
label = Label(frame, image=img)                                         
label.pack()


#Buttons
Button(main_window, text="Register", font=('Calibri', 12), width=15, height=1, command=register).place(x=430, y=425)
Button(main_window, text="Login", font=('Calibri', 12), width=15, command=sign_in_screen).place(x=240, y=425)


#Run the Pop Up Window
main_window.mainloop()