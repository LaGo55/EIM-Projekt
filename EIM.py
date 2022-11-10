import serial
import numpy
import matplotlib
import pandas as pd
import datetime as dt

arduinoData = serial.Serial("com3", 9600)
df = pd.DataFrame(columns=['time','frequency'])
print(df)

while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    frequency = pd.Series(arduinoString[1])
    df['time'] = dt.datetime.now()
    df['frequency'] = frequency
    print(df)
    

