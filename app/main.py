import sys

from auth import login, signup
from analysis import perform_analysis
from database import create_tables

def main():
    print("Welcome to the Inflation Analysis App!")

    # Create tables in the database
    create_tables()

    while True:
        print("\nOptions:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        match choice:
            case "1":
                user_id = login()
                if user_id:
                    country_code = input("Enter the country code for analysis: ")
                    start_year = int(input("Enter the start year: "))
                    end_year = int(input("Enter the end year: "))
                    perform_analysis(user_id, country_code, start_year, end_year)

            case "2":
                user_id = signup()
                if user_id:
                    print("Signup successful! You are now logged in.")
                    # Additional logic if needed after signup

            case "3":
                print("Exiting. Thank you for using the Inflation Analysis App!")
                sys.exit()

            case _:
                print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()