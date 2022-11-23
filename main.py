
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



