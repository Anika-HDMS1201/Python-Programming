#Q15
employees = {
    "Anika": {
        "salary": 50000,
          "experience": 3
          },
    "Rahul": {
        "salary": 65000,
          "experience": 5
          },
    "Priya": {
        "salary": 45000,
          "experience": 2
          }
}
total_salary= 0
highest_salary=0
highest_employee=" "

for x,y in employees.items():
    salary=y["salary"]
    experience=y["experience"]
    print("Employees:", x)
    print("Salary:",salary)
    print("Experience:",experience)
    
    if experience>=5:
        Bonus= salary* (10/100)
    elif experience >=3:
        Bonus= salary* (5/100)
    else:
        print("No Bonus otherwise")

total_salary+=salary
print(f"Total salary:{total_salary}")  

if salary>highest_salary:
    highest_salary=salary
    highest_employee=y

print(f"Total salary expense:{salary}")
print(f"Highest paid employee:{y}")
print(f"Highest salary:{highest_salary}")

print("======================")

#Q11

students = {
    "Anika": [80, 90, 85],
    "Rahul": [70, 75, 80],
    "Priya": [90, 95, 88]
}
for name,marks in students.items():
    total=sum(marks)
    average=total/len(marks)
    if average>= 85:
        print("Excellent")
    elif average>=70:
        print("Good")
    else:
        print("Needs Improvement")

print(f"Total marks of students: {total}")
print(f"Average: {average}")

print("==========================")

products = [
    ("Laptop", 50000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]
inventory_value= 0
count=0
for product in products:
    product_names=product[0]
    product_price=product[1]
    print(f"Products name:{product_names}")
    print(f"Products price:{product_price}")

    if product_price >5000:
        count+=1

    inventory_value+=product_price

print(f"Total inventory value:{inventory_value}")
print(f"Count:{count}")

print("============================")

numbers = [12, 5, 18, 7, 25, 10, 3, 20]
even_numbers=0
odd_numbers=0
total_sum=0
for i in numbers:
    if i %2==0:
        even_numbers+=1
    elif i % 2!=0:
        odd_numbers+=1
total_sum=sum(numbers)
average=total_sum/len(numbers)
largest_number=max(numbers)
smallest_number=min(numbers)

print(f"The even numbers are: {even_numbers}")
print(f"The odd numbers are: {odd_numbers}")
print(f"The largest number: {largest_number}")
print(f"The smallest number: {smallest_number}")
print(f"The sum is: {total_sum}")
print(f"The average is: {average}")

print("============================")  



