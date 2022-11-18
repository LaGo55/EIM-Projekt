import csv
import pandas as pd
import time
import serial
import datetime as dt

x_value = dt.datetime.now()
sensor_data_1 = 0
sensor_data_2 = 0
sensor_data_3 = 0

fieldnames = ["Time","Data_1","Data_2"]  #,"Data_3"

i=0
ArduinoData = serial.Serial("com6", 9600)


with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
    csv_writer.writeheader()

while True: #While Schleife, die immer durchläuf
    while (ArduinoData.inWaiting()==0):
        pass #Mache nichts, wenn keine Daten da sind
    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames, dialect="excel")
        info = {
            "Time": x_value,
            "Data_1": sensor_data_1,
            "Data_2": sensor_data_2,
           # "Data_3": sensor_data_3
                }
        csv_writer.writerow(info)
        print(x_value, sensor_data_1,sensor_data_2)

    # with open('data.csv') as input, open('data.csv', 'w', newline='') as output:
    #     writer = csv.writer(output)
    #     for row in csv.reader(input):
    #         if any(field.strip() for field in row):
    #             writer.writerow(row)

    arduinoPacket = ArduinoData.readline()
    arduinoString = str(arduinoPacket, 'utf-8')
    arduinoString = arduinoString.strip('\r\n')
    arduinoString = arduinoString.split(",")
    sensor_data_1 = float(arduinoString[0])
    sensor_data_2 = float(arduinoString[1])
    x_value = dt.datetime.now()

    # df1['Time'] = pd.DataFrame([TM])
    # df1['Data'] = pd.DataFrame([frequency])
    # df['Time'] = pd.to_datetime(df['Time'], format="%Y-%d-%m %H:%M:%S")
    # df = pd.concat([df,df1], ignore_index=True)
    i = i+1