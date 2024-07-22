# ATM Simulator

This ATM Simulator is a Python-based project that utilizes the tkinter library for the graphical user interface and sqlite3 for storing card information. The application allows users to register a card, sign in using a PIN, and perform various banking transactions such as checking the balance, withdrawing funds, depositing funds, printing transactions, changing the PIN, and transferring funds.



**GUI**

<img src="https://github.com/WillyHad96/ATM-Simulator/blob/main/ATMVideoGIFDef.gif" alt="Screenrecording" width="300" height="300">





**Features**

* Register a Card: Users can register their card by providing details such as name, card number, expiry date, CVC, and PIN.
* Sign In: Users can sign in using their PIN to access various banking functions.
* Check Balance: Users can check their current balance.
* Withdraw Funds: Users can withdraw a specified amount from their balance.
* Deposit Funds: Users can deposit a specified amount into their balance.
* Print Transactions: Users can print a list of their recent transactions.
* Change PIN: Users can change their card PIN.
* Transfer Funds: Users can transfer funds to another account.



**Installation**

1. Clone the repository:
   
```
git clone https://github.com/WillyHad96/ATM-Simulator/tree/main.git
```

2. Navigate to the project directory:
   
```
cd C:\Users\Usuario\OneDrive\Escritorio\My Coding Projects\Cloned Repositories\ATM-Simulator\.git\ATM-Simulator\
```

3. Install requirements.txt:
   
```
pip install -r requirements.txt
```


**Usage**

1. Run the application:
   
```
python AllinOneBankandATM.py
```

2. Register a new card:

* Click on the "Register" button.
* Fill in the card details and click "Enter".
  
3. Sign in:

* Click on the "Login" button.
* Enter your PIN and click "Enter".

4. Perform Transactions:

* Once signed in, choose from the available options (Check Balance, Withdraw Funds, Deposit Funds, etc.).



**Code Overview**


***Libraries***

```
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
```


***Variables***

```
user_balance = 0
transactions = ["NA"] * 10 
pin_value = 1111
```


***Functions***

* *create_window(window_identifier)*:
Creates a new window with a specified identifier.

* *register()*:
Displays the registration screen and saves card information to a SQLite database.

* *sign_in_screen()*:
Displays the sign-in screen and verifies the PIN.

* *save_transaction(transaction)*:
Saves a transaction to the list of transactions.

* *display_balance()*:
Displays the current balance.

* *withdraw_funds()*:
Handles fund withdrawal operations.

* *deposit_funds()*:
Handles fund deposit operations.

* *print_transactions()*:
Prints the list of recent transactions.

* *change_pin()*:
Allows users to change their PIN.

* *transfer_funds()*:
Handles fund transfer operations.

* *return_card()*:
Returns the card and closes the session.



**Main Program**

```
main_window = tk.Tk()
main_window.title("ATM")
main_window.resizable(width=False, height=False)
main_window.geometry("799x900+600+200")   

frame = tk.Frame(main_window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("ATM Image.png"))    
label = Label(frame, image=img)                                         
label.pack()

Button(main_window, text="Register", font=('Calibri', 12), width=15, height=1, command=register).place(x=430, y=425)
Button(main_window, text="Login", font=('Calibri', 12), width=15, command=sign_in_screen).place(x=240, y=425)

main_window.mainloop()
```



**License**

This project is licensed under the MIT License - see the LICENSE file for details.



**Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



**Acknowledgements**

* Python Software Foundation
* Pillow Library
* Tkinter Documentation
