import customtkinter as tk
import customtkinter
from PIL import Image, ImageTk
import string
import random
import pyperclip
from tkinter import messagebox
import tkinter


def generate_password():
    password_len = int(l_entry.get())

    password_chars = string.ascii_letters
    if include_numbers.get():
        password_chars += string.digits
    if include_sp_chars.get():
        password_chars += '!@#$%^&*'

    password = ''.join(random.choice(password_chars)
                       for i in range(password_len))

    password_label.configure(text=password)


def copy_password():
    password = password_label.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied",
                        "The password has been copied to the clipboard.")


root = tk.CTk()
root.title("Password Generator")
root.geometry("700x450")
root.resizable(False, False)
# root.configure(fg_color="white")
customtkinter.set_default_color_theme("blue")

side = tk.CTkImage(Image.open(
    "C:/Users/SAHIL/OneDrive/Documents/Python/Oasis Infobyte/Password Generator/Images/PasswrdGen.jpg"), size=(350, 450))
side_image = tk.CTkLabel(root, image=side, text="",
                         bg_color="red", fg_color="orange")
side_image.place(x=2, y=2, bordermode='outside')

l_label = tk.CTkLabel(root, text="Password length: ",
                      font=("Arial", 14), justify="right")
l_label.place(x=470, y=45)

l_entry = tk.CTkEntry(root, font=("Arial", 14), width=210, border_width=1.5, border_color="yellow")
l_entry.place(x=420, y=90)

include_numbers = tk.BooleanVar()
number_check = tk.CTkCheckBox(root, text="Include numbers", font=(
    "Arial", 14), variable=include_numbers)
number_check.place(x=450, y=140)

include_sp_chars = tk.BooleanVar()
sp_check = tk.CTkCheckBox(root, text="Include special characters", font=(
    "Arial", 14), variable=include_sp_chars)
sp_check.place(x=430, y=190)

generate_button = tk.CTkButton(root, text="Generate Password", font=(
    "Arial", 14), command=generate_password)
generate_button.place(x=460, y=240)

# frame = tk.CTkFrame(root, width=170, height=50,
#                     corner_radius=15, border_color="yellow", border_width=1.5)
# frame.place(x=450, y=295)

password_label = tk.CTkLabel(
    root, text="", font=("Arial", 16), text_color="white", corner_radius=10)
password_label.place(x=460, y=300)

copy_button = tk.CTkButton(root, text="Copy Password", font=(
    "Arial", 14), command=copy_password)

copy_button.place(x=460, y=360)

root.mainloop()
