from tkinter import *


def weather_view(frame):
    print("weather")
    lbl = Label(frame, text="El tiempo", font=("Arial Bold", 50), bg="black", fg="white")
    lbl.grid(column=0, row=0)
    lbl2 = Label(frame, text="22ºC", font=("Arial Bold", 50), bg="black", fg="white")
    lbl2.grid(column=1, row=0)
    return frame
