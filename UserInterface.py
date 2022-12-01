# Benötigte Imports durchführen
# Standard Funktionen
import pandas as pd
import datetime as dt
from collections import deque
import serial

# Dash / GUI Funktionen
import dash
from dash import dcc, html, dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_bootstrap_components as dbc

# Eigene Funktionen
import functionConditionMonitoring as fCM
import getArdData as gAD
import DataToCSV as DB

app = dash.Dash(__name__)

colors = {
    'background': '#708090',
    'text': '#7FDBFF'
}

df = pd.read_csv('data.csv').tail(25)
statuscolor = '#7CFC00'

## Definition der HTML Content Elemente für das Layout

tab1 = html.Div(className='Tab1')

tab2 = html.Div(className='Diagram-Status',style={
            'textAlign': 'left',
            'horizontal-align':'middle',
            'color': colors['text']},
            children=[dcc.Graph(id='live-graph',
                        style={'margin-left': '50px',
                        'top': '50px',
                        'display':'inline-block'})])

ind1 = [html.Div(id='traffic', children=[
                    html.Div(id='status-image', children=[html.Div(style = {'background-image': 'url("/static/ok.jpg")',
                          'background-repeat': 'no-repeat',
                          'background-size': 'auto'
                          })])]),
        html.Div(dcc.Interval(id='update-status',
                            interval=50, # 1s
                            n_intervals=0))]
                    # daq.Indicator(id='traffic-light',
                    #         color=statuscolor,
                    #         value=False,
                    #         label='Zustand',
                    #         width=125,
                    #         style={'horizontal-align':'middle','vertical-align':'middle','display':'inline-block','float':'middle','text-align':'center'}
                    #        ),
                    # dcc.Interval(id='update-status',
                    #         interval=1000, # 1s
                    #         n_intervals=0)


table1 = html.Div(className='Table-Content', children=[ html.H3('Daten Tabelle'),
    dash_table.DataTable(id='Data-Overview',

        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_table={'width':'90%',
               'margin-left':'10',
               'margin-right':'10',
               'top':'50'
        },
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'width': '20%',
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'},
        style_cell={'height':'auto',
                    'textAlign': 'left'},
        )
    ])


app.layout = html.Div(className='content', style={'backgroundColor': colors['background']},children=[
    html.H1('Live Data Feed',
            style={'float':'middle'}),

    dbc.Row(className='Row',style={'width':'100%'},children=[
        dbc.Col(tab1,style={'width':'20px'}),
        dbc.Col(tab2,style={'width':'600px'}),
        dbc.Col(ind1,style={'margin-left':'50px','margin-bottom':'60px'})]),
    dbc.Row(table1, style={'width':'100%'}),
    dcc.Interval(
        id='interval-component',
        interval=1000, # 1s
        n_intervals=0)

    ])

## Callbacks für das interaktive Updaten der HTML Elemente

#Callback für den Live-Graph
@app.callback(
    Output('live-graph','figure'),
    Input('interval-component','n_intervals'))  #Update nach dem im Layout definierten 'Interval'
def graph_update(n):
    v = 30 #Variable für die Anzahl der anzuzeigenden Datenelemente
    #Defintion des Dataframes aus der data.csv Datei
    header = ['Time', 'Data_1','Data_2']
    df = pd.read_csv('data.csv',names=header, skiprows=1)
    #Extrahieren der Zeit und Frequenz Werte als X/Y Achse
    time = pd.Series(df['Time'].tail(v))
    freq = pd.Series(df['Data_1'].tail(v))

    #Erstellen der Figure mit dash_graphic_objects
    fig = go.Figure(data={'x':time,
                      'y':freq}, layout_yaxis_range=[70,130]) #Übergabe der X-/Y-Werte und Festlegen der Y-Achse
    fig.update_layout(  #Formatierungen des Diagramms
        title='Riemen Status',
        xaxis_title="Zeit",
        yaxis_title="Frequenz",
        legend_title="Frequenz",
        font=dict(
            family="Arial",
            size=18,
            color="Black"
        ),
        margin={'l':50,'r':1,'t':45,'b':1}
    )

    # Hinzufügen der Mittellinie und oberen/unteren Grenzen
    fig.add_hline(y=100, line_color='Green')
    fig.add_hline(y=80, line_dash='dash',line_color='red')
    fig.add_hline(y=120, line_dash='dash', line_color='red')
    return fig

# Callback zum interaktiven Updaten der Tabelle mit der Daten-Übersicht
@app.callback(
    Output('Data-Overview','data'),
    Input('interval-component','n_intervals')) #Update nach dem im Layout definierten 'Interval'
def table_update(n):
    df = pd.read_csv('data.csv').tail(25)   #Einlesen der letzen 25 Werte der data.csv Datei
    data=df.to_dict('records')              #Umwandeln des Dataframes in ein Dictionary
    return data                             #Übergabe an Layout Element

@app.callback(
    Output('status-image','children'),
    Input('update-status','n_intervals'))
def update_status(n):
    dfs = pd.read_csv('data.csv', names = ['Time', 'Data_1','Data_2'], skiprows=1).tail(1)
    freq = dfs['Data_1'].tail(1).iloc[0].astype(float)
    if 120<=freq or freq<=80:
           return [
            html.Img(src=r'assets/kritisch.jpg', alt='image')]
    elif 110 <= freq or freq<=90:
        return [
            html.Img(src =r'assets/vorsicht.jpg',alt='image')]
    else:
        return [
            html.Img(src =r'assets/ok.jpg',alt='image')]


if __name__ == '__main__':
    app.run_server(debug=True)