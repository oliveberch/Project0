from database.conn_db import connect_to_database

def login(conn):

    username = input("Enter your username: ")
    password = input("Enter your password: ")


    cursor = conn.cursor()

    cursor.execute("SELECT UserID FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_id = cursor.fetchone()

    if user_id:
        print("Login successful!")
        return {"user": username, "password": password}
    else:
        print("Login failed. Please check your credentials.")
        return None
    
