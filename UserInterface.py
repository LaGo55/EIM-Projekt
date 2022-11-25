import datetime
import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Header('Live Data'),
    html.Div(id='live-text-update'),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1000, # 1s
        n_intervals=0
    )]
)

@app.callback(
    Output('live-graph','figure'),
    Input('interval-component','n_intervals'))
def graph_update(n):

    v = 30
    header = ['Time', 'Data_1','Data_2']
    df = pd.read_csv('data.csv',names=header, skiprows=1)
    time = pd.Series(df['Time'].tail(v))
    freq = pd.Series(df['Data_1'].tail(v))

    dict = {'x':time, 'y':freq}

    return go.Figure({'x':time,
                      'y':freq})
            # xaxis = dict(range = [min(time), max(time)],
            #              title = '<b>Time</b>',
            #              color = 'black',
            #              showline = True,
            #              showgrid = False,
            #              linecolor = 'black',
            #              linewidth = 1,
            #              ticks = 'outside',
            #              tickfont = dict(
            #                  family = 'Arial',
            #                  size = 12,
            #                  color = 'black')
            #
            #              ),
            #
            # yaxis = dict(range = [min(freq) - 20, max(freq) + 20],
            #              title = '<b>Temperature</b>',
            #              color = 'black',
            #              showline = True,
            #              showgrid = True,
            #              linecolor = 'black',
            #              linewidth = 1,
            #              ticks = 'outside',
            #              tickfont = dict(
            #                  family = 'Arial',
            #                  size = 12,
            #                  color = 'black')
            #
            #              )
app.run_server(debug=True)