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

    #running querry to insert a value a table
    query = "insert into noobtable(id, name) values(%s, %s);" #always use table(columns) then use values() either sometimes get exceptions
    values = (1,'Anika Jana') #tuple
    mycursor.execute(query,values)
    values = (2,'Chittajit Chakraborty') #tuple
    mycursor.execute(query,values)
    mydb.commit()
    print("INSERTED DATA SUCCESSFULLY...")
except Exception as e:
    print(e)