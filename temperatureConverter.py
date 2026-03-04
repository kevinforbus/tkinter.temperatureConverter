import tkinter as tk
from converters import TempConverters

# Define the main application class for the temperature converter GUI
class App:
    def __init__(self, window):
        # Store window reference and create main frame
        self.window = window
        frame = tk.Frame(window)
        frame.pack()

        # Create variable objects to store temperature values
        self.c_var = tk.StringVar()
        self.f_var = tk.StringVar()

        # Add labels for Celsius and Fahrenheit
        tk.Label(frame, text='Deg C').grid(row=0, column=0)
        tk.Label(frame, text='Deg F').grid(row=1, column=0, pady=5)
        
        # Create input fields for temperature values
        c_entry = tk.Entry(frame, textvariable=self.c_var)
        c_entry.grid(row=0, column=1, padx=5)
        c_entry.bind('<Return>', lambda event: self.convert())
        
        f_entry = tk.Entry(frame, textvariable=self.f_var)
        f_entry.grid(row=1, column=1, padx=5)
        f_entry.bind('<Return>', lambda event: self.convert())

        # Create button frame for centered buttons
        button_frame = tk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Add Convert and Reset buttons
        convert_button = tk.Button(button_frame, text='Convert', command=self.convert)
        convert_button.bind('<Return>', lambda event: self.convert())
        convert_button.pack(side=tk.LEFT, padx=5)
        
        reset_button = tk.Button(button_frame, text='Reset', command=self.reset)
        reset_button.bind('<Return>', lambda event: self.reset())
        reset_button.pack(side=tk.LEFT, padx=5)

    # Handle the convert button action
    def convert(self):
        # Check if Celsius value is entered, convert to Fahrenheit
        if self.c_var.get() != "":
            # Convert to Fahrenheit
            celsius = self.c_var.get()
            converter = TempConverters('C', 'F', celsius)
            fahrenheit = converter.celsius_to_fahrenheit(float(celsius))
            self.f_var.set(fahrenheit)
        
        # Otherwise, check if Fahrenheit value is entered, convert to Celsius
        elif self.f_var.get() != "":
            fahrenheit = self.f_var.get()
            converter = TempConverters('F', 'C', fahrenheit)
            celsius = converter.fahrenheit_to_celsius(float(fahrenheit))
            self.c_var.set(celsius)

    # Clear both temperature values
    def reset(self):
        self.c_var.set("")
        self.f_var.set("")

# Create a basic window
window = tk.Tk()
window.title('Temperature Converter')
window.geometry('300x100')

# Instantiate the App object
app = App(window)

# Start the main event loop
window.mainloop()