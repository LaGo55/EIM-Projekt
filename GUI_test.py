import dash
from collections import deque
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import csv
import serial
import datetime as dt
import functionConditionMonitoring as fCM

app = dash.Dash('Riemen Live Date')

t = deque(maxlen=50)
y1 = deque(maxlen=50)
y2 = deque(maxlen=50)
data_dict ={"Date": t,
            "Freq": y1,
            "Temp": y2}
def update_graph_data(t,y1,y2):
    com = 'com6'
    ArduinoData = serial.Serial(com, 9600)

    x_value = dt.datetime.now()

    sensor_data_1 = 0
    sensor_data_2 = 0
    fieldnames = ["Time", "Data_1", "Data_2"]  # ,"Data_3"

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
        csv_writer.writeheader()

    while (ArduinoData.inWaiting() == 0):
        pass  # Mache nichts, wenn keine Daten da sind
    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
        info = {
            "Time": x_value,
            "Data_1": sensor_data_1,
            "Data_2": sensor_data_2,
            # "Data_3": sensor_data_3
        }
        csv_writer.writerow(info)

    arduinoPacket = ArduinoData.readline()
    arduinoString = str(arduinoPacket, 'utf-8')
    arduinoString = arduinoString.strip('\r\n')
    arduinoString = arduinoString.split(",")
    sensor_data_1 = float(arduinoString[0])
    sensor_data_2 = float(arduinoString[1])
    x_value = dt.datetime.now()

    fCM.ConditionMonitoring(x_value, sensor_data_1, sensor_data_2)

    t.append(x_value)
    y1.append(sensor_data_1)
    y2.append(sensor_data_2)
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
    Output('graphs', 'children'),
    Input('data-name', 'graph-update')
    )
def update_graph(data_names):
    graphs = []
    update_graph_data(t,y1, y2)
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


