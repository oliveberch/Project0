from database.conn_db import connect_to_database
import mysql.connector

# Delete entry from the GDP table
def delete_entry(conn):
    cursor = conn.cursor()

    country = input("Enter country code: ")
    year = input("Enter year: ")

    try:
        cursor.execute("DELETE FROM InflationData WHERE CountryCode = %s AND Year = %s", (country, year))
        conn.commit()
        print("entry deleted")

    except mysql.connector.Error as err:
        print("Error:", err)
