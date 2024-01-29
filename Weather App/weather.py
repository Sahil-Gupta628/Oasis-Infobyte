import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
import customtkinter as tkk
import customtkinter


def get_weather(city):
    API_key = "e5f3ea2c40846cc8509d698ef4ffe68e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror('Error', 'city not found')
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city},{country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("980x600")
# root.configure(bg="#ADD8E6")

side = tkk.CTkImage(Image.open(
    "Weather App/night.png"), size=(320, 480))
side_image = tkk.CTkLabel(root, image=side, text="",
                          bg_color="red", fg_color="orange")
side_image.place(x=0, y=0, bordermode='outside')

city_entry = ttkbootstrap.Entry(root, font='Helvetica, 18')
city_entry.place(x=520, y=90)

search_button = ttkbootstrap.Button(
    root, text='Search', command=search, bootstyle='warning')
search_button.place(x=660, y=180)

location_label = tk.Label(root, font='Helvetica, 25')
location_label.place(x=600, y=250)

icon_label = tk.Label(root)
icon_label.place(x=645, y=300)

temperature_label = tk.Label(root, font='Helvetica, 20')
temperature_label.place(x=550, y=400)

description_label = tk.Label(root, font='Helvetica, 20')
description_label.place(x=551, y=440)

root.mainloop()
