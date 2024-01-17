import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from getpass import getpass

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'getmecoffee',
    'database': 'sample'
}

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(**db_config)

# Function for user authentication
def authenticate_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Assuming you have a Users table with columns 'username' and 'password'
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()

    return user

# Function to create tables in the database
def create_tables():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Create a table named "InflationMetrics"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS InflationMetrics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            country VARCHAR(255),
            development_status VARCHAR(255),
            year INT,
            inflation FLOAT
        )
    ''')

    conn.commit()
    conn.close()

# CRUD Operations
def add_inflation_metric(country, development_status, year, inflation):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO InflationMetrics (country, development_status, year, inflation) VALUES (%s, %s, %s, %s)",
                   (country, development_status, year, inflation))
    conn.commit()
    conn.close()

def retrieve_inflation_metrics(filters=None):
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM InflationMetrics"
    params = []

    if filters:
        query += " WHERE "
        for key, value in filters.items():
            query += f"{key} = %s AND "
            params.append(value)
        query = query[:-4]

    cursor.execute(query, tuple(params))
    metrics = cursor.fetchall()

    conn.close()
    return metrics

def update_inflation_metric(metric_id, new_values):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "UPDATE InflationMetrics SET "
    for key, value in new_values.items():
        query += f"{key} = %s, "
    query = query[:-2] + " WHERE id = %s"
    params = list(new_values.values()) + [metric_id]
    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()

def delete_inflation_metric(metric_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM InflationMetrics WHERE id = %s", (metric_id,))
    conn.commit()
    conn.close()

# Data Aggregation
def collect_data_from_sources():
    # Implement data collection from economic agencies, open data platforms, and government publications
    # For simplicity, you can use a placeholder or external APIs for real implementation
    pass

# CLI Interaction
def user_options():
    print("\nOptions:")
    print("1. Add Inflation Metric")
    print("2. Retrieve Inflation Metrics")
    print("3. Update Inflation Metric")
    print("4. Delete Inflation Metric")
    print("5. Collect Data from Sources")
    print("6. Exit")

def get_user_choice():
    return input("Enter your choice (1-6): ")

def main():
    print("Welcome to the Inflation Analysis Application!")

    # User Authentication
    user = authenticate_user()
    if not user:
        print("Authentication failed. Exiting.")
        return

    # Create Tables
    create_tables()

    while True:
        user_options()
        choice = get_user_choice()

        match choice:
            case "1":
                # Add Inflation Metric
                country = input("Enter country: ")
                development_status = input("Enter development status: ")
                year = int(input("Enter year: "))
                inflation = float(input("Enter inflation: "))
                add_inflation_metric(country, development_status, year, inflation)
                print("Inflation metric added successfully.")

            case "2":
                # Retrieve Inflation Metrics
                filters = {
                    'country': input("Enter country (press Enter to skip): "),
                    'development_status': input("Enter development status (press Enter to skip): "),
                    'year': int(input("Enter year (press Enter to skip): ")) or None
                }
                metrics = retrieve_inflation_metrics(filters)
                print("Retrieved Inflation Metrics:")
                print(pd.DataFrame(metrics))

            case "3":
                # Update Inflation Metric
                metric_id = int(input("Enter the ID of the metric to update: "))
                new_values = {
                    'country': input("Enter new country (press Enter to skip): "),
                    'development_status': input("Enter new development status (press Enter to skip): "),
                    'year': int(input("Enter new year (press Enter to skip): ")) or None,
                    'inflation': float(input("Enter new inflation (press Enter to skip): ")) or None
                }
                update_inflation_metric(metric_id, new_values)
                print("Inflation metric updated successfully.")

            case "4":
                # Delete Inflation Metric
                metric_id = int(input("Enter the ID of the metric to delete: "))
                delete_inflation_metric(metric_id)
                print("Inflation metric deleted successfully.")

            case "5":
                # Collect Data from Sources
                collect_data_from_sources()
                print("Data collected successfully.")

            case "6":
                # Exit
                print("Exiting. Thank you for using the Inflation Analysis Application!")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
