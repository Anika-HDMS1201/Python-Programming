# weekly_sales = {"Mon": "5000", "Tue": "0", "Wed": "7500", "Thu": "", "Fri": "12000"}
# total_revenue = 0
# for i in weekly_sales:
#     if i == "":
#         x=i.replace("","0")
#     elif i!= "":
#         x=int(i)
# total_revenue+=i
# print(weekly_sales)
# print(total_revenue)

print("==================================")

weekly_sales = {
    "Mon": "5000",
    "Tue": "0",
    "Wed": "7500",
    "Thu": "",
    "Fri": "12000"
}
total_revenue = 0
for day in weekly_sales:

    if weekly_sales[day] == "":
        weekly_sales[day] = 0
    else:
        weekly_sales[day] = int(weekly_sales[day])
        total_revenue += weekly_sales[day]

print("Cleaned Dictionary:", weekly_sales)
print("Total Revenue:", total_revenue)


