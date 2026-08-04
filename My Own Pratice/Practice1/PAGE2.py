#Q1
marks = [85, 42, 91, 67, 38]
passed= 0
for i in marks:
     if i >= 40:
        print("Pass")
        passed+=1
else:
    print("Fail")
print(f"the total number of passed students:{passed}")

#Q2
numbers = [12, 15, 8, 21, 30, 7]
even_numbers=0
for i in numbers:
    if i%2==0:
        print("Even Number")
        even_numbers+=1
    else:
        print("Odd Number")
print(f"total even numbers: {even_numbers}")

#Q3
temps = (32, 35, 34, 37, 33) #Doubt
highest = temps[0]
lowest = temps[0]
total = 0
for i in temps:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / len(temps)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print("Average Temperature:", average)

#Q5
students = {"Anika", "Rahul", "Priya", "Anika", "Rahul"}
for i in students:
    print(i)
print(len(students))

#Q14
numbers = [12, 5, 18, 7, 25, 10, 3, 20]
even_count = 0
odd_count = 0
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        if i > largest:
            largest = i
    if i < smallest:
        smallest = i
    total += i
average = total / len(numbers)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum:", total)
print("Average:", average)

#Q7
marks = {
    "Math": 80,
    "Python": 90,
    "SQL": 70
}
total_marks= 0
each_subject= marks.keys()
each_marks=marks.values()
print(each_subject)
print(each_marks)
for i in marks.values():
    total_marks+=i
print(f"Total_marks:{total_marks}")
average= total_marks/len(marks.values())
print(f"Average marks:{average}")

#Q8
inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10
}
total_quantity=0
all_items=inventory.items()
print(all_items)
for i in inventory.values():
    total_quantity+=1
print(f"Total quantity:{total_quantity}")

#Q9
n=50
while n>1:      #(while n>=5:, while n>4:)
    if n%5==0:
        print(n)
    n-=1
else:
    print("Not Divisible by 5")










    



 






    

 


 









    
       

