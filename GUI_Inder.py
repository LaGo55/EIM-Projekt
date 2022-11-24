import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial as sr

data = np.array([])
cond = False

def plot_data():
    global cond, data

    if (cond == True):
        a = s.readline()
        a.decode()

        if(len(data) < 10):
            data = np.append(data,float(a[0:4]))
        else:
            data[0:9] = data[1:10]
            data[9] = float(a[0:4])

        lines.set_xdata(np.arange(0,len(data)))
        lines.set_ydata(data)

        canvas.draw()

    root.after(1,plot_data)

root = tk.Tk()
root.title('Real Time Plot')
root.configure(background = 'light blue')
root.geometry("650x550")

fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Serial Data')
ax.set_xlabel('Zeit')
ax.set_ylabel('Frequenz')
ax.set_xlim(0,10)
ax.set_ylim(80,120)
lines = ax.plot([],[])[0]

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x = 10,y = 10, width = 500, height = 400)
canvas.draw()

def plot_start():
    global cond
    cond = True
    s.reset_input_buffer()

def plot_stop():
    global cond
    cond = False

root.update()
start = tk.Button(root, text = "Start", font = ('calbiri',12),command = lambda:plot_start())
start.place(x = 100, y = 450)

root.update()
stop = tk.Button(root, text = 'Stop', font = ('calibiri',12), command = lambda:plot_stop())
stop.place(x = start.winfo_x()+start.winfo_reqwidth()+20, y = 450)

s = sr.Serial('COM4',115200)
s.reset_input_buffer()

root.after(1,plot_data)
root.mainloop()