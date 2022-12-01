# Skript zum initialisieren der benötigten Variablen

import serial

i = 0
com = "com6"    #Arduino Port
ArduinoData = serial.Serial(com, 9600) #Arduino Port und Bau-Rate
statuscolor = "#7CFC00"  #hellgrün