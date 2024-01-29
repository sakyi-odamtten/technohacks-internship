import random
import os
def atm():
    #the account balance is generatored with random
    amount = random.randrange(10, 1000000)
    #the user pin must be five numbers in total
    pin = input("Enter pin:")
    if len(pin) != 5:
        pin = input("The pin must be five digit. Try again")
    user = input('Enter user name:')

    while True:
        print("The following are the actions you can perform:\n 1. To Check balance press b\n 2.To Deposit press d\n 3.To Withdraw press w\n 4.To Quit press q\n")
        action = input('Enter action here: \n')

        if action == 'b':
            print(f"{user} current balance is {amount} Cedis\n")
        elif action == 'd':
            depo = int(input('Enter amount you want to deposit:'))
            amount =  amount + depo
            print(f"{user} current balance is {amount} Cedis \n")
        elif action == 'w':
            withdraw = int(input('Enter amount you want to withdraw:'))
            if withdraw > amount: withdraw =  int(input('Your balance is insufficient . Enter amount again:'))
            amount = amount - withdraw
            print(f'{user} have made a cash out of {withdraw} Cedis\n Your current balance is {amount} Cedis \n')
        elif action == 'q':
            exit()
        else:
            action = input('Your option can not be performed please try again:')

atm()