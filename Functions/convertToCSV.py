import csv
from mysql import connector
import os
def export_to_csv():
    cnx = connector.connect(user='root', password='hesam1100417', host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    # Query to select all rows from the cars_data table
    select_query = "SELECT * FROM cars_data;"
    cursor.execute(select_query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Define the path for the CSV file
    current_file_path = os.path.abspath(__file__)
    previous_directory = os.path.dirname(os.path.dirname(current_file_path))
    path = os.path.join(previous_directory, "cars_data.csv")

    csv_file_path = path

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow([i[0] for i in cursor.description])

        # Write the rows from the database to the CSV file
        csv_writer.writerows(rows)

    print(f"Data exported to {csv_file_path} successfully!")

    # Closing Connection
    cursor.close()
    cnx.close()

