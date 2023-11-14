# main_file.py
import json
import re
from all_items_shop import *
import pyodbc

def connect_to_database():
    # Replace these values with your actual database credentials
    server = 'LAPTOP-SR\CBDB'
    database = 'test'
    username = 'sa'
    password = '12345'
    driver = 'ODBC Driver 17 for SQL Server'

    # Establish a connection to the database
    connection = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")

    # Create a cursor
    cursor = connection.cursor()

    return connection, cursor

def print_menu():
    print("1. Show all shop names")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Exit")

def main():
    # Connect to the database
    connection, cursor = connect_to_database()
    while True:
        # Print the menu
        print_menu()

        # Get user input
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Option 1: Show all shop names
            shop_names = all_items_shop(cursor)
            print("Shop Names:", shop_names)
        elif choice == '2':
            # Option 2: Add your logic for Option 2
            pass
        elif choice == '3':
            # Option 3: Add your logic for Option 3
            pass
        elif choice == '4':
            # Option 4: Add your logic for Option 4
            pass
        elif choice == '5':
            # Option 5: Add your logic for Option 5
            pass
        elif choice == '6':
            # Option 6: Exit the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
