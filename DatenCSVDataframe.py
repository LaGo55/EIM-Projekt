import datetime as dt
import serial
import pandas as pd
import time

i=0
arduinoData = serial.Serial("com4", 9600)
time.sleep(.01)
df = pd.DataFrame(columns=['Time', 'Frequency', 'Temperature'])

while True:
        while (arduinoData.inWaiting()==0):
            pass
        x_value = dt.datetime.now()
        arduinoPacket = arduinoData.readline()
        arduinoString = str(arduinoPacket, 'utf-8')
        arduinoString = arduinoString.strip('\r\n')
        splitString = arduinoString.split(',')
        Freq = splitString[0]
        Temp = splitString[1]
        Freq = float(Freq)
        Temp = float(Temp)
        df_new_row = pd.DataFrame({'Time': [x_value], 'Frequency': [Freq], 'Temperature': [Temp]})
        df = pd.concat([df, df_new_row])
        df = df.reset_index(drop=True)
        i=i+1
        print(df)
        df.to_csv('csv.csv',index=False)
        if i > 20:
            df = df.iloc[1:]