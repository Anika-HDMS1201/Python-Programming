import mysql.connector as msql

class SimpleDatabaseManager:
    
    # 1. The Connection Function
    def get_connection(self):
        # Connects to MySQL and returns the connection object
        mydb = msql.connect(
            host="localhost",
            user="root",
            password="root",
            database="anikadb" 
        )
        return mydb

    # 2. Function to Create Table
    def create_table(self):
        mydb = self.get_connection()
        mycursor = mydb.cursor()
        
        # Creates the table if it doesn't already exist
        mycursor.execute("CREATE TABLE IF NOT EXISTS simple_table (id INT, name VARCHAR(25))")
        print("1. Table 'simple_table' created successfully.")
        
        mydb.close()

    # 3. Function to Insert Table Values
    def insert_value(self, user_id, user_name):
        mydb = self.get_connection()
        mycursor = mydb.cursor()
        
        # Inserts data using %s to prevent SQL injection
        sql = "INSERT INTO simple_table (id, name) VALUES (%s, %s)"
        val = (user_id, user_name)
        mycursor.execute(sql, val)
        mydb.commit() # Required to save the insert
        
        print(f"2. Value inserted: {user_name}")
        mydb.close()

    # 4. Function to Show Table Values
    def show_values(self):
        mydb = self.get_connection()
        mycursor = mydb.cursor()
        
        # Fetches and prints all rows
        mycursor.execute("SELECT * FROM simple_table")
        result = mycursor.fetchall()
        
        print("\n--- Current Table Data ---")
        for row in result:
            print(row)
        print("--------------------------\n")
        
        mydb.close()

    # 5. Function to Delete Table Values (Rows)
    def delete_value(self, user_name):
        mydb = self.get_connection()
        mycursor = mydb.cursor()
        
        # Deletes a specific row based on the name
        sql = "DELETE FROM simple_table WHERE name = %s"
        val = (user_name,) 
        mycursor.execute(sql, val)
        mydb.commit() # Required to save the deletion
        
        print(f"3. Value deleted: {user_name}")
        mydb.close()

    # 6. Function to Delete the Entire Table
    def delete_table(self):
        mydb = self.get_connection()
        mycursor = mydb.cursor()
        
        # Drops the table completely
        mycursor.execute("DROP TABLE IF EXISTS simple_table")
        print("4. Table 'simple_table' deleted successfully.")
        
        mydb.close()


# --- Program Execution ---
if __name__ == "__main__":
    # Create the class object
    db = SimpleDatabaseManager()

    # Run the operations in order
    db.create_table()
    
    db.insert_value(101, "Aritra")
    db.insert_value(102, "Sneha")
    
    db.show_values()
    
    db.delete_value("Aritra")
    
    db.show_values()
    
    db.delete_table()