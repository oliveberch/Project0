from database.conn_db import connect_to_database

def year(conn, country):
    try:
        cursor = conn.cursor()

        cursor.execute('SELECT DISTINCT year FROM InflationData WHERE CountryCode=%s', (country,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        start_year = input("Enter the start year: ")
        end_year = input("Enter the end year: ")

        return start_year, end_year

    except Exception as e:
        print(f"Error: {e}")
        return None, None
