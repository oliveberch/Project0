def create_tables(conn):

    # try:
        cursor = conn.cursor()

        # Table 1: CountryInfo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CountryInfo (
                CountryCode VARCHAR(3) PRIMARY KEY,
                Country VARCHAR(255),
                PRIMARY KEY (CountryCode)
            )
        ''')

        # Table 2: InflationData
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS InflationData (
                CountryCode VARCHAR(3),
                Year INT,
                Inflation FLOAT,
                PRIMARY KEY (CountryCode, Year),
                FOREIGN KEY (CountryCode) REFERENCES CountryInfo(CountryCode)
            )
        ''')

        # Table 3: Users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(255),
                Password VARCHAR(255)
            )
        ''')

        conn.commit()

        return "Database schema created successfully."
    # except:
    #     return "Failed to create database schema."
            