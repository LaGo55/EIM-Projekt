import time

def getArdData(x):
    time.sleep(.05)
    arduinoPacket = x.readline()
    arduinoString = str(arduinoPacket, 'utf-8')
    arduinoString = arduinoString.strip('\r\n')
    splitString = arduinoString.split(',')

    sensor_data_1 = float(splitString[0])
    sensor_data_2 = float(splitString[1])
    print(sensor_data_1,sensor_data_2)
    if sensor_data_1 > 500 or sensor_data_2 > 50:
        pass
    return sensor_data_1, sensor_data_2

