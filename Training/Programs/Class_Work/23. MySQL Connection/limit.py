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
    sql = "SELECT * FROM anikadb.friends LIMIT 5"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    for i in mycursor:
        print(i)


    # Using user input
    sql = "SELECT * FROM anikadb.friends LIMIT %s"
    number = int(input("Enter your number to show table data: "))
    mycursor.execute(sql,(number,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    for i in mycursor:
        print(i)


    number = int(input("Enter your number to show table data: "))
    sql = f"SELECT * FROM anikadb.friends LIMIT {number}"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    for i in mycursor:
        print(i)    
except Exception as e:
    print(e)