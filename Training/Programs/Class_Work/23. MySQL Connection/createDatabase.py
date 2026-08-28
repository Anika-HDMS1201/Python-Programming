import mysql.connector as msql

try:
    mydb = msql.connect(
        host="localhost",
        user="root",
        password="root",
    )
    mycursor = mydb.cursor() #cursor function use to execute your sql qurry with python
    print("Connection stablished...")

    #running querry to create a DB
    mycursor.execute("CREATE DATABASE noob")
    print("DATABASE CREATED SUCCESSFULLY...")
except Exception as e:
    print(e)