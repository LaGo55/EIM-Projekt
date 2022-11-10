import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import time
import pandas as pd
import datetime as dt
from time import sleep


plt.style.use("fivethirtyeight")
counter = 0
index = count()

ax = plt.gca()
x_values = []
y_values = []



i = 1
graph = pd.DataFrame(columns=('Time','Data'))
df = pd.DataFrame(columns=('Time','Data'))
df1 = pd.DataFrame()

ArduinoData = serial.Serial("com6", 9600)

while True: #While Schleife, die immer durchläuf
    def animate(k):

        y = df['Data'].iloc[-1]
        y_values.append(y)
        x = df['Time'].iloc[-1]
        x_values.append(x)
        counter = next(index)

        if counter > 40:
            '''
            This helps in keeping the graph fresh and refreshes values after every 40 timesteps
            '''
            x_values.pop(0)
            y_values.pop(0)
            # counter = 0
            plt.cla()  # clears the values of the graph

        plt.plot(x_values, y_values, linestyle='--')

        ax.legend(["Frequency"])
        ax.set_xlabel("Time")
        ax.set_ylabel("Live Sensor Data")
        plt.title('Live Sensor Data')
        time.sleep(.25)  # keep refresh rate of 0.25 seconds

    while (ArduinoData.inWaiting()==0):
        pass #Mache nichts, wenn keine Daten da sind
    while i <= 100:
        arduinoPacket = ArduinoData.readline()
        arduinoString = str(arduinoPacket, 'utf-8')
        arduinoString = arduinoString.strip('\r\n')
        frequency = float(arduinoString)
        TM = dt.datetime.now()
        df1['Time'] = pd.DataFrame([TM])
        df1['Data'] = pd.DataFrame([frequency])

        df['Time'] = pd.to_datetime(df['Time'], format="%Y-%d-%m %H:%M:%S")
        df = pd.concat([df,df1], ignore_index=True)
        ani = FuncAnimation(plt.gcf(), animate, 1)
        plt.tight_layout()
        plt.show()
        i = i+1
    print(df)







