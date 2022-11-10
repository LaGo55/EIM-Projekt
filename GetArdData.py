#import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

import numpy as np
import pandas as pd
import datetime as dt

df[0] = ['Time']
df[1] = ['Sensor Data']
print(df)

# while True:
#
#         df['randNumCol1'] = pd.DataFrame(np.random.uniform(-1, 1, df.shape[0]))
#         df['randNumCol2'] = pd.DataFrame(np.random.normal(-1, 1, df.shape[1]))
#         df['datetime'] = pd.Series([dt.datetime.now()])
#
#
#
#
# def GetSensorData():
#
#     while True: #While Schleife, die immer durchläuft
#         while (arduinoData.inWaiting()==0):
#             pass #Mache nichts, wenn keine Daten da sind
#         df['Sensor Data'] = arduinoData.readline() #Lese Zeile aus dem Arduino Serial port
#         print(arduinoString)
#         dataArray = arduinoString #Wenn Data mit , getrennt wird --> Add: .split(",")
#         frequency = float(dataArray[0])
#         #t = float(dataArray[1])
#         #temperature = float(dataArray[1])   #Wenn mehr Daten eingelesen werden
#         #print frequency #, "," temperature
#         freq.append(frequency)
#         zeit.append(t)
#         drawnow(makeFig) #Update live Grafik
#         plt.pyplot.pause(.000001)
#         cnt = cnt+1
#         if(cnt>50):
#             freq.pop(0)
#             zeit.pop(0)'