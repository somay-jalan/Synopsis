from tkinter import *


def btn_clicked():
    print(entry.get())


window = Tk()

window.geometry("800x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


entry = Entry(
    bd = 0,
    bg = "#9c9797",
    highlightthickness = 0)

entry.place(
    x = 230.0, y = 450,
    width = 365.0,
    height = 35)

img = PhotoImage(file = f"img0.png")
b = Button(
    image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b.place(
    x = 332, y = 509,
    width = 135,
    height = 40)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
