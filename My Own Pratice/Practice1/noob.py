import mysql.connector as msql
import datetime
# try:
#     mydb = msql.connect(
#             host="localhost", 
#             user="root",
#             password="root", 
#             database="bads_placement_backup_demo" 
#         ) 
#     mycursor = mydb.cursor() 
#     mycursor.execute("select * from students")
#     for i in mycursor:
#         print(i)

#     sql = "INSERT INTO students(student_id, student_name,gender,cgpa,python_score,sql_score,internship_months,preferred_role,city,registration_date) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)"

#     student_id = input(int("Enter the stuident Id : "))
#     student_name = input("Enter the student name: ")
#     gender = input("Enter your gender : ")
#     cgpa = input(int("Enter your cgpa : "))
#     python_score = input(int("Enter your python score : "))
#     sql_score = input(int("Enter your sql score : "))
#     internship_months = input(int("Enter the internship months : "))
#     preferred_role = input("Enter your preferred role : ")
#     city = input("Enter your city : ")
#     registration_date = input("Enter the registration date : ")

#     val = (student_id,student_name,gender,cgpa,python_score,sql_score,internship_months,preferred_role,city,registration_date)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")

# except msql.errors.ProgrammingError as e:
#     print("Your Table Name is not proper problem ",e)
# except Exception as e:
#     print(f"Something went wrong {e}")


#     # # Mulltiple time inputs.
#     # sql = "INSERT INTO friends(name, phone_number, address) VALUES (%s, %s, %s)"
#     # x = int(input("How many data do you want to put together?"))
#     # if x >= 1 :
#     #     for i in range(x):
#     #         name = input(f"{i+1}. Enter your name : ")
#     #         phone = int(input(f"{i+1}. Enter your phone : "))
#     #         address = input(f"{i+1}. Enter your address : ")
#     #         val = (name,phone,address)
#     #         mycursor.execute(sql, val)
#     #     mydb.commit()
#     #     print(mycursor.rowcount, "record inserted.")
#     # else:
#     #     print("Sorry wrong value choosen.")
        


# except msql.errors.ProgrammingError as e:
#     print("Your Table Name is not proper")
# except Exception as e:
#     print(f"Something went wrong {e}")



def tryByChittajit():
    try:
        mydb = msql.connect(
                    host="localhost", 
                    user="root",
                    password="root", 
                    database="bads_placement_backup_demo" 
                ) 
        mycursor = mydb.cursor() 


        statement = "select * from students"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        sql = "INSERT INTO students(student_id, student_name,gender,cgpa,python_score,sql_score,internship_months,preferred_role,city,registration_date) VALUES ( %s, %s,%s,%s,%s,%s,%s,%s,%s, %s)"
        print(f"Stuident Id {100+len(data)+1} ")
        student_name = input("Enter the student name: ")
        gender = input("Enter your gender : ")
        cgpa = float(input("Enter your cgpa : "))
        python_score = int(input("Enter your python score : "))
        sql_score = int(input("Enter your sql score : "))
        internship_months = int(input("Enter the internship months : "))
        preferred_role = input("Enter your preferred role : ")
        city = input("Enter your city : ")
        year = int(input("Enter the registration year : "))
        month = int(input("Enter the registration month : "))
        day = int(input("Enter the registration day : "))
        registration_date = datetime.date(year,month,day)

        val = (100+len(data)+1,student_name,gender,cgpa,python_score,sql_score,internship_months,preferred_role,city,registration_date)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

        
    except Exception as e:
        print(e)


tryByChittajit()