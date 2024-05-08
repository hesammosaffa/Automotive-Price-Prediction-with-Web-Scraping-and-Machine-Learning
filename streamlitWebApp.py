# Importing necessary libraries
import streamlit as st
from Functions.preprocess import preprocess
import pandas as pd
import os

# Getting the current working directory
current_path = os.getcwd()
# Path to the CSV file containing cars data
csv_path = os.path.join(current_path, 'cars_data.csv')
# Reading the CSV file into a DataFrame
cars_data = pd.read_csv(csv_path, encoding='latin1')

# Setting up the header for the Streamlit app
st.header("Automotive Price Prediction with Web Scraping and Machine Learning")

# Getting unique city names and brand names from the DataFrame
city_list = cars_data['city'].unique()
brand_list = cars_data['brand'].unique()

# Creating selectbox widgets for selecting brand, model, city, and inputting km value
brand_name = st.selectbox("select brand name:", brand_list)
model_list = cars_data[cars_data['brand'] == brand_name]['model'].tolist()
model_name = st.selectbox("select model name:", model_list)
city_name = st.selectbox("select city name:", city_list)
km_value = float(st.number_input("The number of km the car has traveled:"))

# Creating a button for price prediction
btn = st.button('Price Prediction')

if btn:
    # Preprocessing user input and making price prediction
    price = preprocess(model_name, brand_name, city_name, km_value)
    # Displaying balloons to indicate successful prediction
    st.balloons()

    # Calculating price increase and decrease
    price_increase = price * 1.3
    price_decrease = price * 0.7

    # Displaying predicted prices with variations
    st.warning("Price after +30%: ${}".format(int(price_increase)))
    st.success("Original Price: ${}".format(int(price)))
    st.error("Price after -30%: ${}".format(int(price_decrease)))
