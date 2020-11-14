# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from weather_view import weather_view
from home_view import home_view

views = {
    "0": weather_view,
    "1": home_view
}
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def change_view(event):
    func = views[event.char]
    for widget in frame_aux.winfo_children():
        widget.destroy()
    frame_ret = func(frame_aux)
    frame_ret.pack(fill="both", expand=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.title("Bienvenido")
    #window.attributes('-fullscreen', True)
    window.configure(bg="black")
    frame_aux = Frame(window)
    frame_aux.configure(bg="black")
    window.bind("<Key>", change_view)

    window.mainloop()

