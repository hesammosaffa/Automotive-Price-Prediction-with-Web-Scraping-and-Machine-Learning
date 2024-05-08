# Importing necessary functions from custom modules
from Functions.AppFunction import webReader
from Functions.convertToCSV import export_to_csv
import time

# Recording start time of the execution
start_time = time.time()

# Looping through page ranges to extract data
for i in range(1, 200, 10):
    # Extracting data for a range of pages
    all_cars_data = webReader(i, i + 9)

# Exporting extracted data to CSV
export_to_csv()

# Recording end time of the execution
end_time = time.time()

# Calculating total execution time
execution_time = end_time - start_time

# Printing total execution time
print(f"\nTotal Execution Time: {execution_time} seconds")
