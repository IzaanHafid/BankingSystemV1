
'''
    Hey! This was my first ever project, created all the way back in 2022, I made
    this in honour of my brother who used to be really interested in computer science.
    
    He made a simple banking system with transaction logs using Python and mySQL,
    all of the accounts, transaction logs, and everything else would be logged
    in csv files.
    
    I was also extremely interested in Python at the time, so I followed in my brother's
    footsteps and made my own banking system, it's no way as great as my brother's,
    but it was the first project I ever properly made.
    
    To my brother, I love you <3
'''


acc_create = False
money = 0
print("Yes Bank")
while True:
    print("""1 = create an account
2 = access an account
3 = exit""")
    response = input("> ")
    if response == "1":
        if acc_create == False:
            print("Create an account name")
            acc_name_create = input("> ")
            print("Enter a 4 digit password")
            acc_password_create = (input("> "))
            if len(acc_password_create) == 4 and acc_password_create.isnumeric():
                print("Account Created!")
                acc_create = True
            else:
                print("Enter a 4 digit number!")

        elif acc_create == True:
            print("You already have an account!")
    elif response == "2":
        if acc_create == False:
            print("Create an Account first!")
        elif acc_create == True:
            print("Account Name:")
            acc_name_access = input("> ")
            if acc_name_access == acc_name_create:
                print("Account Password:")
                acc_password_access = input("> ")
                if acc_password_access == acc_password_create:
                    print(f"You have accessed {acc_name_create}")
                    print("""1 = deposit
2 = withdraw""")
                    response_access = int(input("> "))
                    if response_access == 1:
                        print("How much money do you want to deposit?")
                        money_deposit_access = int(input("> "))
                        money += money_deposit_access
                        print(f"Deposited {money_deposit_access}$ into {acc_name_create}, You now have {money}$ in {acc_name_create}")
                    elif response_access == 2:
                        if money > 0:
                            print(f"How much money do you want to withdraw? You have {money}$ in {acc_name_create}")
                            money_withdraw_access = int(input("> "))
                            if money_withdraw_access > money:
                                print("You cannot withdraw more then what is in your account!")
                            elif money_withdraw_access <= money:
                                money -= money_withdraw_access
                                print(f"Withdrawn {money_withdraw_access} from {acc_name_create}, You now have {money}$ in {acc_name_create}")
                        else:
                            print("You do not have any money in your bank account...")
                    else:
                        print("I don't understand...")
                else:
                    print("Password is not correct...")
            else:
                print("Account not found...")
    elif response == "3":
        print("Exiting Yes Bank...")
        break
    else:
        print("I don't understand...")
