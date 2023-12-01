import time
import sys

user_balance = 100
user_pin = '1996'

trans1 = 'NA'
trans2 = 'NA'
trans3 = 'NA'
trans4 = 'NA'
trans5 = 'NA'
trans6 = 'NA'
trans7 = 'NA'
trans8 = 'NA'
trans9 = 'NA'
trans10 = 'NA'

time.sleep(0.75)

print('''The code is 1996. 
Don't use caps.
You can only see your previous 10 transactions''')

time.sleep(1)

print('Welcome to WillCodeIT bank')
print()
time.sleep(1)
attempts = 3

while attempts > 0:
    attempt1 = input('Please enter PIN: ')
    if attempt1 == user_pin:
        print('Correct PIN')
        time.sleep(1)
        break
    else:
        print('Incorrect PIN. Attempts remaining:', attempts - 1)
        attempts -= 1
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
        print("Display Balance")
        print('$', user_balance)
        print()
        time.sleep(0.25)
    elif menu == "2":
        print("Withdraw Funds")
        time.sleep(0.75)
        wf = int(input('''
        How much would you like to withdraw?
        Your options are:
        10:
        20:
        50:
        100:
        7 - Other(Must be a multiple of 10)
        8 - Return to main menu:
        9 - Return card:

        --->: '''))
        #this is another menu/question thing for the withdraw funds(wf) menu
        if wf == user_balance:
            #checks if the amount you wanted to withdraw was the same amount as the money in your bank account
            print("Congratulations you broke, you now have $0 in your bank account")
            user_balance = 0
            #because they withdraw the same amount that they have, the value will be 0
            never = 'Withdrew', wf
            #made variable called never to display i.e. 'Withdrew 50'

        elif wf > user_balance:
            print("you don't have that much money")
            never = 0
            #we need this variable for later in the code
            yes = yes - 1
            #this was added because the way the print transaction work is that check what the value is

        elif wf ==10:
            print("Succesfully withdrawn $10, so you now have", user_balance - 10)
            #here it says how much you withdrew and your current balance
            user_balance = user_balance - wf
            #it sets the user balance to the correct number after the withdrawal
            never = 'Withdrew', wf

        elif wf ==20:
            print("Succesfully withdrawn $20, so you now have", user_balance - 20)
            user_balance = user_balance - wf
            never = 'Withdrew', wf

        elif wf ==50:
            print("Succesfully withdrawn $50, so you now have", user_balance - 50)
            user_balance = user_balance - wf
            never = 'Withdrew', wf

        elif wf ==100:
            print("Succesfully withdrawn $100, so you now have", user_balance - 100)
            user_balance = user_balance - wf
            never = 'Withdrew', wf

        elif wf == 7:
            print("Other amount")
            ea = int(input("How much would you like to withdraw?: "))
            #for the custom amount they want to withdraw

            if ea == user_balance:
                #checks if the amount you wanted to withdraw was the same amount as the money in your bank account
                print("Congratulations you broke, you now have $0 in your bank account")
                user_balance = 0
                #because they withdraw the same amount that they have, the value will be 0
                never = 'Withdrew', ea
                #made variable called never to display i.e. 'Withdrew 50'
            elif ea > user_balance:
                print("you don't have that much money")
                never = never
                #we need this variable for later in the code
                yes = yes - 1
                #this was added because the way the print transaction work is that check what the value is
            elif ea % 10 == 0:
                #to make sure the value they enter is a multiple of 10
                print("Succesfully withdrawn $", ea, " you now have $", user_balance - ea)
                user_balance = user_balance - ea
                never = 'Withdrew', ea
            else:
                print("Invalid")
                print("Make sure it is a multiple of 10 and numbers only")
                never = never
                yes = yes - 1


        elif wf == 8:
            print()
            never = never
            yes = yes - 1

        elif wf == 9:
            print("Thank you for Banking at WillCodeIT Bank")
            sys.exit()

        else:  
            print("Invalid")
            yes = yes - 1

        yes = yes + 1
        #after the user withdraws their money, the code adds 1 to the value of yest because if it doesn't then the value of...???
        if yes > 10:
        #at the start of the code I said that you would only be able to see that last 10 transactions
        #the way the code works is that if yes = 1 then never will go to trans1 
        #when the number of transactions you have done passes 10, then all the information gets passed on as shown
            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never
        # as you can see trans1 information is lost and the new on is there
        elif yes == 1:
            trans1 = never
            # if yes = 1 then this is where the information is stored and same for the rest

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            trans3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

     
    elif menu == '3':
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
                print("Successfully Deposited", dp, "you now have $", user_balance + dp)
                user_balance = user_balance + dp
            else:
                print("You cannot deposit negative amounts")
        elif EA == 2:
            print()
        elif EA == 9:
            print("Thank you for Banking at WillCodeIT Bank")
            sys.exit()
        else:
            print("Invalid option")


    elif menu == '4':
        print("Print list of transactions:")
        time.sleep(0.75)
        print()
        print(trans1)
        print(trans2)
        print(trans3)
        print(trans4)
        print(trans5)
        print(trans6)
        print(trans7)
        print(trans8)
        print(trans9)
        print(trans10)

    elif menu == "5":
        print("Change PIN")
        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            user_pin = new_pin
            print(f"PIN successfully changed to {new_pin}")
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    elif menu == "6":
        print("Transfer Funds")
        transfer_amount = int(input("Enter the amount to transfer: "))
        if transfer_amount <= user_balance:
            recipient_account = input("Enter recipient's IBAN number: ")
            if len(recipient_account) == 24:
                print(f"Successfully transferred ${transfer_amount} to {recipient_account}")
                user_balance -= transfer_amount
            else:
                print("The IBAN must have 24 digits, please try again")
        else:
            print("Insufficient funds for the transfer.")

    elif menu == "9":
        print("Thank you for using WillCodeIT banking:")
        sys.exit()

    else:
        print("Please choose a valid option")



    
