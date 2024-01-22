import csv
import mysql.connector
    
def load_data_into_country_info(conn):
    try:
        cursor = conn.cursor()

        with open('D:/ProjectFiles/Project0/iter 3/database/CountryInfo.csv') as f:
            reader = csv.DictReader(f)
            data = [(row['Country Code'], row['Country']) for row in reader]

        # Insert or update data into the CountryInfo table
        cursor.executemany(
            "INSERT INTO CountryInfo (CountryCode, Country) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Country = VALUES(Country)",
            data)

        conn.commit()
        return "Country Data added."
    except Exception as e:
        return f"Failed to load Country data. Error: {e}"

def load_data_into_inflation_data(conn):
    try:
        cursor = conn.cursor()

        with open('D:/ProjectFiles/Project0/iter 3/database/InflationData.csv') as f:
            reader = csv.DictReader(f)
            data = [(row['Country Code'], int(row['Year']), float(row['Inflation'])) for row in reader]

        # Insert data into InflationData table
        cursor.executemany("INSERT INTO InflationData (CountryCode, Year, Inflation) VALUES (%s, %s, %s) "
                           "ON DUPLICATE KEY UPDATE Inflation = VALUES(Inflation)",
                           data)

        conn.commit()
        return "Inflation Data added."
    except Exception as e:
        return f"Failed to load Inflation data. Error: {e}"


# def load_data_from_csv(conn, csv_path, table_name):
#         cursor = conn.cursor()
#         with open(csv_path, 'r') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip header row
#             for row in reader:
#                 placeholders = ', '.join(['%s' for _ in row])
#                 cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)
#         conn.commit()
#         print(f"Data loaded into '{table_name}' table successfully.")

# def load_data(conn):
#     try:
#         cursor = conn.cursor()

#         # Read data from the inflation-GDP CSV file
#         with open('D:/ProjectFiles/ProjectZero/InflatioInsight/database/inflation-gdp.csv') as f:
#             reader = csv.DictReader(f)
#             data = list(reader)
        
#         # Insert data into the GDP table
#         for row in data:
#             cursor.execute("INSERT INTO InflationData(CountryCode, Year, Inflation) VALUES (%s, %s, %s)",
#                         (row['Country Code'], row['Year'], row['Inflation']))
        
#         # Commit the changes and close connection
#         conn.commit()
#         return "Data added to DB"
    
#     except:
#         return "Failed to load Data Set"