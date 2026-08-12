# Basic Banking Structure.
# ------------------------
# A/C No.
# IFSC Code.
# Name :

# UPI ID = tatai47@upi

# 1/ Withdraw -  (*)
# 2/ Deposit (*)
# 3/ Transfer to another account - Required receiver account details. (*)
# 4/ Balance check (*)
# 5/ Card system - Credit / Debit ()
# 6/ Loan system ()

#Single user banking system
import random


AllCustomers = {}
customer = {
    "Name":"",
    "AccountNo":00,
    "Location":"",
    "IFSC":"",
    "Balance":0.0
}

def accountCreation():
    print("====================================")
    print("||Python Banking Account Creation||")
    print("====================================")
    CustomerName = input("Enter your name : ")
    AccountNo = random.random(10000000000, 99999999999)
    location = input("Enter your location : ")
    ifsc = str(location + str(AccountNo)) #auto generated value
    customer["Name"] = CustomerName
    customer["AccountNo"] = AccountNo
    customer["Location"] = location
    customer["IFSC"] = ifsc

    x = float(input("Enter Minimum Deposit amount for account creation (1000) : "))
    if x >= 1000:
        customer["Balance"] = x
    elif x<=0:
        print("Entered amount cannot be 0 or negative")
    else:
        print("Minimum Deposit amount is 1000")
    choice()


def deposit():
    print("====================================")
    print("||Python Banking Account Deposit||")
    print("====================================")
    Money = float(input("Enter your deposit amount : "))
    if Money >= 0:
        customer["Balance"] += Money #10
        print(f"========== {Money} Deposited Successfully ==========")
    else:
        print("Entered amount cannot be 0 or negative")

def withdraw():
    print("====================================")
    print("||Python Banking Account Withdraw||")
    print("====================================")
    Money = float(input("Enter your withdraw amount : "))
    if Money >= 0:
        customer["Balance"] -= Money #10
        print(f"========== {Money} Withdrawn Successfully ==========")
    else:
        print("Entered amount cannot be 0 or negative")

def balanceCheck():
    print(f"Current Balance : {customer["Balance"]}")

def showDetails():
    print("====================================")
    print("||Python Banking Account Details||")
    print("====================================")
    print(f"Name : {customer['Name']}")
    print(f"Account Number : {customer['AccountNo']}")
    print(f"Location : {customer['Location']}")
    print(f"IFSC Code : {customer['IFSC']}")
    balanceCheck()

def choice():
    x = """
Enter your choice : 
0/. Exit Banking System
1/. Show Customer Details
2/. Deposit Money
3/. Withdraw 
 -> """
    choose = int(input(x))
    if choose == 1 :
        showDetails()
    elif choose == 2:
        deposit()
    elif choose == 3:
        withdraw()
    elif choose == 0:
        return
    
    else :
        print("Entered wrong option ",choose)
    choice()   


def startUp():
    print("=======================================")
    print("|| Welcome to Python Banking System ||")
    print("=======================================")
    choose = int(input("Enter your choice : \n 1/. Create Account / Start Banking \n 2/. Exit \n -> "))
    if choose == 1 :
        accountCreation()
    elif choose == 2:
        print("Thank you for visiting our banking system")
        return
    else:
        print(f"Wrong operator entered {choose}")


startUp()