def view_data(conn, country, start_year, end_year):
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM InflationData WHERE CountryCode=%s AND Year BETWEEN %s AND %s',
                   (country, start_year, end_year))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("redirecting to home page")