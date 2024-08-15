import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "49f4c9e7e6f88bcd24a0286fdc250b72"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        message = f'Temperature: {temperature}°C\nWeather: {weather_desc.capitalize()}'
        messagebox.showinfo('Weather Forecast', message)
    else:
        messagebox.showerror('Error', 'City not found. Please check the spelling.')

# Create the GUI
root = tk.Tk()
root.title('Weather Forecast by Mithlesh')
root.geometry("400x200")

# Label and Entry for City Input
city_label = tk.Label(root, text='Enter City:' , font=('Book Antiqua', 15, 'bold'))
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Button to Get Weather Forecast
get_weather_button = tk.Button(root, text='Get Weather', command=get_weather, font=('Book Antiqua', 10, 'bold'), bg = "Lightgreen")
get_weather_button.pack()

root.mainloop()