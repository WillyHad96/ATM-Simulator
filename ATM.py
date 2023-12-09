#IMPORTING LIBRARIES

import time
import sys

#CONSTANTS

user_balance = 100
user_pin = '1996'
transactions = ['NA'] * 10

#FUNCTIONS

def display_balance():
    print("Display Balance")
    print(f'${user_balance}\n')
    time.sleep(0.25)

def withdraw_funds():
    print("Withdraw Funds")
    time.sleep(0.75)
    wf_options = {10: 10, 20: 20, 50: 50, 100: 100}
    wf = int(input('''
    How much would you like to withdraw?
    Your options are:
    10:
    20:
    50:
    100:
    7 - Other (Must be a multiple of 10)
    8 - Return to main menu:
    9 - Return card:

    --->: '''))

    if wf in wf_options:
        handle_successful_withdrawal(wf)
    elif wf == 7:
        handle_other_withdrawal()
    elif wf == 8:
        print()
    elif wf == 9:
        print("Thank you for Banking at WillCodeIT Bank")
        sys.exit()
    else:
        print("Invalid\n")

def handle_successful_withdrawal(amount):
    global user_balance
    global yes
    global transactions
    print(f'Successfully withdrawn ${amount}, so you now have ${user_balance - amount}\n')
    user_balance -= amount
    never = f'Withdrew ${amount}'
    update_transactions(never)

def handle_other_withdrawal():
    global user_balance
    ea = int(input("How much would you like to withdraw?: "))
    if ea % 10 == 0:
        print(f'Successfully withdrawn ${ea}, you now have ${user_balance - ea}\n')
        user_balance -= ea
        never = f'Withdrew ${ea}'
        update_transactions(never)
    else:
        print("Invalid\nMake sure it is a multiple of 10 and numbers only\n")

def update_transactions(transaction):
    global yes
    global transactions
    yes += 1
    if yes > 10:
        transactions[:-1] = transactions[1:]
        transactions[-1] = transaction
    elif yes == 1:
        transactions[0] = transaction
    elif 2 <= yes <= 10:
        transactions[yes - 1] = transaction

def deposit_funds():
    global user_balance
    global yes
    global transactions
    print("Deposit Funds")
    EA = int(input('''
    Choose an option:
    1 - Deposit
    2 - Return to main menu
    9 - Return card

    -->: '''))
    if EA == 1:
        dp = int(input("How much would you like to deposit?: "))
        if dp >= 0:
            print(f"Successfully Deposited ${dp}, you now have ${user_balance + dp}\n")
            user_balance += dp
            never = f'Deposited ${dp}'
            update_transactions(never)
        else:
            print("You cannot deposit negative amounts\n")
    elif EA == 2:
        print()
    elif EA == 9:
        print("Thank you for Banking at WillCodeIT Bank")
        sys.exit()
    else:
        print("Invalid option\n")

def print_transactions():
    print("Print list of transactions:")
    time.sleep(0.75)
    print('\n'.join(transactions) + '\n')

def change_pin():
    global user_pin
    print("Change PIN")
    new_pin = input("Enter a new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        user_pin = new_pin
        print(f"PIN successfully changed to {new_pin}\n")
    else:
        print("Invalid PIN. Please enter a 4-digit number.\n")

def transfer_funds():
    global user_balance
    global transactions
    print("Transfer Funds")
    transfer_amount = int(input("Enter the amount to transfer: "))
    if transfer_amount <= user_balance:
        recipient_account = input("Enter recipient's IBAN number: ")
        if len(recipient_account) == 24:
            print(f"Successfully transferred ${transfer_amount} to {recipient_account}\n")
            user_balance -= transfer_amount
            never = f'Transferred ${transfer_amount} to {recipient_account}'
            update_transactions(never)
        else:
            print("The IBAN must have 24 digits, please try again\n")
    else:
        print("Insufficient funds for the transfer.\n")

def main():
    global yes
    global transactions

    time.sleep(0.75)
    print('''The code is 1996.
    Don't use caps.
    You can only see your previous 10 transactions''')

    time.sleep(1)
    print('Welcome to WillCodeIT bank\n')
    time.sleep(1)
    attempts = 3

    while attempts > 0:
        attempt = input('Please enter PIN: ')
        if attempt == user_pin:
            print('Correct PIN')
            time.sleep(1)
            break
        else:
            attempts -= 1
            print(f'Incorrect PIN. Attempts remaining: {attempts}')
            if attempts == 0:
                print('Too many incorrect attempts. Exiting...')
                sys.exit()

    yes = 0
    valid_option = True
    never = None

    while valid_option:
        time.sleep(0.75)
        menu = input('''
        Please select an option:

        Welcome to WillCodeIT banking.
        1. Display balance
        2. Withdraw funds
        3. Deposit funds
        4. Print list of transactions
        5. Change PIN
        6. Transfer funds
        9. Return card

        ---> : ''')

        print()

        if menu == "1":
            display_balance()
        elif menu == "2":
            withdraw_funds()
        elif menu == '3':
            deposit_funds()
        elif menu == '4':
            print_transactions()
        elif menu == "5":
            change_pin()
        elif menu == "6":
            transfer_funds()
        elif menu == "9":
            print("Thank you for using WillCodeIT banking:\n")
            sys.exit()
        else:
            print("Please choose a valid option\n")

if __name__ == "__main__":
    main()
