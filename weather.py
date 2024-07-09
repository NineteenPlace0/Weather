### WEATHER ###
"""V0.5.1: Introduce API -> small tweaks"""


import requests, json
import tkinter as tk


"""Code needed to properly use/integrate API will be temporarily placed here."""
'''#--- will be converted into functions later'''
# Parameters & Information:
"""
# Current weather: https://openweathermap.org/current
# Geocoding API  : https://openweathermap.org/api/geocoding-api
"""

# API Key
api_key = '3294a33bb60c1fa031b89f141c8bfd74'

# URL to API-store ---> "COMPLETE URL", (full_url), REQUIRES USER INPUT (and other variables)
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city = "Florence"   # Placeholder: will be replaced with user input, possibly through 'Geocoding API'

# Complete URL
full_url = base_url + 'appid=' + api_key + '&q=' + city + '&units=metric'
'''Default temperature measurements are in Kelvin.'''

print(full_url)
'''Example: http://api.openweathermap.org/data/2.5/weather?appid=3294a33bb60c1fa031b89f141c8bfd74&q=Florence&units=metric'''
print()
response = requests.get(full_url)

x = response.json()

if x["cod"] != "404":

    # store the value of "main" key in variable y
    y = x["main"]

    # store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding to the "feels_like" key of y
    current_feels_like = y["feels_like"]

    # store the value corresponding to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather" key in variable z
    z = x["weather"]

    # store the value corresponding to the "description" key at the 0th index of z
    weather_description = z[0]["description"]

    # store the value of "wind" key in variable w
    w = x["wind"]

    # store the value corresponding to the "speed" key of w
    current_speed = w["speed"]

    # translate "current_speed" from m/s to km/h
    kmh_speed = current_speed * 3.6

    # print following values
    print(" Temperature (in Celsius unit) = " +
          str(current_temperature) +
          "\n |-> feels like (in Celsius unit) = " +
          str(current_feels_like) +
          "\n Wind speed (in km/h) = " +
          str(kmh_speed) +
          "\n Atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n Humidity (in percentage) = " +
          str(current_humidity) +
          "\n Description = " +
          str(weather_description))

else:
    print(" City Not Found ")


# Geocoding
base_url_geo = 'http://api.openweathermap.org/geo/1.0/direct?'
geo_url = base_url_geo + 'appid=' + api_key + '&q=' + city + '&limit=1'

coordinates = requests.get(geo_url)
g = coordinates.json()

"""END OF TEMPORARY PLACEMENT"""


class Weather:
    def __init__(self, root):
        self.root = root
        self.root.title = "Weather"
        self.make_widgets()

    def make_widgets(self):
        """Add functionality to tKinter window."""
        # Title/Output --- TEST
        self.output = tk.Label(self.root, text="TITLE-TEST")
        self.output.pack()

        # Input
        tk.Label(self.root, text="What's the weather like in...?")
        self.location = tk.Entry(self.root)
        self.location.pack()

        # Button
        self.button = tk.Button(self.root, text="Submit", command=self.check_location)
        self.button.pack(pady=10)

        # Have 'Enter'-key submit "Input"
        self.root.bind('<Return>', lambda event=None: self.check_location())

    def check_location(self):
        """Check input value."""
        loc = self.location.get()

        if loc == "Alaska":
            self.output.config(text="Cold.")
        else:
            self.output.config(text="It's cold in Alaska.")

    '''def call_API(self):'''


root = tk.Tk()
root.geometry("500x400")
weather = Weather(root)
root.mainloop()
