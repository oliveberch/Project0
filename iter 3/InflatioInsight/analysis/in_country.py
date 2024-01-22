from database.conn_db import connect_to_database

def country(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT DISTINCT CountryCode FROM InflationData')

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        country_code = input("Enter the country code: ")

        return country_code

    except Exception as e:
        print(f"Error: {e}")
        return None
