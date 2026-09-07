from connection import SimpleDatabaseManager as noob
def verify_connection():
    try:
        db = noob() 
        mydb = db.get_connection()
        if mydb.is_connected():
            print("Success: Connection established perfectly!")
        mydb.close()
    except Exception as e:
        print(f"Failed to connect! Error details: {e}")
verify_connection()