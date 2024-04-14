from temperature_converter import TemperatureConverter
from temperature_window import TemperatureWindow

temperature_converter = TemperatureConverter()

temperature_window = TemperatureWindow(temperature_converter)
temperature_window.start()