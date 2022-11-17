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
csv = pd.DataFrame()
x_values = []
y_values = []

def monitoring(csv):
    with open("data.csv", "r") as ll:
        last_line = ll.readlines()[-1]
    csv = csv.append(last_line, ignore_index=True)

    if len(csv)>50:
        csv = csv.drop()[-1]

    return csv



def animate(k):
    data = pd.read_csv('data.csv')
    x = data["Time"]
    y1 = data["Data_1"]
    y2 = data["Data_2"]
    plt.cla()
    plt.plot(x, y1, y2, linestyle='-')

    # ax.legend(["Frequency"])
    # ax.set_xlabel("Time")
    # ax.set_ylabel("Live Sensor Data")
    plt.title('Live Sensor Data')

#while True:

    #monitoring(csv)


ani = FuncAnimation(plt.gcf(), animate, interval=500)
plt.tight_layout()
plt.show()

# i = 1
# graph = pd.DataFrame(columns=('Time','Data'))
# df = pd.DataFrame(columns=('Time','Data'))
# df1 = pd.DataFrame()



# while True: #While Schleife, die immer durchläuf
#
#
#     while (ArduinoData.inWaiting()==0):
#         pass #Mache nichts, wenn keine Daten da sind
#     while i <= 100:
#         arduinoPacket = ArduinoData.readline()
#         arduinoString = str(arduinoPacket, 'utf-8')
#         arduinoString = arduinoString.strip('\r\n')
#         frequency = float(arduinoString)
#         TM = dt.datetime.now()
#              df['Time'] = pd.DataFrame([TM])
#     #         df1['Data'] = pd.DataFrame([frequency])
#     #
#     #         df['Time'] = pd.to_datetime(df['Time'], format="%Y-%d-%m %H:%M:%S")
#     #         df = pd.concat([df,df1], ignore_index=True)
#     #         #y = df['Data'].iloc[-1]
#     #         #x = df['Time'].iloc[-1]
#
#         i += 1








