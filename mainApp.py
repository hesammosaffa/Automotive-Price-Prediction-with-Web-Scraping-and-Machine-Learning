from Functions.AppFunction import webReader
from Functions.convertToCSV import export_to_csv
import time


start_time = time.time()
for i in range(1,200,10):
    all_cars_data = webReader(i,i+9)

export_to_csv()

end_time = time.time()
execution_time = end_time - start_time
print(f"\nTotal Execution Time: {execution_time} seconds")

