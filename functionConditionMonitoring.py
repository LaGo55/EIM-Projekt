
from collections import deque

def ConditionMonitoring(t,x1):

    max_length = 50
    Date = deque(maxlen=max_length)
    freq = deque(maxlen=max_length)

    Date.append(t)
    freq.append(x1)


    if 80 < max(freq) < 100:
        output_freq = print("Die Amplitude der Frequenz nimmt zu (Gelb)")
        color = "yellow"
    elif 100 >= max(freq) < 105:
        output_freq = print("Die Amplitude der Frequenz ist zu groß (Rot)")
        color = "red"
    elif max(freq) >=120:
        output_freq = print("Kritischer System Zustand!")
        color = "red"
    else:
        output_freq = print("Die Amplitude der Frequenz ist in Ordnung (Grün)")
        color = "green"

    return(output_freq,color)