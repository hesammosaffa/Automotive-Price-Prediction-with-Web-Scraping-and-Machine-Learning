import pandas as pd
import os
import pickle




def preprocess(model,brand,city,km):
    current_file_path = os.path.abspath(__file__)
    previous_directory = os.path.dirname(os.path.dirname(current_file_path))

    path_model = os.path.join(previous_directory,'Models','le_Model.pkl')
    path_brand = os.path.join(previous_directory,'Models','le_Brand.pkl')
    path_city = os.path.join(previous_directory,'Models','le_City.pkl')
    path_catBoost = os.path.join(previous_directory,'Models','catboost.pkl')
    path_sc = os.path.join(previous_directory,'Models','StandardScaler.pkl')


    lion_model = open(path_model,'rb')
    model_model = pickle.load(lion_model)
    lion_model.close 

    lion_brand = open(path_brand,'rb')
    model_brand = pickle.load(lion_brand)
    lion_brand.close 

    lion_city = open(path_city,'rb')
    model_city = pickle.load(lion_city)
    lion_city.close 

    sc_model = open(path_sc,'rb')
    sc = pickle.load(sc_model)
    sc_model.close 

    catboost_model = open(path_catBoost,'rb')
    catboost = pickle.load(catboost_model)
    catboost_model.close 


    user_data = {
    'brand': [brand],
    'model': [model],
    'city': [city],
    'km': [km]
      }
    
    data = pd.DataFrame(user_data)

    data['brand'] = model_brand.transform(data['brand'])
    data['model'] = model_model.transform(data['model'])
    data['city'] = model_city.transform(data['city'])

    data = sc.transform(data)

    y_pred = catboost.predict(data)

    return y_pred


