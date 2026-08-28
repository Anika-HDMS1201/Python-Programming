import mysql.connector as msql

try:
    mydb = msql.connect(
        host="localhost",
        user="root",
        password="root",
        database = 'noob'
    )
    mycursor = mydb.cursor() 
    print("Connection stablished...")

    #running querry to show all data of a table
    mycursor.execute('SELECT * FROM noobtable;')
    result = mycursor.fetchall() #use fetchall() function to get data
    print(type(result)) #printing the type of result variable
    print(f"{len(result)} DATA FETCHED SUCCESSFULLY...")
    for i in result:
        print(i)
except Exception as e:
    print(e)