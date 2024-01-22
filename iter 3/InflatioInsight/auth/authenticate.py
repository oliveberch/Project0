# auth/authenticate.py
from auth.login import login
from auth.signup import signup
from database.conn_db import connect_to_database

def auth_user(conn):
    user_choice = input("Do you want to login or sign up? Enter 'login' or 'signup': ")

    if user_choice.lower() == 'login':
        user_credentials = login(conn)
    elif user_choice.lower() == 'signup':
        user_credentials = signup(conn)
    else:
        print("Invalid choice. Please enter 'login' or 'signup'.")
        return None

    if user_credentials:
        print("User authentication successful!")
        return user_credentials
    else:
        print("User authentication failed.")
        return None