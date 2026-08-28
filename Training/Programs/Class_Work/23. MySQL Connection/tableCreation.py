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

    #running querry to create a table
    mycursor.execute("create table noobtable(id int, name varchar(25))")
    print("TABLE CREATED SUCCESSFULLY...")
except Exception as e:
    print(e)