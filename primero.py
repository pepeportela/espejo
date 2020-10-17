from tkinter import *


def click_btn():
    lbl.configure(text="CLICKED")


window = Tk()
window.title("Bienvenido")
lbl = Label(window, text="Hola", font=("Arial Bold", 50), bg="light blue")
lbl.grid(column=0, row=0)
window.attributes('-fullscreen', True)
btn = Button(window, text="Click Me", command=click_btn)
btn.grid(column=1, row=0)
window.mainloop()
