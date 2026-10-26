#student={}
def sign_up():
    email=input("Enter your email:")
    name=input("Enter your name:")
    phone=input("Enter your number:")
    course=input("Enter a course:")
    password=input("Enter a password:")

    student={
        email:{"name":name,
        "email":email,
        "phone number":phone,
        "course":course,
        "password":password}
        
    }
    print("Registered Succesfully.")
    return student

def log_in():
    student=sign_up()
    email=input("Enter your email:")
    password=input("Enter your password:") 
    if email in student and password == student[email]["password"]:
        print("email:",student[email]["email"])
        print("Student Name:",student[email]["name"])
        print("Phone Number:",student[email]["phone number"])
        print("Course:",student[email]["course"])
        return "Login Succesfull",student
    print("Invalid email or password.")
    return None

# log_in()

def fee_structure():
    login = log_in()

    if login is None:
        print("Login Failed")
        return
    student, email = login

    # course = input("Enter your course name:")
    # if course == student[email]["BADS"]:
    fees={    
        "BADS":"For MBA on Businee Analytics & Data Analytics: 7.35L/-",
        "Finance":"For MBA on Finance: 7L/-",
        "Supply Chain":"For MBA on Supply Chain: 5L/-",
        "DM":"For MBA on Digital Marketing: 5.5L/-",
        "Marketing":"For MBA on Marketing: 6L/-",
        "HR":"For MBA on HR: 4L/-"
    }
    course = input("Enter your course name:").upper()
    if course in fees:
        print(fees[course])
    else:
        print("Sorry your course is not available")
fee_structure()






