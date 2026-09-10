import datetime

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# current_hour=datetime.datetime.now().second
# current_hour=datetime.datetime.now().minute
current_hour=datetime.datetime.now().hour
if current_hour < 12:
	greeting="Good morning!"
elif 12 <current_hour<4:
	greeting="Good afternoon!"
elif 4 <current_hour <8:
	greeting="Good evenig!"
else:
	greeting="Good night!"

print(greeting)

# Nested if

salary=45000
manager_post=True

if salary>=35000: 
	print("She gets some good amount!")
	if manager_post:
		print("Wow! she's super-senior to us")
	else:
		print("She's still pushing herself")
else: 
	print("She's doesn't get much amount")

# use of all() and any() function

numbers=[1,2,0,4,5,-6]
all_positive=all(num>0 for num in numbers )
has_even=any(num % 2==0 for num in numbers )
print(all_positive)
print(has_even)

#Password validation

# def validate_password():
# 	while True:
# 		password=input("Enter the Password:")
# 		if len(password)>=8:
# 			print("Password accepted!")
# 		    break
# 		else:
#             print("The password is short.Try again")
# validate_password()

def password_validate():
	while True:
		password=input("Enter the Password:")
		if len(password)>=8:
			print("Password Validated!")
			break
		else:
			print("Password too short.Try again!")
password_validate()

#For loop
for char in "Python":
	print(char)

# For-break loop
for i in range(1,11):
	print(i,end=" ")
	if i==5:
		print("Found 5! Breaking out of the loop.")
		break
print("Loop Ended")

#
for i in range(1,6):
	if i==3:
		print("Skipping 3.....")
		continue
	print()

def diff_names(name):
	# return f"{name} likes to ride horses, more than cars."
	 print(f"{name} likes to ride horses, more than cars.")
# print(diff_names("Anika"))
diff_names("Anika")

# Return function can be used to return the value from a function
def get_person_details():
	name="Anika"
	lover="Messi"
	boyfriend="Taemin"
	husband="Lee Minho"
	age=23
	return name,lover,boyfriend,husband,age
person_name, person_lover,person_bf,person_hubby,person_age=get_person_details()
print(f"{person_name} has {person_lover},{person_bf} and {person_hubby} at the age of {person_age}")




