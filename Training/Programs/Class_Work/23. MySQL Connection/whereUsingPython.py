import mysql.connector as msql

try:
    mydb = msql.connect(
        host="localhost",
        user="root",
        password="root",
        database = "noob"
    )
    mycursor = mydb.cursor() 
    print("Connection stablished...")
    sqlStatement = "select * from anikadb.friends where name = 'Chittajit Chakraborty';"
    mycursor.execute(sqlStatement)

    #just try
    name = 'Chittajit Chakraborty'
    sqlStatement = f"select * from anikadb.friends where name = '{name}' ;"

    #printing direct mycursor
    print(type(mycursor))
    print(mycursor)

    #Using fetchall() 
    values = mycursor.fetchall()
    print(type(values))
    print(values)

    #Using direct mycursor but using for loop.
    for i in mycursor:
        print(i)

    #fetching and showing all data from DB
    mycursor.execute("SELECT * FROM anikadb.friends")
    for i in mycursor:
        print(i)

    #Using user input.
    name = input("Enter your name to search : ")
    sqlStatement = "select * from anikadb.friends where name = %s;"
    mycursor.execute(sqlStatement,(name,))
    result = mycursor.fetchall()
    print(result)
except Exception as e:
    print(e)