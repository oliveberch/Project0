import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="Archit",
            user=input("Enter DB username: "),
            password=input("Enter DB password: "),
            database="inflation_records"
        
        )
        return conn
        # cursor = conn.cursor()
        # return cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None