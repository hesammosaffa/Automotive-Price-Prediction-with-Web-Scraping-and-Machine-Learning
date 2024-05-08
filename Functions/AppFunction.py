# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from mysql import connector
import time

# Function to read data from a website
def webReader(startpage, endpage):
    # Setting up options for Firefox webdriver
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.headless = True

    # Initializing page count
    count = startpage
    # Creating table if it doesn't exist
    create_table_if_not_exists()

    # Looping through the pages
    while startpage < endpage:
        # URL of the website
        url = 'https://www.auto123.ca/en-ca/cars?Favorites=false&Distance=100&Country=CA&YearMin=2000&YearMax=2025&YearLow=2000&PriceMin=0&PriceMax=100000&PriceNone=false&PriceLow=1000&PriceHigh=100000&MileageMin=0&MileageMax=300000&MileageHigh=300000&Promotion=false&BuyOnline=false&Certified=false&Inspected=false&ShopiCare=false&Bridge=false&Viral=false&PageIndex={}&PageSize=24&ImageTotal=1&SortExpression=Pertinence&SortDirection=1&Source=Auto123&Division=Automotive'.format(startpage)

        try:
            # Initializing webdriver
            driver = webdriver.Firefox(options=options)
            driver.get(url)

            # Finding elements on the webpage
            cars_price = driver.find_elements(By.CSS_SELECTOR, "div.middle div.price span")
            cars_brand = driver.find_elements(By.CSS_SELECTOR, "div.middle div.make")
            cars_model = driver.find_elements(By.CSS_SELECTOR, "div.middle div.model span")
            cars_city = driver.find_elements(By.CSS_SELECTOR, "div.row-2 div.grid div.overflow")
            cars_km = driver.find_elements(By.CSS_SELECTOR, "div div.data div.row-2 div:nth-child(2) div:nth-child(3)")

            # Connecting to MySQL database
            cnx = connector.connect(user='root', password='hesam1100417', host='127.0.0.1', database='test')
            cursor = cnx.cursor()

            # SQL queries
            insert_query = ('INSERT INTO cars_data (brand, model, city, km, price) VALUES (%s, %s, %s, %s, %s);')
            select_query = ('SELECT * FROM cars_data WHERE brand = %s AND model = %s AND city = %s AND km = %s AND price = %s;')

            # Iterating through each element and extracting data
            for price, brand, model, city, km in zip(cars_price, cars_brand, cars_model, cars_city, cars_km):
                price_text = price.text.strip() # Removing extra spaces from the text
                if price_text and price_text.replace('$', '').replace(',', '').replace('.', '').isdigit():
                    parsed_price = float(price_text.replace('$', '').replace(',', ''))
                else:
                    parsed_price = None

                parsed_km = float(km.text.replace(' km', '').replace(',', '').replace(' KM', ''))
                parsed_brand = brand.text
                parsed_model = model.text
                parsed_city = city.text

                # Executing SQL queries
                cursor.execute(select_query, (parsed_brand, parsed_model, parsed_city, parsed_km, parsed_price))
                result = cursor.fetchone()

                if not result:
                    cursor.execute(insert_query, (parsed_brand, parsed_model, parsed_city, parsed_km, parsed_price))

            # Committing changes to the database
            cnx.commit()
            cursor.close()
            cnx.close()

            # Printing status
            print(f'Page {count} is done!')
            count += 1

            # Quitting webdriver
            driver.quit()
            startpage += 1

        except Exception as e:
            # Handling exceptions
            print(f"An error occurred: {str(e)}")
            print("Trying again in 5 seconds...")
            time.sleep(5)

# Function to create table in MySQL database if it doesn't exist
def create_table_if_not_exists():
    # Connecting to MySQL database
    cnx = connector.connect(user='root', password='hesam1100417', host='127.0.0.1', database='test')
    cursor = cnx.cursor()

    # Query to check if the table exists
    check_table_query = "SHOW TABLES LIKE 'cars_data';"
    cursor.execute(check_table_query)
    result = cursor.fetchone()

    # If the table does not exist, create it
    if not result:
        create_table_query = """
            CREATE TABLE cars_data (
                brand VARCHAR(30),
                model VARCHAR(30),
                city VARCHAR(30),
                km VARCHAR(30),
                price VARCHAR(30)
            );
        """
        cursor.execute(create_table_query)
        print("Table 'cars_data' created successfully!")
    
    # Closing Connection
    cursor.close()
    cnx.close()
