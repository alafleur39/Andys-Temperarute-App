import tkinter as tk
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser 
from tkinter import Entry, StringVar, Button, Label
import requests

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def get_the_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        temp_farenheit = (temp_kelvin-273.15) * 9 / 5 +32
        icon = json['weather'][0]['icon']
        weather1 = json['weather'][0]['main']
        final = (city, country, temp_kelvin,  
                 temp_celsius,temp_farenheit,icon, weather1) 
        return final
    else:
        print("NO content found")

def search_function():
    city = weather_city_text.get()
    weather = get_the_weather(city)

    if weather:
        location_label['text']='{},{}'.format(weather[0],weather[1])
        temperature_label['text']= str(weather[3])+" Degree Celsius and Farenheit below"
        weather_1['text']=weather[4]
        image['bitmap']= 'weatherappicons/{}.png'.format(weather[4])
    else:
        messagebox.showerror('Error',"Cannot find {}".format(city))

main_window_root = tk.Tk()

# Configure the main window
main_window_root.configure(bg="lightblue")  # Set background color to light blue
main_window_root.geometry("1200x800")        # Set window size

# Create and pack widgets
label = tk.Label(main_window_root, text="Andy's Temperature App", bg="lightblue", justify="center", wraplength=200,
                 font=('Arial', 18, 'bold'), fg='black')  # Corrected font name to 'Arial'
label.pack(padx=40, pady=40)

weather_city_text = StringVar()
weather_city_entry = Entry(main_window_root, textvariable=weather_city_text)
weather_city_entry.pack()

Search_button = Button(main_window_root, text="Search Weather", width=12, bg="lightblue",
                       font=('Arial', 18, 'bold'), fg='black', command=search_function)
Search_button.pack()

location_label = Label(main_window_root, text="Location", bg="lightblue",
                       font=('Arial', 18, 'bold'), fg='black')
location_label.pack()

image = Label(main_window_root,text='')
image.pack()

temperature_label = Label(main_window_root, text="", bg="lightblue",
                          font=('Arial', 18, 'bold'), fg='black')
temperature_label.pack()

weather_1 = Label(main_window_root, text="")
weather_1.pack()

# Start the main event loop
main_window_root.mainloop()
