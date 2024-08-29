### WEATHER ###
"""V1.0.0: Weather-Checker"""


import tkinter as tk
from tkinter import messagebox

import datetime
import requests
from docx import Document


class Weather:
    def __init__(self, root):
        self.root = root
        self.root.title = "Weather"
        self.make_widgets()

    def make_widgets(self):
        """Add functionality to tKinter window."""
        # Title
        self.title = tk.Label(self.root, text="What's the weather like in...?")
        self.title.pack()

        # Input
        self.location = tk.Entry(self.root)
        self.location.pack()

        # Button
        self.button = tk.Button(self.root, text="Submit", command=self.call_api)
        self.button.pack(pady=10)

        # Have 'Enter'-key submit "Input"
        self.root.bind('<Return>', lambda event=None: self.call_api())

        # Output
        self.output_title = tk.Label(self.root, text="")
        self.output_title.pack()
        self.output = tk.Label(self.root, text="", justify="left")
        self.output.pack()

        # Save output
        self.save = tk.Button(self.root, text="Save?", command=self.store_word)
        self.save.pack()

    def call_api(self):
        """Call API."""
        self.date_time()
        # API Key
        api_key = '3294a33bb60c1fa031b89f141c8bfd74'

        # URL to API-store ---> "COMPLETE URL", (full_url), REQUIRES USER INPUT (and other variables)
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'

        self.city = self.location.get()

        # "KEY ERROR: 'main'"
        while len(self.city) < 3:
            '''If the variable stored in 'city' contains less than 3 characters ('no','hi'), results in "ERROR".'''
            self.city = " " + self.city

        # Complete URL
        full_url = base_url + 'appid=' + api_key + '&q=' + self.city + '&units=metric'
        '''Default temperature measurements are in Kelvin.'''

        print()
        response = requests.get(full_url)

        x = response.json()

        if x["cod"] != "404":

            # Store the value of "main" key in variable y
            y = x["main"]

            # Store values to corresponding keys of y
            current_temperature = y["temp"]
            current_feels_like = y["feels_like"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

            # Store the value of "weather" key in variable z
            z = x["weather"]

            # Store the value corresponding to the "description" key at the 0th index of z
            weather_description = z[0]["description"]

            # Store the value of "wind" key in variable w
            w = x["wind"]

            # Store the value corresponding to the "speed" key of w
            current_speed = w["speed"]

            # Translate "current_speed" from m/s to km/h
            kmh_speed = current_speed * 3.6

            # Improve readability of data
            title = str(self.city.title() + "\n" + self.dt)
            txt = str("\n Temperature (in Celsius unit) = " +
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

            # Return to 'Output' / Display results
            self.output_title.config(text=title)
            self.output.config(text=txt)
            self.data = title + txt

            # Store data
            f = open('weather.txt', 'w')
            f.write(self.data)

        else:
            self.output.config(text=" City Not Found ")

    def store_word(self):
        """Store retrieved data in 'Word-document' (.docx)."""
        word = messagebox.askyesno("Store data?", "Store data in '.docx'-file?")
        if word:
            # Name Document
            doc_name = str(self.city.replace(' ', '_')) + str(self.dtfile) + ".docx"

            # Create, write and save Document
            doc = Document()
            doc.add_paragraph(text=self.data)
            doc.save(doc_name)

    def date_time(self):
        """Store current date & time."""
        self.dtnow = datetime.datetime.now()
        self.dtfile = self.dtnow.strftime('%Y%m%d%H%M%S')
        self.dt = self.dtnow.strftime('%Y/%m/%d_%H:%M:%S')


root = tk.Tk()
root.title("Weather-Checker")
root.geometry("250x300")
weather = Weather(root)
root.mainloop()
