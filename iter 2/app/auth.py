from database import connect_to_database

def login():
    conn = connect_to_database()
    cursor = conn.cursor()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT UserID FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_id = cursor.fetchone()

    conn.close()

    if user_id:
        print("Login successful!")
        return user_id[0]
    else:
        print("Login failed. Please check your credentials.")
        return None

def signup():
    conn = connect_to_database()
    cursor = conn.cursor()

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    cursor.execute("INSERT INTO Users (Username, Password) VALUES (%s, %s)", (username, password))
    conn.commit()

    # Retrieve the user ID after signup
    cursor.execute("SELECT UserID FROM Users WHERE Username = %s AND Password = %s", (username, password))
    user_id = cursor.fetchone()

    conn.close()

    if user_id:
        return user_id[0]
    else:
        print("Signup failed. Please try again.")
        return None