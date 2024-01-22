# app/analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from database import connect_to_database

def perform_analysis(user_id, country_code, start_year, end_year):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Retrieve Inflation Data for the specified country and year range
    cursor.execute("SELECT Year, Inflation FROM InflationData WHERE CountryCode = %s AND Year BETWEEN %s AND %s",
                   (country_code, start_year, end_year))
    data = cursor.fetchall()

    if not data:
        print("No data available for the specified country and year range.")
        return

    # Perform data analysis and visualization (for simplicity, just a line chart)
    df = pd.DataFrame(data, columns=['Year', 'Inflation'])
    plt.plot(df['Year'], df['Inflation'], marker='o')
    plt.title(f'Inflation Trend for {country_code} ({start_year} to {end_year})')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.show()

    conn.close()
