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

    sql = "DELETE FROM anikadb.friends WHERE name = 'Hexagon Chottopadhyi'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

    #By user input
    sql = "DELETE FROM anikadb.friends WHERE name = %s"
    name = input("Enter name to delete : ")
    mycursor.execute(sql,(name,))
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
except Exception as e:
    print(e)