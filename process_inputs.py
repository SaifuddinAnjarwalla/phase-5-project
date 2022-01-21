import pandas as pd
import re 
from datetime import datetime
from xgboost import XGBRegressor 


#in this file we define how we are goign to make the prediciton. we manupulate inputs and call the model 

def get_host_since_days(x):
    try:
        diff = (datetime.date(datetime.strptime('07/12/21','%d/%m/%y'))-x).days
        return diff
    except:
        return None 

def get_num_amenities(x):
    try:
        str_list = x[1:-1]
        am_list = str_list.split(',')
        return len(am_list)
    except:
        return None

def make_prediction(entry):

    df = pd.read_csv("data/empty_df.csv")
    df = df.drop(columns=['Unnamed: 0'])

    df['host_since_days'] = get_host_since_days(entry['host_since'])
    df['num_amenities'] = get_num_amenities(entry['amenities'])
    df['bedrooms'] = entry['bedrooms']
    df['beds'] = entry['beds']
    df['bathrooms'] = entry['bathrooms']

    df['minimum_nights'] = entry['minimum_nights']
    df['maximum_nights'] = entry['maximum_nights']
    df['host_listings_count'] = entry['host_listings_count']
    df['host_acceptance_rate'] = entry['host_acceptance_rate']
    df['host_response_rate'] = entry['host_response_rate']

    df['host_is_superhost'] = entry['host_is_superhost']
    df['host_identity_verified'] = entry['host_identity_verified']
    df['host_has_profile_pic'] = entry['host_has_profile_pic']
    df['instant_bookable'] = entry['instant_bookable']
    df['accommodates'] = entry['accommodates']

    if (f'room_type_{entry["room_type"]}') in df.columns:
        df[f'room_type_{entry["room_type"]}'] = 1
    
    if (f'property_type_{entry["property_type"]}') in df.columns:
        df[f'property_type_{entry["property_type"]}'] = 1

    if (f'neighbourhood_cleansed_{entry["neighbourhood_cleansed"]}') in df.columns:
        df[f'neighbourhood_cleansed_{entry["neighbourhood_cleansed"]}'] = 1

    if (f'host_response_time_{entry["host_response_time"]}') in df.columns:
        df[f'host_response_time_{entry["host_response_time"]}'] = 1

    df = df.fillna(0)

    model = XGBRegressor()
    model.load_model("models/model_2022-01-21.json")

    pred = model.predict(df)

    return pred[0]