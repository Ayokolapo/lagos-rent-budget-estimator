import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pickle
from prediction_data import *
import joblib


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('Cleaned_house_data.csv')
df['price'] = df['price']/1000000
df['price'] = df['price']
dff = df.groupby(['location','area'])['price'].median().reset_index()
df1 = dff.groupby(['location'])['price'].sum().reset_index()
df2 = df.groupby(['location','bed'])['price'].median().reset_index()
dfnew = df.groupby(['island','location'])['price'].median().reset_index()
dfbed = df.groupby(['area','bed'])['price'].median().reset_index()
model1 = decompress_pickle('small_model.pbz2')

#joblib.load('model.pkl')


fig =px.sunburst(dfnew,path = ['island','location'],values='price',
	color='price', color_continuous_scale = "algae", labels = {'location':'location','price':'Average Price'},
	hover_data = {'location': True,'price':True,'island':False}
	,title = 'Average Price per Location (in NGN millions)')

fig.update_traces(
        go.Sunburst(hovertemplate= '<b>%{label} </b> <br> Average Price: NGN%{color:.1f}m<br>'))

fig.update_layout(autosize= True,
#height = 250, width = 550,
    margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor = "#202a3b",plot_bgcolor= "#202a3b",
    font=dict(color="#c3c3c3",size = 7))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)      


#10571d
#bdbcbc


#app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

app.title = 'Lagos Rent Budget Estimator'
server = app.server

