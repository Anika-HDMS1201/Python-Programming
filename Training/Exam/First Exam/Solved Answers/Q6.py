metrics = {
    "Total_Deposits": 0, 
    "Total_Withdrawals": 0
    }
bank_balance = 0
transactions = [ #as sample data not present in QP
    "Deposit-5000",
    "Deposit-10000",
    "Deposit-15000",
    "Deposit-20000",
    "Withdraw-4000"
    ]
for i in transactions:
    items = i.split("-")
    action = items[0] #Deposit / Withdrawals
    amount = int(items[1]) #stores number
    if action == "Deposit":
        bank_balance+=amount
        metrics["Total_Deposits"]+= amount
    elif action == "Withdraw":
        bank_balance-=amount
        metrics["Total_Withdrawals"]+= amount
print(f"Bank Balance : ${bank_balance}")
print(f"Metrics : {metrics}")