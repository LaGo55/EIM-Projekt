# Benötigte Imports durchführen
# Standard Funktionen
import pandas as pd
import datetime as dt
import serial

# Dash / GUI Funktionen
import dash
from dash import dcc, html, dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SLATE])

colors = {
    'background': '#708090',
    'text': '#7FDBFF'
}

df = pd.read_csv('data.csv').tail(25)
df1 = pd.read_csv('history.csv').tail(50)
statuscolor = '#7CFC00'

## Definition der HTML Content Elemente für das Layout

tab2 = html.Div(id='Diagram-Status',style={
            'width':'1200px',
            'text-align': 'center',
            'horizontal-align':'middle',
            'color': colors['text'],
            'display':'inline-block'},
            children=[
                dbc.Col(
                dbc.Card(dbc.CardBody([dcc.Graph(id='live-graph',
                        style={
                        'display':'inline-block'})]))
                    )])

ind1 = [html.Div(id='traffic', style={'display':'inline-block'}, children=
    dbc.Col(
    dbc.Card(
        dbc.CardBody([
                    html.Div(id='status-image', children=[html.Div(style = {'background-image': 'url("/static/ok.jpg")',
                          'background-repeat': 'no-repeat',
                          'background-size': 'auto'
                          })]),
                    html.Div(dcc.Interval(id='update-status',
                            interval=50, # 1s
                            n_intervals=0))]
        ))
))]

table1 = html.Div(id='Table-Content', children=[
    html.H3('Daten Tabelle',style={'text-align':'center'}),
    dash_table.DataTable(id='Data-Overview',

        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_table={'width':'90%',
               'margin-left':'10',
               'margin-right':'10',
               'top':'50',
               'component-align':'center'
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

table2 = html.Div(id='Table-Content2', children=[
    html.H3('Fehler-Historie', style={'text-align':'center'}),
    dash_table.DataTable(id='Data-Overview1',

        data=df1.to_dict('records1'),
        columns=[{'id': c, 'name': c} for c in df1.columns],
        style_table={'width':'90%',
               'margin-left':'10',
               'margin-right':'10',
               'top':'50',
               'component-align':'center'
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

content1= html.Div([
    dbc.Card(dbc.CardBody([dbc.Row(html.H1('Live Data Feed',style={'text-align':'center'}),align='center'),
            dbc.Row([
                dbc.Col(tab2,width=8),
                dbc.Col(width=1),
                dbc.Col(ind1,width=2)],
            align='center')]))
            ])
content2 = html.Div([
            dbc.Card(dbc.CardBody([
                dbc.Row(html.H1('Fehler Historie',style={'text-align':'center'}),align='center'),
                dbc.Row(table2, style={'margin-left':'50','component-align':'center'}),
                dbc.Row(table1, style={'margin-left':'50','component-align':'center'})]))])


app.layout = html.Div(
    html.Div(id='content1', style={'backgroundColor': colors['background']},
            children=[dbc.Card(
                dbc.CardBody(children=[
            dbc.Row(dcc.Tabs(id='tab-selection',value='Diagram Status',children=[
                    dcc.Tab(label='Live Diagramm', value='Diagram Status'),
                    dcc.Tab(label='Fehler-Historie',value='Table-Content')
                    ])),
            dbc.Row(html.Div(id='tabs-content')),
            dcc.Interval(
                id='interval-component',
                interval=1000,  # 1s
                n_intervals=0)]
            ))
            ]
             )
)

## Callbacks für das interaktive Updaten der HTML Elemente
@app.callback(
    Output('tabs-content','children'),
    Input('tab-selection','value'))
def tabcontent(tab):
    if tab=='Diagram Status':
        return html.Div([content1])
    elif tab=='Table-Content':
        return html.Div([content2])

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
        margin={'l':80,'r':50,'t':45,'b':1},
        width=1000,
        plot_bgcolor='#888888',
        transition_easing='sin-in-out'
        )

    # Hinzufügen der Mittellinie und oberen/unteren Grenzen
    fig.add_hline(y=100, line_color='Green')
    fig.add_hline(y=80, line_dash='dash',line_color='red')
    fig.add_hline(y=120, line_dash='dash', line_color='red')
    return fig

# Callback zum interaktiven Updaten der Tabelle mit der Daten-Übersicht
@app.callback(
    Output('Data-Overview','data'),
    Output('Data-Overview1','data1'),
    Input('interval-component','n_intervals')) #Update nach dem im Layout definierten 'Interval'
def table_update(n):
    df = pd.read_csv('data.csv').tail(25)   #Einlesen der letzen 25 Werte der data.csv Datei
    data=df.to_dict('records')               #Umwandeln des Dataframes in ein Dictionary

    df1 = pd.read_csv('history.csv').tail(50) # Einlesen der letzen 50 Werte der data.csv Datei
    data1 = df1.to_dict('records1')  # Umwandeln des Dataframes in ein Dictionary

    return [data,data1]                             #Übergabe an Layout Element

@app.callback(
    Output('traffic','children'),
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