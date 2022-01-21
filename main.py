#dash and plotly imports
import dash 
from dash import html,dcc,dash_table
from dash.dependencies import Input,Output,State
import plotly.express as px
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import dash_bootstrap_components as dbc

#data science imports
import pandas as pd 

#imports from other scripts
from layout import get_layout
from process_inputs import make_prediction

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = get_layout()

@app.callback(
    Output("price_output","children"),
    Input("predict_button","n_clicks"),
    [
        State("neighbourhood_select","value"),State("bedrooms","value"),
        State("beds","value"),State("bathrooms","value"),
        State("host_since","date"),State("host_response_time_select","value"),
        State("host_boolean_switches","value"),State("host_listings_count","value"),
        State("host_acceptance_rate","value"),State("host_response_rate","value"),
        State("room_type_select","value"),State("property_type_input","value"),
        State("amenities","value"),State("minimum_nights","value"),
        State("maximum_nights","value"),State("accommodates","value"),
        State("instant_bookable_switch","value")
    ],
 )
def predict(n_clicks,neighbourhood,bedrooms,beds,bathrooms,host_since,host_response_time,host_boolean,host_listings_count,host_acc_rate,host_res_rate,room_type,prop_type,amenities,min_nights,max_nights,accommodates,instant_bookable):    
    if "superhost" in host_boolean:
        superhost = 1
    else:
        superhost = 0

    if "profile_pic" in host_boolean:
        profile_pic = 1
    else:
        profile_pic = 0

    if "profile_verified" in host_boolean:
        profile_ver = 1
    else:
        profile_ver = 0

    if "instant" in instant_bookable:
        instant = 1
    else:
        instant = 0
    
    entry = {
        "neighbourhood_cleansed":neighbourhood,"bedrooms":bedrooms,"bathrooms":bathrooms,
        "beds":beds,"host_since":host_since,"host_response_time":host_response_time,
        "host_listings_count":host_listings_count,"host_acceptance_rate":host_acc_rate,
        "host_response_rate":host_res_rate,"room_type":room_type,"property_type":prop_type,
        "amenities":amenities,"minimum_nights":min_nights,"maximum_nights":max_nights,
        "accommodates":accommodates,"host_is_superhost":superhost,"host_identity_verified":profile_ver,
        "host_has_profile_pic":profile_pic,"instant_bookable":instant
    }

    pred = make_prediction(entry)
    return "$"+str(round(pred,2))

if __name__ == '__main__':
    app.run_server(debug=True)