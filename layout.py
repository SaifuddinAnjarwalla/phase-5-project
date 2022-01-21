#in this file we build the layout of our dash app

#dash and plotly imports
from dash import html,dcc,dash_table
from dash.dependencies import Input,Output,State
from numpy import place
import plotly.express as px
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import dash_bootstrap_components as dbc

#data science imports
import pandas as pd 

intro_card = dbc.Card([
        dbc.CardImg(src="/static/images/logo.svg",top=True),
        dbc.CardBody([html.H3('Get Advice From AI on Pricing Your Property'),
            html.Div(html.P('Input information about your potential listing and get guidance from our AI tool to avoid over- or underestimating your property.')) ]),
        dbc.CardFooter(
            html.P("Data taken from http://insideairbnb.com/get-the-data.html")
        )
    ],
    className = 'p-4 m-4'
)

prediction_button_card = dbc.Card([
        dbc.CardBody([
            html.H3('Make a prediction'),
            html.Div([html.Button('Predict',id='predict_button',n_clicks=0,style={'backgroundColor':'#ff5c5c','border':'none','border-radius':'10px','padding':'15px 32px'}),
                    html.Div(
                        [html.H3("Estimated price:"), html.H3("",id="price_output",className='p-2',style={'color':'#ff5c5c'})
                        ],
                        className = 'pt-2')],
                className = 'pt-2'
            )
        ],
        #className = 'align-center'
        )
    ],
    className = 'p-4 m-4'
)

boroughs = ['Islington', 'Kensington and Chelsea', 'Westminster',
       'Hammersmith and Fulham', 'Barnet', 'Hounslow',
       'Richmond upon Thames', 'Haringey', 'Croydon', 'Southwark',
       'Waltham Forest', 'Brent', 'Camden', 'Newham', 'Tower Hamlets',
       'Lambeth', 'Hackney', 'Merton', 'Lewisham', 'Wandsworth',
       'Bromley', 'Havering', 'Greenwich', 'Enfield', 'City of London',
       'Ealing', 'Barking and Dagenham', 'Hillingdon', 'Harrow',
       'Redbridge', 'Kingston upon Thames', 'Bexley', 'Sutton']

neighbourhood_select = dbc.Select(id = 'neighbourhood_select',options = [{"label":borough,"value":borough} for borough in boroughs])

input_group_basic = html.Div(
    [
        dbc.InputGroup(
            [dbc.InputGroupText('Listing Name',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="name",placeholder='Example: Superb 1-bedroom Apartment in Hammersmith'),        
            ],
            className = 'mb-3'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText('Description',style={'backgroundColor':'#9ea39d'}),dbc.Textarea(id="description",placeholder='Example: Bright double bedroom with a large window has a relaxed feeling! It comfortably fits one or two and is centrally located just two blocks from Ravenscourt Park.')        
            ],
            className = 'mb-3'
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText('London borough',style={'backgroundColor':'#9ea39d'}),neighbourhood_select,
                dbc.InputGroupText('Bedrooms',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="bedrooms",placeholder="1",type="number",min=0,max=10,step=1),
                dbc.InputGroupText('Beds',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="beds",placeholder="1",type="number",min=0,max=50,step=1),
                dbc.InputGroupText('Bathrooms',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="bathrooms",placeholder="1", type="number",min=0,max=10,step=1)
            ],
            style = {'width':'100%'},
            className = 'mb-3'
        )
    ],
    className = 'p-2 m-2'
)

host_response_time_select = dbc.Select(
    id = 'host_response_time_select',
    options = [
        {"label":"within an hour","value":"within an hour"},
        {"label":"within a few hours","value":"within a few hours"},
        {"label":"within a day","value":"within a day"},
        {"label":"a few days or more","value":"a few days or more"},
    ]
)

host_boolean_switches = html.Div(
    [
        dbc.Checklist(
            options=[
                {"label": "Superhost", "value": 'superhost'},
                {"label": "Profile picture available", "value": 'profile_pic'},
                {"label": "Identity verified", "value": 'profile_verified'},
            ],
            value=[],
            id="host_boolean_switches",
            inline=True,
            switch=True,
        ),
    ],
    #style = {'border':'1px solid #ff5c5c'},
    className = 'p-2 ml-2 mt-1 mb-1'
)

