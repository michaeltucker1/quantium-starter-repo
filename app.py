from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("daily_sales_data.csv")

line_chart = px.line(df, x='date', y='Sales')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H1(
        children='Sales of Pink Morsel',
        style={
            'textAlign': 'center',
            'color': 'black'
        }
    ),

    dcc.Graph(
        id='salesGraph'
    ),

    html.Div([
        dcc.RadioItems(id="region", options=[
            {'label':'North', 'value':'North'},
            {'label':'East', 'value':'East'},
            {'label':'South', 'value':'South'},
            {'label':'West', 'value':'West'},
            {'label':'All Regions', 'value':'All Regions'},
        ], value='All Regions'),
        
    ], style={
        
        'textAlign': 'center',
        'fontSize' : '20px',
        })
])

@app.callback(
    Output(component_id='salesGraph', component_property='figure'),
    [Input(component_id='region', component_property='value')]
)

def updateGraph (value):
    if value == 'All Regions':
        fig = px.line(df, x='date', y='Sales')
        return fig
    if value == "North":
        dfNorth = pd.read_csv("daily_sales_data.csv")
        dfNorth.drop(df[df['region'] != "north"].index, inplace = True)
        fig = px.line(dfNorth, x='date', y='Sales')
        return fig
    if value == "East":
        dfEast = pd.read_csv("daily_sales_data.csv")
        dfEast.drop(df[df['region'] != "east"].index, inplace = True)
        fig = px.line(dfEast, x='date', y='Sales')
        return fig
    if value == "South":
        dfSouth = pd.read_csv("daily_sales_data.csv")
        dfSouth.drop(df[df['region'] != "south"].index, inplace = True)
        fig = px.line(dfSouth, x='date', y='Sales')
        return fig
    if value == "West":
        dfWest = pd.read_csv("daily_sales_data.csv")
        dfWest.drop(df[df['region'] != "west"].index, inplace = True)
        fig = px.line(dfWest, x='date', y='Sales')
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)