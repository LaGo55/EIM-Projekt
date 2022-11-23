
from collections import deque

def ConditionMonitoring(t,x1,x2):

    max_length = 50
    Date = deque(maxlen=max_length)
    freq = deque(maxlen=max_length)
    temp = deque(maxlen=max_length)

    Date.append(t)
    freq.append(x1)
    temp.append(x2)

    if 80 < max(freq) < 100:
        output_freq = print("Die Amplitude der Frequenz nimmt zu (Gelb)")
        color = "yellow"
    elif 100 >= max(freq) < 105:
        output_freq = print("Die Amplitude der Frequenz ist zu groß (Rot)")
        color = "red"
    elif max(freq) >=120:
        output_freq = print("Kritischer System Zustand!")
        return (output_freq)
        color = "red"
    else:
        output_freq = print("Die Amplitude der Frequenz ist in Ordnung (Grün)")
        color = "green"
    if 20 < max(temp) < 23:
        output_temp = print("Die Temperatur nimmt zu (Gelb)")
    elif max(temp) >= 23:
        output_temp = print("Die Temperatur ist zu hoch (Rot)")
    else:
        output_temp = print("Die Temperatur ist in Ordnung (Grün)")

    return(output_freq,output_temp,color)