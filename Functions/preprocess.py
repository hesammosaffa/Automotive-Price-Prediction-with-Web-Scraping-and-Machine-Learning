# Importing necessary libraries
import pandas as pd
import os
import pickle

# Function to preprocess user data and make predictions
def preprocess(model, brand, city, km):
    # Getting the path of the current file
    current_file_path = os.path.abspath(__file__)
    # Navigating to the previous directory
    previous_directory = os.path.dirname(os.path.dirname(current_file_path))

    # Paths to the saved models
    path_model = os.path.join(previous_directory, 'Models', 'le_Model.pkl')
    path_brand = os.path.join(previous_directory, 'Models', 'le_Brand.pkl')
    path_city = os.path.join(previous_directory, 'Models', 'le_City.pkl')
    path_catBoost = os.path.join(previous_directory, 'Models', 'catboost.pkl')
    path_sc = os.path.join(previous_directory, 'Models', 'StandardScaler.pkl')

    # Loading the saved models
    lion_model = open(path_model, 'rb')
    model_model = pickle.load(lion_model)
    lion_model.close()

    lion_brand = open(path_brand, 'rb')
    model_brand = pickle.load(lion_brand)
    lion_brand.close()

    lion_city = open(path_city, 'rb')
    model_city = pickle.load(lion_city)
    lion_city.close()

    sc_model = open(path_sc, 'rb')
    sc = pickle.load(sc_model)
    sc_model.close()

    catboost_model = open(path_catBoost, 'rb')
    catboost = pickle.load(catboost_model)
    catboost_model.close()

    # Creating a dictionary of user data
    user_data = {
        'brand': [brand],
        'model': [model],
        'city': [city],
        'km': [km]
    }

    # Creating a DataFrame from user data
    data = pd.DataFrame(user_data)

    # Transforming categorical features using Label Encoders
    data['brand'] = model_brand.transform(data['brand'])
    data['model'] = model_model.transform(data['model'])
    data['city'] = model_city.transform(data['city'])

    # Scaling numerical features using StandardScaler
    data = sc.transform(data)

    # Making predictions using the CatBoost model
    y_pred = catboost.predict(data)

    return y_pred
