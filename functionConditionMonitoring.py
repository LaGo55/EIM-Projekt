import pandas as pd

csv = 'csv.csv'

def ConditionMonitoring(csv):

    colnames = ['time','freq','temp']
    df = pd.read_csv(csv,sep=';',names=colnames)

    time = df['time'].tolist()
    freq = df['freq'].tolist()
    temp = df['temp'].tolist()

    if 80 < max(freq) < 100:
        output_freq = print("Die Amplitude der Frequenz nimmt zu (Gelb)")
    elif max(freq) >= 100:
        output_freq = print("Die Amplitude der Frequenz ist zu groß (Rot)")
    else:
        output_freq = print("Die Amplitude der Freuqenz ist in Ordnung (Grün)")

    if 20 < max(temp) < 23:
        output_temp = print("Die Temperatur nimmt zu (Gelb)")
    elif max(temp) >= 23:
        output_temp = print("Die Temperatur ist zu hoch (Rot)")
    else:
        output_temp = print("Die Temperatur ist in Ordnung (Grün)")

    return(output_freq,output_temp)

ConditionMonitoring(csv)