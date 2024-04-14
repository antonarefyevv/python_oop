class TemperatureConverter:
    def convert_from_celsius_to_kelvin(self, celsius_temperature):
        return celsius_temperature + 273.15

    def convert_from_celsius_to_fahrenheit(self, celsius_temperature):
        return celsius_temperature * 1.8 + 32

    def convert_from_fahrenheit_to_kelvin(self, fahrenheit_temperature):
        return (fahrenheit_temperature + 459.67) / 1.8

    def convert_from_fahrenheit_to_celsius(self, fahrenheit_temperature):
        return (fahrenheit_temperature - 32) / 1.8

    def convert_from_kelvin_to_fahrenheit(self, kelvin_temperature):
        return kelvin_temperature * 1.8 - 459.67

    def convert_from_kelvin_to_celsius(self, kelvin_temperature):
        return kelvin_temperature - 273.15
