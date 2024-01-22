from database.conn_db import connect_to_database

import mysql.connector
 
def display_countries(conn):

    cursor = conn.cursor()
    try:
        cursor.execute('SELECT DISTINCT country FROM CountryInfo')
        
        # Fetch all rows
        rows = cursor.fetchall()

        # Display the data
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("Error:", err)


def display_year_for_country(conn, country):
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT DISTINCT year FROM CountryInfo WHERE country = %s',(country))
        
        # Fetch all rows
        rows = cursor.fetchall()

        # Display the data
        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print("Error:", err)

def display_inflation_for_year_country(conn, country, year):
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT Inflation FROM InflationData WHERE CountryCode = %s AND Year = %s', (country, year))
    
        # Fetch all rows
        rows = cursor.fetchall()

        # Display the data
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("Error:", err)
