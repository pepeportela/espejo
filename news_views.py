from tkinter import *


def news_view(frame):
    print("News")
    lbl = Label(frame, text="Noticias del día", font=("", 50))
    lbl.grid(column="0", row="0")
    return frame
