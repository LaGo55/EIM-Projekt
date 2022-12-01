def main():
    import serial
    import datetime as dt
    import turtle

    import getArdData as gAD
    import DataFrame as DCDf
    import DataToCSV as DB
    import functionConditionMonitoring as fCM
    import Ampel
    import GUI
    import test1

    DB # Initialisiere Database

    i = 0
    com = "com6"
    ArduinoData = serial.Serial(com, 9600)
    GUI

    while True:
        df = test1.handover(ArduinoData,i)
        GUI.GUI((df))

if __name__ == '__main__':
    main()

