# Temperature Converter

A simple and intuitive graphical application for converting temperatures between Celsius and Fahrenheit.

## Overview

Temperature Converter is a lightweight desktop application built with Python's Tkinter library. It allows you to quickly convert temperature values between Celsius and Fahrenheit scales with a clean, user-friendly interface.

## Features

- **Bidirectional Conversion**: Convert from Celsius to Fahrenheit or Fahrenheit to Celsius
- **Real-time Input**: Enter temperature values in either unit
- **Quick Reset**: Clear values with a single button click
- **Lightweight**: Minimal dependencies and fast startup

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone or download the repository
2. Navigate to the project directory:
   ```
   cd tkinter.temperatureConverter
   ```

## Usage

### Running the Application

```bash
python temperatureConverter.py
```

The application window will open with two input fields and control buttons.

### How to Convert

1. **Enter a Temperature**: Type a temperature value into the Celsius field or the Fahrenheit field
2. **Click Convert**: Press the "Convert" button to calculate the equivalent temperature in the other unit
3. **View the Result**: The converted temperature will appear in the corresponding field

### Example Usage

- Enter `32` in the Celsius field and click Convert → displays `89.6` in the Fahrenheit field
- Enter `98` in the Fahrenheit field and click Convert → displays the equivalent Celsius value

### Reset Values

Click the "Reset" button to clear both temperature fields.

## Modules

### temperatureConverter.py
The main application file containing the graphical user interface built with Tkinter. It handles user interactions, manages input fields, and coordinates the conversion calls.

### converters.py
Core module containing the `TempConverters` class, which handles all temperature conversion calculations. This module includes methods for:
- Converting Celsius to Fahrenheit
- Converting Fahrenheit to Celsius

### README.md
This documentation file

## How It Works

The application uses the standard temperature conversion formulas:

- **Celsius to Fahrenheit**: °F = (°C × 9/5) + 32
- **Fahrenheit to Celsius**: °C = (°F − 32) × 5/9

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for full details.
