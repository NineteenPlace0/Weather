### WEATHER ###
"""V0.1: Setup tKinter"""

import tkinter as tk


class Weather:
    def __init__(self, root):
        self.root = root
        self.root.title = "Weather"
        self.make_widgets()

    def make_widgets(self):
        self.output = tk.Label(self.root, text="")
        self.output.pack()

        tk.Label(self.root, text="What's the weather like in...?")
        self.location = tk.Entry(self.root)
        self.location.pack()

        self.button = tk.Button(self.root, text="Submit", command=self.check_location)
        self.button.pack(pady=10)

        self.root.bind('<Return>', lambda event=None: self.check_location())

    def check_location(self):
        loc = self.location.get()

        if loc == "Alaska":
            self.output.config(text="Cold.")
        else:
            self.output.config(text="It's cold in Alaska.")


root = tk.Tk()
root.geometry("500x400")
weather = Weather(root)
root.mainloop()
