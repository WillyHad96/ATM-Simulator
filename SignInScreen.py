import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
from ATMFunctions import *

# Variables
correct_pin = 1996

def sign_in_screen():
    #main_window.destroy()
    global pin_entry
    global sign_in_window
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
        global correct_pin
        entered_pin = int(pin_entry.get())  # Retrieve the PIN entered by the user in tkinter entry
        #sign_in_window.destroy()
        if entered_pin == correct_pin:
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
    enter_button = Button(sign_in_window, text="Enter", command=check_pin, width=10).place(x=480, y=535)
    cancel_button = Button(sign_in_window, text="Cancel", command=sign_in_window.destroy, width=10).place(x=240, y=535)

    # Run the Pop Up Window
    sign_in_window.mainloop()
