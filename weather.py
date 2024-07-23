### WEATHER ###
"""V0.6: Store Data -> Write"""


import requests, json
import tkinter as tk


class Weather:
    def __init__(self, root):
        self.root = root
        self.root.title = "Weather"
        self.make_widgets()

    def make_widgets(self):
        """Add functionality to tKinter window."""
        # Title
        self.title = tk.Label(self.root, text="TITLE-TEST")
        self.title.pack()

        # Input
        tk.Label(self.root, text="What's the weather like in...?")
        self.location = tk.Entry(self.root)
        self.location.pack()

        # Button
        self.button = tk.Button(self.root, text="Submit", command=self.call_api)
        self.button.pack(pady=10)

        # Have 'Enter'-key submit "Input"
        self.root.bind('<Return>', lambda event=None: self.call_api())

        # Output
        self.output = tk.Label(self.root, text="")
        self.output.pack()

    def call_api(self):
        """Call API."""
        # API Key
        api_key = '3294a33bb60c1fa031b89f141c8bfd74'

        # URL to API-store ---> "COMPLETE URL", (full_url), REQUIRES USER INPUT (and other variables)
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'

        city = self.location.get()

        while len(city) < 3:
            # If the variable stored in 'city' contains less than 3 characters ('no','hi'), results in "KEY ERROR: 'main'"
            city = " " + city

        # Complete URL
        full_url = base_url + 'appid=' + api_key + '&q=' + city + '&units=metric'
        '''Default temperature measurements are in Kelvin.'''

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

            txt = str(" Temperature (in Celsius unit) = " +
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

            # Return to 'Output'
            self.output.config(text=txt)

            # Store data
            f = open('weather.txt', 'w')
            f.write(txt)

        else:
            self.output.config(text=" City Not Found ")


root = tk.Tk()
root.geometry("500x400")
weather = Weather(root)
root.mainloop()
