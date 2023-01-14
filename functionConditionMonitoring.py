from collections import deque


def ConditionMonitoring(t, x1):
    max_length = 50
    Date = deque(maxlen=max_length)
    freq = deque(maxlen=max_length)

    Date.append(t)
    freq.append(x1)

    if 3.5 > max(freq) < 4 and 0 > max(freq) < 1:
        output_freq = "Warnung (Gelb)"
        color = "yellow"
    elif 4 >= max(freq) and 0 <= max(freq):
        output_freq = "Kritischer Zustand (Rot)"
        color = "red"
    else:
        output_freq = "In Ordnung (Grün)"
        color = "green"

    return output_freq, color
