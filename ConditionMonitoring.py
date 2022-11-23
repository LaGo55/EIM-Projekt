import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import numpy as np
import pandas as pd
import datetime as dt



plt.style.use("fivethirtyeight")
counter = 0
index = count()
csv = 'data.csv'



def monitoring(csv):
    Date = np.array([0])
    ySen1 = np.array([0])
    ySen2 = np.array([0])

    with open(csv, "r") as ll:
        last_line = ll.readlines()[-1]

    dataString = last_line.split(",")
    Date = Date.np.append(dataString[0])
    ySen1 = ySen1.append(dataString[1])
    ySen2 = ySen2.append(dataString[2])

    if Date.size()>50:
        Date = Date.drop()[0]
        ySen1 = ySen1.drop()[0]
        ySen2 = ySen2.drop()[0]

    return Date,ySen1,ySen2



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


#print(monitoring(csv))

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








