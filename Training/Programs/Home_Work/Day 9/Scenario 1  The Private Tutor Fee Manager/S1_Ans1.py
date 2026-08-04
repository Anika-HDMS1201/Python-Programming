# students = ["Aritra", "Sneha", "Rohan", "Priya"]
# amount_paid = [1500, 0, 1500, 500]
# monthly_fee = 1500
# #Added_data= students[i]+ amount_paid[i]
# noob = 0
# for i in amount_paid:
#     noob+=i
# print(noob)

students = ["Aritra", "Sneha", "Rohan", "Priya"]
amount_paid = [1500, 0, 1500, 500]
monthly_fee = 1500

fee_status={}
for i in range(len(students)):
    if amount_paid[i] == monthly_fee:
        fee_status[students[i]] = "Clear"
    elif amount_paid[i] == 0:
        fee_status[students[i]] = "Defaulter"
    else:
        fee_status[students[i]] = ("Partial Payment")

print(f"Final Fee Status:{fee_status}")

#very slight help from chatgpt.



