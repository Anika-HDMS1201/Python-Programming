import mysql.connector as msql

try:
    mydb = msql.connect(
        host="localhost",
        user="root",
        password="root",
        database = "anikadb"
    )

    #Sorting name alphabatically ascending 
    mycursor = mydb.cursor() 
    print("Connection stablished...")
    sqlStatement = "select * from anikadb.friends order by name;"
    mycursor.execute(sqlStatement)
    for i in mycursor:
        print(i)

    print("\n\n\n=============================================\n\n\n\n")

    #Sorting name alphabatically descending 
    sqlStatement = "select * from anikadb.friends order by name desc;"
    mycursor.execute(sqlStatement)
    for i in mycursor:
        print(i)
except Exception as e:
    print(e)