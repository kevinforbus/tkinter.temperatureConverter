import tkinter as tk
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
        
        tk.Entry(frame, textvariable=self.c_var).grid(row=0, column=1, padx=5,)
        tk.Entry(frame, textvariable=self.f_var).grid(row=1, column=1, padx=5)

        # Create button frame for centered buttons
        button_frame = tk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        tk.Button(button_frame, text='Convert', command=self.convert).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text='Reset', command=self.reset).pack(side=tk.LEFT, padx=5)

    def convert(self):
        if self.c_var.get() != 0.0:
            # Convert to Fahrenheit
            celsius = self.c_var.get()
            converter = TempConverters('C', 'F', celsius)
            fahrenheit = converter.celsius_to_fahrenheit(celsius)
            self.f_var.set(fahrenheit)
        
        elif self.f_var.get() != 0.0:
            # Convert to Celsius
            fahrenheit = self.f_var.get()
            converter = TempConverters('F', 'C', fahrenheit)
            celsius = converter.fahrenheit_to_celsius(fahrenheit)
            self.c_var.set(celsius)

    def reset(self):
        self.c_var.set(0.0)
        self.f_var.set(0.0)

# Create a basic window
window = tk.Tk()
window.title('Temperature Converter')
window.geometry('300x100')

# Instantiate the App object
app = App(window)

# Start the main event loop
window.mainloop()