
import serial
import datetime as dt
import turtle

import getArdData as gAD
import DataFrame as DCDf
import DataToCSV as DB
import functionConditionMonitoring as fCM
import Ampel

from multiprocessing import Process

DB # Initialisiere Database

color_list = deque(maxlen=10) # Initialisierte Liste für die Historie
color_list.append('green')
color_list.append('green')

i = 0
com = "com6"
ArduinoData = serial.Serial(com, 9600)
green_light = turtle.Turtle()
yellow_light = turtle.Turtle()
red_light = turtle.Turtle()
color = "green"
wn = turtle.Screen()
Ampel.init_ampel(wn,color)
while True:
    Ampel.init_ampel(wn, color)
    wn.listen()
    while (ArduinoData.inWaiting() == 0):
        pass
    x_value = dt.datetime.now()
    sens1,sens2 = gAD.getArdData(ArduinoData)
    df, i = DCDf.DataFrame(x_value, sens1, sens2, i)
    DB.CreateDataBase(x_value,sens1,sens2)
    out1, out2, color = fCM.ConditionMonitoring(x_value, sens1, sens2)  # t,y1,y2
    color_list.append(color)

    if color_list[-1] == 'green' and color_list[-2] == 'green':
        pass
    elif color_list[-1] == 'green' and color_list[-2] != 'green':
        hist.write_history(x_value, out1, out2)
    elif color_list[-1] == 'yellow' and color_list[-2] == 'yellow':
        pass
    elif color_list[-1] == 'yellow' and color_list[-2] != 'yellow':
        hist.write_history(x_value, out1, out2)
    elif color_list[-1] == 'red' and color_list[-2] == 'red':
        pass
    elif color_list[-1] == 'red' and color_list[-2] != 'red':
        hist.write_history(x_value, out1, out2)
    else:
        pass


