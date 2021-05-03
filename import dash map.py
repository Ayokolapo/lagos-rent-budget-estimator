import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import json
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/Cleaned_house_data.csv')
#print(df.head())
#df1 = df.dropna()
#f = open('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/lagospolygon.geojson',)
#places = json.load(f)
#f.close()
#df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/location and price.csv')

#fig = px.choropleth(df, geojson=places, locations='location', color='price',
 #                         color_continuous_scale="Viridis",
  #                        range_color=(400000, 4000000),
   #                      labels={'unemp':'unemployment rate'}
    #                      )
#fig.update_geos(fitbounds="locations", visible=False)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

#fig = px.choropleth_mapbox(df, geojson=places, locations='location', color='price',
 #                          color_continuous_scale="Viridis",
  #                         range_color=(400000, 4000000),
   #                        mapbox_style="carto-positron",
    #                       zoom=3, center = {"lat": 6.5244, "lon": 3.3792},
     #                      opacity=0.5,
      #                     labels={'unemp':'unemployment rate'}
       #                   )
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()


#app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)



#app.layout = 

#if __name__ == '__main__':
#	app.run_server(debug=True)

#df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/Cleaned_house_data.csv')
df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/location and price.csv')

#print(df.head())
#df1 = df.dropna()
#df['price'] = round(df['price']/1000000,2)
#dff = df.groupby(['location','area'])['price'].sum().reset_index()
#df1 = dff.groupby(['location'])['price'].sum().reset_index()
#df2 = df.groupby(['location','bed','bath'])['price'].median().reset_index()
df2 = df.head(3)

fig = px.scatter(df2, x="average price", y="count",
	         size="max price", color="location")
                #hover_name="location")
fig.show()


#fig = px.scatter(df2, x="price", y="bed", color="location",
 #                 hover_data=['location'])

fig =px.sunburst(df,names=df['location'],parents= df['island'],values=df['price'],)

#fig.show()

#fig =px.sunburst(df,path = ['island','location'],values='price',)


data = dict(character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
 	parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
 	value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig =px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()  



df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/location and price.csv')

#print(df.head())
#df1 = df.dropna()
#df['price'] = round(df['price']/1000000,2)
#dff = df.groupby(['location','area'])['price'].sum().reset_index()
#df1 = dff.groupby(['location'])['price'].sum().reset_index()
#df2 = df.groupby(['location','bed','bath'])['price'].median().reset_index()
df2 = df.head(3)

fig = px.scatter(df2, x="average price", y="count",
	         size="max price", color="location")



df = pd.read_csv('C:/Users/aoluleye001/Desktop/Learning/COUSERA/Data_and_Analytics/Python/Dash/dash sample/datasets/location and price.csv')

fig = px.scatter(df2, x="average price", y="count",
	         size="max price", color="location")	         




'aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
             'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
             'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
             'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
             'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
             'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
             'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
             'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
             'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
             'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
             'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
             'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
             'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
             'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
             'ylorrd']