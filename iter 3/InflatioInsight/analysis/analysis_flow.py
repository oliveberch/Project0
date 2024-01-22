from analysis.in_country import country
from analysis.in_year import year
from analysis.view_data import view_data
from analysis.visualize import filter_data, plot_inflation_line, plot_inflation_bar

def analysis_flow(conn):
    user_country = country(conn)
    user_start_year, user_end_year = year(conn, user_country)

    user_analysis_prefence = input("Enter your data analysis preference (e.g., 'data', 'visual', etc.): ")

    if user_analysis_prefence == 'data':
        view_data(conn, user_country, user_start_year, user_end_year)


    elif user_analysis_prefence == 'visual':
        user_visual_preference = input("Enter your visualization preference (e.g., 'plot', 'bar', etc.): ")

        if user_visual_preference == 'plot':
            filtered_data = filter_data(conn, user_country, user_start_year, user_end_year)
            plot_inflation_line(filtered_data)
            print("Data range visualized. Exiting analysis page.")
            
        elif user_visual_preference == 'bar':
            filtered_data = filter_data(conn, user_country, user_start_year, user_end_year)
            plot_inflation_bar(filtered_data)
            print("Data range visualized. Exiting analysis page.")

        else:
            print("Invalid preference.")
