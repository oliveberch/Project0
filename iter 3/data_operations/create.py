import mysql.connector
from database.conn_db import connect_to_database

# Create new entry in the GDP table
def create_entry(conn):

    cursor = conn.cursor()

    country = input("Enter country name: ")
    country_code = input("Enter country code: ")
    year = input("Enter year: ")
    inflation = input("Enter inflation index: ")

    try:
        # Check if the entry already exists in CountryInfo
        cursor.execute("SELECT COUNT(*) FROM CountryInfo WHERE CountryCode = %s", (country_code,))
        count = cursor.fetchone()[0]

        if count == 0:
            # Entry doesn't exist, insert into CountryInfo
            cursor.execute("INSERT INTO CountryInfo(CountryCode, Country) VALUES (%s, %s)",
                        (country_code, country))

        # Check if the entry already exists in InflationData
        cursor.execute("SELECT COUNT(*) FROM InflationData WHERE CountryCode = %s AND Year = %s", (country_code, year))
        count = cursor.fetchone()[0]

        if count == 0:
            # Entry doesn't exist, insert into InflationData
            cursor.execute("INSERT INTO InflationData(CountryCode, Year, Inflation) VALUES (%s, %s, %s)",
                        (country_code, year, inflation))
        else:
            # Entry already exists, update the Inflation value
            cursor.execute("UPDATE InflationData SET Inflation = %s WHERE CountryCode = %s AND Year = %s",
                        (inflation, country_code, year))
        conn.commit()
        print("Data Added successfully")

    except conn as err:
        if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            print("Duplicate entry. Data with the same country code already exists.")
        else:
            print("Error:", err)