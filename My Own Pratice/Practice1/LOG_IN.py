users={}
def sign_up():
    email=input("Enter your Email: ")
    name=input("Enter your Name: ")
    phone=input("Enter your Number:")

    users[email]={
        "name":name,
        "phone":phone
    }
    print("Sign up successfull")
# sign_up()

def show_users():
    email=input("Enter your email:")

    if email in users:
        print("Email:",email)
        print("Name :",users[email]["name"])
        print("Phone :",users[email]["phone"])
    else:
        print("User not found")
while True:
    sign_up()
    show_users()
    x=int(input("Enter O to exit:"))
    if x==0:
        exit()
# # def show_info():
# #     student=sign_up()
# #     email=input("Enter your email:")
# #     entered_password=input("Enter your password:") 

#     if email in student:
#         if entered_password==student[email]["password"]:
#             print("Student Name:",student[email]["name"])
#             print("Phone Number:",student[email]["phone number"])
#             print("Course:",student[email]["course"])
#         else:
#             print("Wrong password!")
#     else:
#         print("Email not registered!")

    