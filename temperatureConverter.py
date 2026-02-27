import tkinter as tk
from tkinter import ttk
from converters import TempConverters

class App:
    def __init__(self, window):
        self.window = window
        frame = tk.Frame(window)
        frame.pack()

        self.c_var = tk.DoubleVar()
        self.f_var = tk.DoubleVar()
        
        tk.Label(frame, text='Deg C').grid(row=0, column=0)
        tk.Label(frame, text='Deg F').grid(row=1, column=0, pady=5)
        
        tk.Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.f_var).grid(row=1, column=1)

        tk.Button(frame, text='Convert', command=self.convert).grid(row=2, column=0, columnspan=2, pady=10)


    def convert(self):
        # Convert to Fahrenheit
        celsius = self.c_var.get()
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        self.f_var.set(fahrenheit)

        # Convert to Celsius
        fahrenheit = self.f_var.get()
        celsius = self.converters.fahrenheit_to_celsius(fahrenheit)
        self.c_var.set(celsius)


# Create a basic window
window = tk.Tk()
window.title('Temperature Converter')
window.geometry('300x100')

# Instantiate the App object
app = App(window)

# Start the main event loop
window.mainloop()