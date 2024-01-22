# import mysql.connector

# def get_user_input():
#     print("Enter MySQL Database Credentials:")
#     # host = input("Host: ")  # Example: localhost
#     user = input("Username: ")  # Example: your_username
#     password = input("Password: ")  # Example: your_password
#     # database = input("Database: ")  # Example: inflation_records

#     return {
#         "host": "3306",
#         "user": user,
#         "password": password,
#         "database": "inflation_records"
#     }

# def connect_to_database():
#     db_config = get_user_input()
#     conn = mysql.connector.connect(**db_config)
#     return conn

# def create_tables():
#     try:
#         conn = connect_to_database()
#         cursor = conn.cursor()
        
#         # Your table creation logic goes here
        

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# if __name__ == "__main__":
#     create_tables()