# Tkinter window for weather visualization

from tkinter import *
from PIL import ImageTk, Image

path = sys.path[0]
ICONS_PATH = path + "/icons/"


def get_icon():
    img = Image.open(ICONS_PATH + "a01d.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


def weather_view(frame):
    print("weather")
    lbl = Label(frame, text="El tiempo", font=("Arial Bold", 50), bg="black", fg="white")
    lbl.grid(column=0, row=0)
    lbl2 = Label(frame, text="22ºC", font=("Arial Bold", 50), bg="black", fg="white")
    lbl2.grid(column=1, row=0)

    lbl3 = Label(frame, text="PONTEVEDRA", font=("Arial Bold", 50), bg="black", fg="white")
    lbl3.grid(column=0, row=1)
    icon_weather = get_icon()
    img_wea = Label(frame, image=icon_weather, bg="black")
    img_wea.image = icon_weather
    img_wea.grid(column=1, row=1)
    return frame
