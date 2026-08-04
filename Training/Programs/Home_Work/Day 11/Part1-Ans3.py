#enter_age=input("Enter the age:")
# age=int(enter_age)
def check_eligibility(age):
    return("Eligible to Vote")if age>=18 else("Minor")
enter_age=input("Enter the age:")
age=int(enter_age)
print(check_eligibility(age))




