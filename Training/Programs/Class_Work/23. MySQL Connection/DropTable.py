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

    sql = "DROP TABLE anikadb.friends"
    sql = "DROP TABLE IF EXISTS anikadb.friends"
    mycursor.execute(sql)
except Exception as e:
    print(e)