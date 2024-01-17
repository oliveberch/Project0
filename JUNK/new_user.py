import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="inflation_records"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Sample user data (replace with actual user data)
user_id = 1
user_pass = "your_password"

# Insert a new user into the Users table
insert_user_query = "INSERT INTO Users (UserID, PASS) VALUES (%s, %s)"
user_data = (user_id, user_pass)

try:
    cursor.execute(insert_user_query, user_data)
    conn.commit()
    print("User registered successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.rollback()

# Close the cursor and connection
cursor.close()
conn.close()
