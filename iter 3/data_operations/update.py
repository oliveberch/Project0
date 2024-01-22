from database.conn_db import connect_to_database
import mysql.connector

# Update entry in the Inflation table
def update_entry(conn):
    try:
        cursor = conn.cursor()

        country_code = input("Enter country code name: ")
        year = input("Enter year: ")
        new_inflation = input("Enter inflation index: ")

        cursor.execute("UPDATE InflationData SET Inflation = %s WHERE CountryCode = %s AND Year = %s",
                (new_inflation, country_code, year))

        conn.commit()

        print("Entry Updated")

    except mysql.connector.Error as err:
        print("Error:", err)
