Certainly! Here's the translation of the provided README template into English:

Car Information Retrieval and Price Prediction Project
Brief Description:

This project collects car information from the Auto123 website using the Selenium library and Firefox WebDriver, and stores them in a MySQL database. In the next step, this data is read from the database and saved as a CSV file. Subsequently, preprocessing and statistical analysis are performed, and machine learning is conducted using the CatBoostRegressor algorithm, achieving an accuracy of 73%. Additionally, a web application has been implemented using the Streamlit library, allowing users to easily predict car prices.

Installation and Usage:
Install the required libraries:
Copy code
pip install selenium webdriver firefox mysql-connector-python streamlit catboost pandas numpy
Run the main.py file:
css
Copy code
python main.py
After running, go to localhost:8501 to access the web application.
Dependencies:
Selenium
Firefox WebDriver
MySQL Connector Python
Streamlit
CatBoost
Pandas
NumPy
License:
This project is published under the MIT license. For more information, see the LICENSE file.

----------------------------------------------------------------------------------
***To execute the steps flawlessly, follow these instructions:

1. Run the `mainApp.py` file, which reads 200 pages of data from the auto123.ca website when executed, saves it into the database, and finally reads all the information from the database and writes it into the `cars_data.csv` file. This task has already been completed, and the `cars_data.csv` file exists.

2. Execute the `carPriceModel.ipynb` file to save the models in the `Models` folder. It only requires the installation of the `catboost` library to run this code.

3. To predict car prices, a web application has been created using the `streamlit` library. The file is named `streamlitWebApp.py`, and it can be run using the command `streamlit run streamlitWebApp.py`.
----------------------------------------------------------------------------------
Contact:
If you have any questions or suggestions, feel free to contact me:

Email: hesam.mosaffa.1251@gmail.com
Linkedin: www.linkedin.com/in/hesameddin-mosaffa