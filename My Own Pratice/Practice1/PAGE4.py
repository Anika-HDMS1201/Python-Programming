#Q1
#attendance = [1, 0, 1, 1, 0, 1, 1]
#Write a program to:
#Count the number of days present (1).
#Count the number of days absent (0).
#Calculate attendance percentage.
#Print "Eligible" if attendance ≥ 75%, otherwise "Not Eligible".


attendance = [1, 0, 1, 1, 0, 1, 1]
numbers_present=0
numbers_absent=0
for i in attendance:
    if i==1:
        numbers_present+=1
    elif i==0:
        numbers_absent+=1
attendance_percentage= (numbers_present/len(attendance))*100
if attendance_percentage>=75:
    print("Eligible")
else:
    print("Not Elligible")

print(f"Total no of students present:{numbers_present}")
print(f"Total no of students absent: {numbers_absent}")
print(f"Attendence percentage: {attendance_percentage:.2f}%")

print("==========================")

#Q2
"""prices = (450, 1200, 750, 3000, 1800)
Using a loop:

Count products costing more than ₹1000.
Find the most expensive product price.
Find the cheapest product price.
Calculate the average price."""

prices = (450, 1200, 750, 3000, 1800)
count=0
most_expensive_product=0
cheapest_product=0
total=0

for i in prices:
    total+=i

    if i >1000:
        count+=1
        
    if i>most_expensive_product:
        most_expensive_product= i
    elif i<cheapest_product:
        cheapest_product= i

average_price=total/len(prices)

print(f"Total count product: {count}")
print(f"the most expensive product price: {most_expensive_product}")
print(f"the cheapest product price: {cheapest_product}")

print("==========================")

#Q3
"""marks = {
    "Math": 85,
    "Python": 72,
    "SQL": 95,
    "Excel": 68
}

Write a program to:

Print each subject and mark.
Count subjects with marks ≥ 80.
Find the highest-scoring subject.
Calculate the average mark."""

marks = {
    "Math": 85,
    "Python": 72,
    "SQL": 95,
    "Excel": 68
}
highest_scoring=0
count=0
average=0
for i,j in marks.items():
    print(f"{i} : {j}")
    count+=(j>=80) #True is considered as 1.
    #if j>highest_scoring:highest_scoring=j
    highest_scoring= max(highest_scoring,j)
    average+=j/len(marks)
print(f"Average marks: {average}")
print(f"the highest-scoring subject: {highest_scoring}")

print("==============================")

"""numbers = [11, 22, 33, 44, 55, 66]
Write a program to:

Calculate the sum of all even numbers.
Calculate the sum of all odd numbers.
Print which sum is larger."""

numbers = [11, 22, 33, 44, 55, 66]
even_numbers=0
odd_numbers=0

for i in numbers:
    if i%2==0:
        even_numbers+=i
    else:
        odd_numbers+=i

print(f"the sum of all even numbers: {even_numbers}")
print(f"the sum of all odd numbers: {odd_numbers}")

if even_numbers>odd_numbers:
    print("Even sum is larger")
elif odd_numbers>even_numbers:
    print("Odd sum is larger")
else:
    ("Both sums are equal")

print("================================")

"""employees = {
    "Anika": 50000,
    "Rahul": 70000,
    "Priya": 45000,
    "Riya": 80000
}
Write a program to:

Give a 10% bonus if salary > 60000.
Otherwise give a 5% bonus.
Print each employee's bonus.
Calculate total bonus expense."""

employees = {
    "Anika": 50000,
    "Rahul": 70000,
    "Priya": 45000,
    "Riya": 80000
}
total_bonus=0
bonus=0

for i in employees.items():
    employee=i[0]
    salary=i[1]
       
    if salary >60000:
        employee_bonus=salary*10/100
    else:
        employee_bonus=salary*5/100

    print(f"{employee}:{employee_bonus}")

total_bonus= salary+bonus
print(f"total bonus expense: {total_bonus}")
















