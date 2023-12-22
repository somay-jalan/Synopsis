from tkinter import *


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file = f"backgroundgenpasswrdscreen.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"img3.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 24, y = 547,
    width = 136,
    height = 37)

img1 = PhotoImage(file = f"img1genpasswrdscreen.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 324, y = 451,
    width = 150,
    height = 42)

img2 = PhotoImage(file = f"img2genpasswrdscreen.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 479, y = 547,
    width = 314,
    height = 41)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    203.0, 415.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 58.0, y = 399,
    width = 290.0,
    height = 30)



entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 458.0, y = 399,
    width = 290.0,
    height = 30)

window.resizable(False, False)
window.mainloop()
