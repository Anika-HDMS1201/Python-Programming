import mysql.connector as msql

try:
    #establishing connection with python
    mydb = msql.connect(
            host="localhost", #host name
            user="root", #user name
            password="root", #password
            database="anikadb" #database name
        ) #this function is use to connect this program with mysqlDB
    #creating cursor for execution of any mysql querry
    mycursor = mydb.cursor() #next we will create a cursor which will be use to execute some querry
    #executing first querry to see all data inside the friends table
    mycursor.execute("select * from friends")
    #all data get's stored into mycursor so we are getting one by one data
    for i in mycursor:
        print(i)

    sql = "INSERT INTO friends(name, phone_number, address) VALUES (%s, %s, %s)"
    # sql = "INSERT INTO friends VALUES (%s, %s, %s)"


    name = input("Enter your name : ")
    phone = int(input("Enter your phone : "))
    address = input("Enter your address : ")

    val = (name,phone,address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


    # Mulltiple time inputs.
    sql = "INSERT INTO friends(name, phone_number, address) VALUES (%s, %s, %s)"
    x = int(input("How many data do you want to put together?"))
    if x >= 1 :
        for i in range(x):
            name = input(f"{i+1}. Enter your name : ")
            phone = int(input(f"{i+1}. Enter your phone : "))
            address = input(f"{i+1}. Enter your address : ")
            val = (name,phone,address)
            mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Sorry wrong value choosen.")
        


except msql.errors.ProgrammingError as e:
    print("Your Table Name is not proper")
except Exception as e:
    print(f"Something went wrong {e}")