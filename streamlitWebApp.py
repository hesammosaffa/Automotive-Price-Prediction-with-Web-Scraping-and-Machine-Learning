import streamlit as st
from Functions.preprocess import preprocess
import pandas as pd
import os


current_path = os.getcwd()
csv_path = os.path.join(current_path, 'cars_data.csv')
cars_data = pd.read_csv(csv_path, encoding='latin1')

st.header("Automotive Price Prediction with Web Scraping and Machine Learning")

city_list = cars_data['city'].unique()
brand_list = cars_data['brand'].unique()

brand_name = st.selectbox("select brand name:",brand_list)

model_list =cars_data[cars_data['brand'] == brand_name]['model'].tolist()

model_name = st.selectbox("select model name:",model_list)
City_name = st.selectbox("select city name:", city_list)
km_value = float(st.number_input("The number of km the car has traveled:"))
btn = st.button('Price Prediction')

if btn:
    price = preprocess(model_name,brand_name,City_name,km_value)
    st.balloons()

    price_increase = price * 1.3
    price_decrease = price * 0.7


    st.warning("Price after +30%: ${}".format(int(price_increase)))
    st.success("Original Price: ${}".format(int(price)))
    st.error("Price after -30%: ${}".format(int(price_decrease)))




