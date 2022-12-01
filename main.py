def main():
    import datetime as dt
    import serial
    from collections import deque

    import getArdData as gAD
    import DataToCSV as DB
    import functionConditionMonitoring as fCM
    import UserInterface

    i = 0
    com = "com6"  # Arduino Port
    ArduinoData = serial.Serial(com, 9600)  # Arduino Port und Bau-Rate

    DB # Initialisiere Database
    UserInterface

    color_list = deque(maxlen=10) # Initialisierte Liste für die Historie
    color_list.append('green')
    color_list.append('green')


    while True:
        try:
            while (ArduinoData.inWaiting() == 0):
                pass
            x_value = dt.datetime.now()
            sens1,sens2 = gAD.getArdData(ArduinoData)
           # df, i = DCDf.DataFrame(x_value, sens1, sens2, i)
            DB.CreateDataBase(x_value,sens1,sens2)
            out1, out2, statuscolor = fCM.ConditionMonitoring(x_value, sens1, sens2)
        except ValueError or IndexError:
            pass
    color_list.append(color)

    if color_list[-1] == 'green' and color_list[-2] == 'green':
        pass
    elif color_list[-1] == 'green' and color_list[-2] != 'green':
        hist.write_history(x_value, out1)
    elif color_list[-1] == 'yellow' and color_list[-2] == 'yellow':
        pass
    elif color_list[-1] == 'yellow' and color_list[-2] != 'yellow':
        hist.write_history(x_value, out1)
    elif color_list[-1] == 'red' and color_list[-2] == 'red':
        pass
    elif color_list[-1] == 'red' and color_list[-2] != 'red':
        hist.write_history(x_value, out1)
    else:
        pass

if __name__ == '__main__':
    main()

