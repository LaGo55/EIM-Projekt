import dash
import pandas as pd
from collections import deque
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import time
import plotly.graph_objs as go
import DataToCSV as DTC

app = dash.Dash('Riemen Live Date')

t = deque(maxlen=50)
y1 = deque(maxlen=50)
y2 = deque(maxlen=50)
data_dict ={"Date": t,
            "Freq": y1,
            "Temp": y2}
def update_graph_data(t,y1,y2):
    t.append(DTC.x_value)
    y1.append(DTC.sensor_data_1)
    y2.append(DTC.sensor_data_2)
    return t,y1,y2

t, y1, y2 = update_graph_data(t,y1,y2)

app.layout = html.Div([
    html.Div([
        html.H2('Riemen Live Daten',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['Date','freq','temp']
                 ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    dcc.Interval(
        id='graph-update',
        interval=100,
        n_intervals=0
        ),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


@app.callback(
    Output('graphs','children'),
    Input('data-name','graph-update')
    )
def update_graph(data_names):
    graphs = []
    update_graph_data(y1, y2)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for data_name in data_names:

        data = go.Scatter(
            x=list(t),
            y=list(data_dict[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(t),max(t)]),
                                                        yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(data_name))}
            ), className=class_choice))

    return graphs



external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
    app.scripts.append_script({'external_url': js})
if __name__ == '__main__':
    app.run_server(debug=True)


