import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *

root = Tk()
root.title("BMI Calculator")
root.geometry("500x600+350+250")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h/100
    bmi = round(float(w/m**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight then \n normal body!")

    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="It indicates that you are healthy!")

    elif bmi > 25 and bmi <= 30:
        label2.config(text="OverWeight!")
        label3.config(
            text="It indicates that a person is \n slightly overweight!")

    else:
        label2.config(text="Obes!")
        label3.config(
            text="Health may be at risk, if they do not \n lose weight!")


image_icon = PhotoImage(
    file="C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/BMI Calculator/Images/icon.png")
root.iconphoto(FALSE, image_icon)

top = PhotoImage(
    file="C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/BMI Calculator/Images/top.png")
top_image = Label(root, image=top, background="orange")
top_image.place(x=2, y=6)

Label(root, width=72, height=18, bg="orange").pack(side=BOTTOM)

box = PhotoImage(
    file="C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/BMI Calculator/Images/box.png")
Label(root, image=box).place(x=30, y=100)
Label(root, image=box).place(x=260, y=100)

Scale = PhotoImage(
    file="C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/BMI Calculator/Images/scale.png")
Label(root, image=Scale, bg="orange").place(x=15, y=330)

current_v = tk.DoubleVar()


def get_current_v():
    return '{: .2f}'.format(current_v.get())


def slider_changed(event):
    Height.set(get_current_v())

    size = int(float(get_current_v()))
    img = (Image.open(
        "C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/BMI Calculator/Images/man.png"))
    resized_image = img.resize((50, 5+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2, bg="orange")
    secondimage.place(x=70, y=570-size)
    secondimage.image = photo2


style = ttk.Style()
style.configure("TScale", background="White")
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal",
                   style="TScale", command=slider_changed, variable=current_v)
slider.place(x=80, y=250)


current_v2 = tk.DoubleVar()


def get_current_v2():
    return '{: .2f}'.format(current_v2.get())


def slider_changed2(event):
    Weight.set(get_current_v2())


style2 = ttk.Style()
style2.configure("TScale", background="White")
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal",
                    style="TScale", command=slider_changed2, variable=current_v2)
slider2.place(x=320, y=250)

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50',
               bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=43, y=160)
Height.set(get_current_v())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50',
               bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=273, y=160)
Weight.set(get_current_v2())

secondimage = Label(root, bg="lightyellow")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold",
       bg="#1f6e68", fg="White", command=BMI).place(x=280, y=350)
label1 = Label(root, font="arial 50 bold", bg="orange", fg="#fff")
label1.place(x=270, y=400)

label2 = Label(root, font="arial 25 bold", bg="orange", fg="#3b3a3a")
label2.place(x=290, y=480)

label3 = Label(root, font="arial 10 bold", bg="orange")
label3.place(x=240, y=520)

root.mainloop()
