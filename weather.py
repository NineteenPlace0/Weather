### WEATHER ###
"""V0.2: Add comments"""

import tkinter as tk


class Weather:
    def __init__(self, root):
        self.root = root
        self.root.title = "Weather"
        self.make_widgets()

    def make_widgets(self):
        """Add functionality to tKinter window."""
        # Title/Output --- TEST
        self.output = tk.Label(self.root, text="")
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


root = tk.Tk()
root.geometry("500x400")
weather = Weather(root)
root.mainloop()
