from database.conn_db import connect_to_database

from database.create_db import create_tables
from database.load_data import load_data_into_country_info, load_data_into_inflation_data

# from database.load_data import load_data_from_csv

from auth.authenticate import auth_user 

from data_operations.create import create_entry
from data_operations.read import read_entries
from data_operations.update import update_entry
from data_operations.delete import delete_entry



from analysis.analysis_flow import analysis_flow

def main():

    # Connect to DB
    conn = connect_to_database() # Store that user credetial for whole session | run that for each calls

    print("Welcome to the Inflation Analysis App!")
    # try:
    print(create_tables(conn))
    # print(load_data_from_csv(conn, 'D:/ProjectFiles/ProjectZero/InflatioInsight/database/inflation-gdp.csv', 'CountryInfo'))
    # print(load_data_from_csv(conn, 'D:/ProjectFiles/ProjectZero/InflatioInsight/database/inflation-gdp.csv', 'InflationData'))
    print(load_data_into_country_info(conn))
    print(load_data_into_inflation_data(conn))

    # Authenticate user
    user_credentials = auth_user(conn)

    if not user_credentials:
        print("Exiting the Inflation Analysis App.")
        # Need to exit appAdmin 

    else:        
        # Inflation insight home page
        while True:
            print("Welcome to Home page")
            print("\nOptions:")
            print("1. Add Data")
            print("2. Read Data")
            print("3. Update Data")
            print("4. Delete Data")
            print("5. Analyse Data")
            print("6. Exit App")

            user_choice = input("Enter your choice (1-6): ")

            if user_choice == "1":
                create_entry(conn)
            elif user_choice == "2":
                read_entries(conn)
            elif user_choice == "3":
                update_entry(conn)
            elif user_choice == "4":
                delete_entry(conn)
            elif user_choice == "5":
                analysis_flow(conn)
            elif user_choice == "6":
                print("Exiting the Inflation Analysis App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    # except:
    #     print("Encountered Error")

    # Close DB connection
    conn.close()

if __name__ == "__main__":
    main()


# import sys

# from analysis.analysis import analysis

# # before running main
# # create db
# # load data

# def main():
#     print("Welcome to the Inflation Analysis App!")

#     # Connect to DB
    

#     # authenticate user
#     auth_user()


#     # Inflation insight home app 

#     # while not exit app

#         # ask for options - add data/update data/see data/delete data/visualize data
    
#             # while not exit add data
#                 # Take input
#                 # Display added data
        
#             # while not exit read data
#                 # Take input
#                 # Display data
        
#             # while not exit update data
#                 # Take input for reading
#                 # Display old data
#                 # Take update input
#                 # Display new data
        
#             # while not exit delete data
#                 # Take input for reading
#                 # Delete data and confirm
        
#             # while not exit visualize mode
#                 # ask for analysis parameters
#                 # show analysis
#                 # option to exit or check analysis for other country
    
