class TempConverters:
    """A class to convert between temperature units (Celsius and Fahrenheit)."""

    def __init__(self, units_from, units_to, temperature):
        """Initialize the temperature converter.
        
        Args:
            units_from (str): The source temperature unit (e.g., 'C' for Celsius)
            units_to (str): The target temperature unit (e.g., 'F' for Fahrenheit)
            temperature (float): The initial temperature value
        """
        self.units_from = units_from
        self.units_to = units_to
        self.temperature = temperature
    
    def description(self):
        """Get a description of the conversion.
        
        Returns:
            str: A string describing the conversion (e.g., 'Convert C to F')
        """
        return f'Convert {self.units_from} to {self.units_to}'

    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius temperature to Fahrenheit.
        
        Args:
            celsius (float): Temperature in Celsius
            
        Returns:
            str: Temperature in Fahrenheit as a string
        """
        return str((celsius * 9) / 5 + 32)

    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit temperature to Celsius.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit
            
        Returns:
            str: Temperature in Celsius as a string
        """
        return str((fahrenheit - 32) * 5/9)


# Test cases for the TempConverters class...Remove once project is complete.
# c1 = TempConverters('C', 'F', 0)
# print(str(c1.celsius_to_fahrenheit(45)) + ' ' + c1.units_to)

# c2 = TempConverters('F', 'C', 0)
# print(str(c2.fahrenheit_to_celsius(68)) + ' ' + c2.units_to)