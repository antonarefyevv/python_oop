from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

import select


class TemperatureWindow:
    def __init__(self, temperature_converter):

        self.__root = Tk()

        self.__root.title('First app on Tkinter')
        self.__root.geometry('600x400')

        frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        text_temperature = StringVar()

        label_temperature = ttk.Label(frame, text='Введите температуру:')
        label_temperature.pack(padx=5, anchor=NW)

        celsius_temperature_entry = ttk.Entry(frame, textvariable=text_temperature, width=20)
        celsius_temperature_entry.pack(padx=5, pady=5, anchor=NW)

        def convert():
            try:
                temperature = float(text_temperature.get())

                if scales.get() == 'Шкала Цельсия':

                    if convert_to_celsius.get() == 1:
                        celsius_label['text'] = f'Результат в шкале Цельсия = {temperature}'

                    if convert_to_kelvin.get() == 1:
                        kelvin_temperature = temperature_converter.convert_from_celsius_to_kelvin(temperature)
                        kelvin_label['text'] = f'Результат в шкале Кельвина = {kelvin_temperature}'

                    if convert_to_fahrenheit.get() == 1:
                        fahrenheit_temperature = temperature_converter.convert_from_celsius_to_fahrenheit(temperature)
                        fahrenheit_label['text'] = f'Результат в шкале Фаренгейта = {fahrenheit_temperature}'

                if scales.get() == 'Шкала Кельвина':

                    if convert_to_kelvin.get() == 1:
                        kelvin_label['text'] = f'Результат в шкале Кельвина = {temperature}'

                    if convert_to_celsius.get() == 1:
                        celsius_temperature = temperature_converter.convert_from_kelvin_to_celsius(temperature)
                        celsius_label['text'] = f'Результат в шкале Цельсия = {celsius_temperature}'

                    if convert_to_fahrenheit.get() == 1:
                        fahrenheit_temperature = temperature_converter.convert_from_kelvin_to_fahrenheit(temperature)
                        fahrenheit_label['text'] = f'Результат в шкале Фаренгейта = {fahrenheit_temperature}'

                if scales.get() == 'Шкала Фаренгейта':

                    if convert_to_celsius.get() == 1:
                        celsius_temperature = temperature_converter.convert_from_fahrenheit_to_celsius(temperature)
                        celsius_label['text'] = f'Результат в шкале Цельсия = {celsius_temperature}'

                    if convert_to_kelvin.get() == 1:
                        kelvin_temperature = temperature_converter.convert_from_fahrenheit_to_kelvin(temperature)
                        kelvin_label['text'] = f'Результат в шкале Кельвина = {kelvin_temperature}'

                    if convert_to_fahrenheit.get() == 1:
                        fahrenheit_label['text'] = f'Результат в шкале Фаренгейта = {temperature}'

            except ValueError:
                showerror('Ошибка', 'Температура должна быть числом')

        frame.pack(padx=10, pady=5, fill=X)

        label_scales = ttk.Label(frame, text='Укажите шкалу из которой требуется конвертировать данную температуру:')
        label_scales.pack(padx=5, anchor=NW)

        scales = StringVar()
        scales.set('Шкала Цельсия')

        celsius_scale_button = ttk.Radiobutton(frame, variable=scales, value='Шкала Цельсия', text='Шкала Цельсия')
        celsius_scale_button.pack(anchor=NW)

        kelvin_scale_button = ttk.Radiobutton(frame, variable=scales, value='Шкала Кельвина', text='Шкала Кельвина')
        kelvin_scale_button.pack(anchor=NW)

        fahrenheit_scale_button = ttk.Radiobutton(frame, variable=scales, value='Шкала Фаренгейта',
                                                  text='Шкала Фаренгейта')
        fahrenheit_scale_button.pack(anchor=NW)

        label_convert_scale = ttk.Label(frame,
                                        text='Укажите шкалу в которую требуется конвертировать данную температуру:')
        label_convert_scale.pack(padx=5, pady=5, anchor=NW)

        convert_to_celsius = IntVar()
        convert_check_button_to_celsius = ttk.Checkbutton(frame, variable=convert_to_celsius,
                                                          text='Конвертировать в шкалу Цельсия')
        convert_check_button_to_celsius.pack(anchor=W)

        convert_to_kelvin = IntVar()
        convert_check_button_to_kelvin = ttk.Checkbutton(frame, variable=convert_to_kelvin,
                                                         text='Конвертировать в шкалу Кельвина')
        convert_check_button_to_kelvin.pack(anchor=W)

        convert_to_fahrenheit = IntVar()
        convert_check_button_to_fahrenheit = ttk.Checkbutton(frame, variable=convert_to_fahrenheit,
                                                             text='Конвертировать в шкалу Фаренгейта')
        convert_check_button_to_fahrenheit.pack(anchor=W)

        convert_button = ttk.Button(frame, text='Конвертировать', command=convert)
        convert_button.pack(pady=5)

        celsius_label = ttk.Label()
        celsius_label.pack(padx=10, anchor=W)

        kelvin_label = ttk.Label()
        kelvin_label.pack(padx=10, anchor=W)

        fahrenheit_label = ttk.Label()
        fahrenheit_label.pack(padx=10, anchor=W)

    def start(self):
        self.__root.mainloop()
