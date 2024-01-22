import pandas as pd
import matplotlib.pyplot as plt

def filter_data(conn, country=None, start_year=None, end_year=None):
    cursor = conn.cursor()

    # Modify this query based on your table structure
    query = 'SELECT * FROM InflationData WHERE 1'

    if country:
        query += ' AND CountryCode=%s'  # Use 'CountryCode' instead of 'country'
    if start_year:
        query += ' AND year>=%s'
    if end_year:
        query += ' AND year<=%s'

    cursor.execute(query, (country, start_year, end_year))

    rows = cursor.fetchall()

    return pd.DataFrame(rows, columns=['CountryCode', 'Year', 'Inflation'])  # Update column names



def plot_inflation_line(data):
    plt.plot(data['Year'], data['Inflation'], marker='o')
    plt.title(f'Inflation Trend for {data["CountryCode"].iloc[0]} ({data["Year"].min()} to {data["Year"].max()})')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.show()

def plot_inflation_bar(data):
    plt.bar(data['Year'], data['Inflation'])
    plt.title(f'Inflation Bar Chart for {data["CountryCode"].iloc[0]} ({data["Year"].min()} to {data["Year"].max()})')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.show()