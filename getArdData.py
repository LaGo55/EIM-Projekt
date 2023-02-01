import time

def getArdData(x):
    try:
        #time.sleep(.05)
        arduinoPacket = x.readline()    # Lesen des Arduino Serial Outputs
        arduinoString = str(arduinoPacket, 'utf-8') # Umwandlung der Arduino Sprache in String
        arduinoString = arduinoString.strip('\r\n') # Entfernen von Umbrüchen
        splitString = arduinoString.split(',') # Aufteilen des Strings bei Komma

        sensor_data_1 = float(splitString[0]) #Speichern des 1. Sensor Werts
        sensor_data_2 = float(splitString[1]) #Speichern des 2. Sensor Werts
        print(sensor_data_1,sensor_data_2)
        if sensor_data_1 > 500 or sensor_data_2 > 50:   # Ausschließen von fehlerhaften Werten
            pass
        else:
            return sensor_data_1, sensor_data_2
    except ValueError or IndexError or TypeError:   # Fehler Minimierung
        pass

