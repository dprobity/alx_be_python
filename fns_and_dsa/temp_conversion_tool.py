CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius:.2f}°C")

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit:.2f}°F")

# User input
try:
    current_temp = float(input("Enter the temperature to convert: "))
    temp_units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temp_units == "C":
        convert_to_fahrenheit(current_temp)
    elif temp_units == "F":
        convert_to_celsius(current_temp)
    else:
        print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Error: Invalid temperature. Please enter a numeric value.")
