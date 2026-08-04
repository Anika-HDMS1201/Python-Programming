roll = [101, 102, 103]
names = ["Amit", "Sneha", "Rohit"]
student_db = {}
for i in range(len(roll)):
    student_db[roll[i]] = names[i]
    print(student_db)