input_group_host = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupText('Airbnb joining date',style={'backgroundColor':'#9ea39d'}),dcc.DatePickerSingle(id='host_since',date='2022-01-01',display_format='MMM Do, YY'), 
                dbc.InputGroupText('Response time',style={'backgroundColor':'#9ea39d'}),host_response_time_select,
                dbc.InputGroupText('Further details',style={'backgroundColor':'#9ea39d'}),host_boolean_switches
            ],
            className = 'mb-3'
        ),
        dbc.InputGroup(
            [   
                dbc.InputGroupText('Number of other listings',style={'backgroundColor':'#9ea39d'}),
                dbc.Input(id="host_listings_count",placeholder="0", type="number"),
                dbc.InputGroupText('Current acceptance rate',style={'backgroundColor':'#9ea39d'}),
                dbc.Input(id="host_acceptance_rate",placeholder="100", type="number",min=0,max=100,step=1),
                dbc.InputGroupText("%"),
                dbc.InputGroupText('Current response rate',style={'backgroundColor':'#9ea39d'}),
                dbc.Input(id="host_response_rate",placeholder="100", type="number",min=0,max=100,step=1),
                dbc.InputGroupText("%"),
            ],
            className = 'mb-3'
        )
    ],
    className = 'p-2 m-2'
)

room_type_select = dbc.Select(
    id = 'room_type_select',
    options = [
        {"label":"private room","value":"Private room"},
        {"label":"entire house/apartment","value":"Entire home/apt"},
        {"label":"shared room","value":"Shared room"},
        {"label":"hotel room","value":"Hotel room"},
    ]
)

input_group_further = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupText('Accommodation type',style={'backgroundColor':'#9ea39d'}),room_type_select,
                dbc.InputGroupText('Property type',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="property_type_input",placeholder="Example: entire loft or shared room in townhouse", type="text")
            ],
            className = 'mb-3'
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText('Amenities',style={'backgroundColor':'#9ea39d'}),dbc.Textarea(id="amenities",placeholder='Example: Hot water, Heating, Coffee maker, TV with HDMI cable')
            ],
            className = 'mb-3'
        )
    ],
    className = 'p-2 m-2'
)

instant_bookable_switch = html.Div(
    [
        dbc.Checklist(
            options=[
                {"label": "", "value": 'instant'},
            ],
            value=[],
            id="instant_bookable_switch",
            inline=True,
            switch=True,
        ),
    ],
    className = 'p-2 m-2'
)

input_group_offering = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupText('Minimum nights',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="minimum_nights",placeholder="1", type="number",min=1,max=365,step=1),
                dbc.InputGroupText('Maximum nights',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="maximum_nights",placeholder="1", type="number",min=1,max=365,step=1),
                dbc.InputGroupText('Maximum number of guests',style={'backgroundColor':'#9ea39d'}),dbc.Input(id="accommodates",placeholder="4", type="number",min=1,max=50,step=1),
                dbc.InputGroupText('Instant bookable',style={'backgroundColor':'#9ea39d'}),instant_bookable_switch
            ],
            className = 'mb-3'
        )
    ],
    className = 'p-2 m-2'
)

def get_layout():
    layout = dbc.Container([
        dbc.Row([
            dbc.Col(
                [
                    intro_card,
                    prediction_button_card
                ],
                style = {
                    #'border':'2px dashed red',
                    'backgroundColor':'#ff5c5c'
                },
                #className = 'p-2 m-2',
                width = 4
            ),
            dbc.Col(
                html.Div(
                    id = 'input_div',
                    children = [
                        html.H4('Step 1: Enter basic information about your property:',className = 'p-2 m-2 text-center',style={'background':'#ff5c5c'}),
                        input_group_basic,
                        html.H4('Step 2: Enter some information about yourself as a host:',className = 'p-2 m-2 text-center',style={'backgroundColor':'#ff5c5c'}),
                        input_group_host,
                        html.H4('Step 3: Enter more details about your property:',className = 'p-2 m-2 text-center',style={'backgroundColor':'#ff5c5c'}),
                        input_group_further,
                        html.H4('Step 4: Enter information about your offering details:',className = 'p-2 m-2 text-center',style={'backgroundColor':'#ff5c5c'}),
                        input_group_offering
                    ]
                ),
                style = {
                    #'border':'2px dashed red'
                },
                #className = 'p-2 m-2',
                width = 8
            ),
        ])
    ],
    fluid = True 
    )

    return layout