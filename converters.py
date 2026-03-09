class TempConverters:
    """A class to convert between temperature units (Celsius and Fahrenheit)."""

    def __init__(self, temperature):
        """Initialize the temperature converter.
        
        Args:
            temperature (float): The initial temperature value
        """
        self.temperature = temperature
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius temperature to Fahrenheit.
        
        Args:
            celsius (float): Temperature in Celsius
            
        Returns:
            str: Temperature in Fahrenheit as a string
        """
        # Apply the formula: F = (C * 9/5) + 32
        return str((celsius * 9) / 5 + 32)

    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit temperature to Celsius.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit
            
        Returns:
            str: Temperature in Celsius as a string
        """
        # Apply the formula: C = (F - 32) * 5/9
        return str((fahrenheit - 32) * 5/9)