app.layout = html.Div([
	html.H5("Lagos Rent Budget Estimator",style = {'color': 'white'}),
	html.P("Find the home of your dreams",style = {'color': 'orange','fontSize':10}),
	
	html.Div(
		[html.P("Number of Properties", style = {'textAlign': 'left','color': 'white', 'fontSize': 10}),
		html.P(str(round(df.location.count(),0)),style = {'textAlign': 'left','color':'white','fontSize': 20,'fontWeight': 'normal'})], 
		className = 'card_container three columns'),
	html.Div(
		[html.P("Number of Locations", style = {'textAlign': 'left','color': 'white','fontSize': 10}),
		html.P(str(round(df1.location.count(),0)),style = {'textAlign': 'left','color':'white','fontSize': 20,'fontWeight': 'normal'})], 
		className = 'card_container three columns'),
	html.Div(
		[html.P("Number of Areas", style = {'textAlign': 'left','color': 'white','fontSize': 10}),
		html.P(str(round(dff.area.count(),0)),style = {'textAlign': 'left','color':'white','fontSize': 20,'fontWeight': 'normal'})], 
		className = 'card_container three columns'),
	html.Div(
		[html.P("Average Price", style = {'textAlign': 'left','color': 'white','fontSize': 10}),
		html.P(str(round(df.price.median(),2)) + ' M',style = {'textAlign': 'left','color':'white','fontSize': 20,'fontWeight': 'normal'})], 
		className = 'card_container three columns'),

	html.Div([dcc.Graph(id = 'sunburst_chart', figure = fig,style={'width':'72vh','height':'50vh'}) ,
		dcc.Graph(id = 'bar_chart',style={'width':'72vh','height':'50vh'}, config={'displayModeBar': False}),
		html.Div([dcc.Dropdown(id = 'dropdown',options=[{'label': c, 'value': c}
			for c in (dff['location'].unique())],value='gbagada',searchable=False, optionHeight = 25,style={"width": '20vh','fontSize':10})
        ],className = 'dcc_compon')]
        ,className = 'graph-container'),

	html.Div([dcc.Graph(id = 'sample_gauge2',style={'width':'72vh','height':'50vh'}),
	html.Div([html.P(id = 'budget_estimate',style = {'textAlign':'center','color': '#619a6b',
	'fontSize':25})],
	className = 'budget_container'),
		html.Div([dcc.Dropdown(id = 'dropdown2',options=[{'label': c, 'value': c}
			for c in (dff['location'].unique())],value='gbagada',searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"}),
		dcc.Dropdown(id = 'dropdown3',searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"}),
		dcc.Dropdown(id = 'dropdownbed',options=[{'label': c, 'value': c}
			for c in (dfbed['bed'].unique())],searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"}),
		dcc.Dropdown(id = 'dropdownserv',options=[{'label': 'serviced? Yes' , 'value':'serviced? Yes' },
			{'label': 'serviced? No' , 'value':'serviced? No' }],searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"}),
		dcc.Dropdown(id = 'dropdownterrace',options=[{'label': 'terraced? Yes' , 'value':'terraced? Yes' },
			{'label': 'terraced? No' , 'value':'terraced? No' }],searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"}),
		dcc.Dropdown(id = 'dropdownfurn',options=[{'label': 'furnished? Yes' , 'value':'furnished? Yes' },
			{'label': 'furnished? No' , 'value':'furnished? No' }],searchable=False, 
			optionHeight = 25,style={"width": '20vh','fontSize':10,'margin-bottom':"4px"})],className = 'dcc_compon')]
		,className = 'gauge-container'),
		#html.Div([html.Div(id= 'budget_estimate2',style = {'textAlign':'center','color': '#619a6b','fontSize':15})],
		#className = 'estimate_container'),
		# Hidden div inside the app that stores the intermediate value
		html.Div(id='intermediate-value', style={'display': 'none'}),
		html.P("source of data - www.PropertyPro.ng", style = {'textAlign': 'center','color': '#619a6b','fontSize': 8}, 
		className = 'datasource')
	])

@app.callback(
    Output("bar_chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(location):
	mask = dff["location"] == location
	figure = px.bar(dff[mask],x = 'price',y = 'area'#,animation_frame='location',animation_group='location'
		,color_discrete_sequence =['#619a6b']*len(df1),orientation = 'h')
	figure.update_layout(autosize= True,
	#height = 250, width = 550,
		margin=dict(l=20, r=20, t=40, b=20),
		paper_bgcolor = "#202a3b",plot_bgcolor= "#202a3b",
		font=dict(color= "#c3c3c3",size = 7), title_text='Average Price per Area in Location (in NGN millions)')
	figure.update_xaxes(fixedrange=True)
	figure.update_yaxes(fixedrange=True)
	figure.update_xaxes(showgrid=False)
	figure.update_yaxes(showgrid=False, categoryorder = 'total ascending')
	figure.update_traces(dict(marker_line_width=0))
	return figure
	

@app.callback(
    Output('dropdown3', 'options'),
    Input('dropdown2', 'value'))
def set_area_options(location):
    return [{'label': i, 'value': i} for i in dff['area'][dff['location']==location]]


@app.callback(
    Output('dropdown3', 'value'),
    Input('dropdown3', 'options'))
def set_area_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('dropdownbed', 'options'),
    Input('dropdown3', 'value'))
def set_area_options(area):
    return [{'label': i, 'value': i} for i in dfbed['bed'][dfbed['area']==area]]

@app.callback(
    Output('dropdownbed', 'value'),
    Input('dropdownbed', 'options'))
def set_area_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output("intermediate-value", "children"), 
    Input("dropdown2", "value"),Input("dropdown3", "value"),Input("dropdownbed", "value"),
    Input("dropdownserv", "value"),Input("dropdownterrace", "value"),Input("dropdownfurn", "value"))
def get_estimate(location,area,bed,serviced,terraced,furnished):
	data = predict_data(location,area,bed,serviced,terraced,furnished)
	return model1.predict(data)[0]

@app.callback(
    Output("sample_gauge2", "figure"), 
    Input("intermediate-value", "children"))
def update_gauge_chart(intermediate_value):
	figgauge = go.Figure(go.Indicator(mode = "gauge+number",value = intermediate_value,
		domain = {'x': [0, 1], 'y': [0, 1]},
		title = {'text': "Budget Estimate"}))
	figgauge.update_layout(autosize= True,
	#height = 250, width = 550,
    	margin=dict(l=30, r=30, t=70, b=30),
    	paper_bgcolor = "#202a3b",plot_bgcolor= "#202a3b",
    	font=dict(color="#c3c3c3"))
	figgauge.update_xaxes(showgrid=False)
	figgauge.update_yaxes(showgrid=False)     
	return figgauge

@app.callback(
    Output('budget_estimate', 'children'),
    Input("intermediate-value", "children"))
def set_budget(input_value):
    return 'Your budget should be between {:,} and {:,} {} '.format(int(round(input_value-(input_value*0.2),-4)),int(round(input_value+(input_value*0.2),-4)),'Naira')

if __name__ == '__main__':
	app.run_server(debug=True)

