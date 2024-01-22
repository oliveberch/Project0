from database.conn_db import connect_to_database

def signup(conn):

    username = input("Create your username: ")
    password = input("Create your password: ")

    #Check for unique ness of user id, this might be problem later

    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (Username, Password) VALUES (%s, %s)", (username, password))
    conn.commit()

    cursor.execute("SELECT UserID FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_id = cursor.fetchone()


    if user_id:
        print("Signup successful!")
        return {"user": username, "password": password}
    else:
        print("Signup failed. Please try again.")
        return None
