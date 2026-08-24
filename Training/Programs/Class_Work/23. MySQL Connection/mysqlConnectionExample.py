import mysql.connector as msql

try:
    #establishing connection with python
    mydb = msql.connect(
            host="localhost",
            user="root",
            password="root",
            database="anikadb"
        ) #this function is use to connect this program with mysqlDB
    #creating cursor for execution of any mysql querry
    mycursor = mydb.cursor() #next we will create a cursor which will be use to execute some querry
    #executing first querry to see all data inside the friends table
    mycursor.execute("select * from friends")
    #all data get's stored into mycursor so we are getting one by one data
    for i in mycursor:
        print(i)

    sql = "INSERT INTO friends(name, phone_number, address) VALUES (%s, %s, %s)"

    name = input("Enter your name : ")
    phone = int(input("Enter your phone : "))
    address = input("Enter your address : ")

    val = (name,phone,address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



except msql.errors.ProgrammingError as e:
    print("Your Table Name is not proper")
except Exception as e:
    print(f"Something went wrong {e}")