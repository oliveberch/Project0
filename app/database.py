import mysql.connector

def get_user_input():
    print("Enter MySQL Database Credentials:")
    user = input("Username: ")  
    password = input("Password: ")  

    return {
        "host": 3306,
        "user": user,
        "password": password,
        "database": "inflation_records"
    }

def connect_to_database():
    db_config = get_user_input()
    conn = mysql.connector.connect(**db_config)
    return conn

def create_tables():
    conn = None
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        # Table 1: CountryInfo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CountryInfo (
                CountryCode VARCHAR(3) PRIMARY KEY,
                Country VARCHAR(255),
                Region VARCHAR(255)
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
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        conn.commit()
        conn.close()
