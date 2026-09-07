import mysql.connector as msql

try:
    mydb = msql.connect(
        host="localhost",
        user="root",
        password="root",
        database = "anikadb"
    )
    mycursor = mydb.cursor() 
    print("Connection stablished...")
    sql = "UPDATE anikadb.friends SET address = 'New address' WHERE name = 'chittajit chakraborty'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Using user input
    sql = "UPDATE anikadb.friends SET address = %s WHERE name = %s"
    address = input("Enter your new addess : ")
    name = input("Enter your name to find:")
    mycursor.execute(sql,(address,name))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
except Exception as e:
    print(e)