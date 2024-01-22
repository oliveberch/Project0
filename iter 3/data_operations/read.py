from data_operations.display_data import display_countries, display_year_for_country, display_inflation_for_year_country

def read_entries(conn):
    cursor = conn.cursor()

    print("Read data from DB based on your prefences.")

    display_countries(conn)

    country_code = input("Enter country code: ")

    display_year_for_country(conn, country_code)

    start_year = input("Enter Start year: ")
    end_year = input("Enter End year: ")

    query = "SELECT * FROM InflationData WHERE "
    params = []

    if country_code:
        query += "CountryCode = %s"
        params.append(country_code)

    if start_year:
        query += " AND Year >= %s"
        params.append(start_year)

    if end_year:
        query += " AND Year <= %s"
        params.append(end_year)

    # Remove the trailing "AND" if any
    if query.endswith("AND"):
        query = query[:-4]

    cursor.execute(query, tuple(params))
    # entries = cursor.fetchall()

    # return entries

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the data
    for row in rows:
        print(row)

    print("Exiting Read Data Page")

    return 
