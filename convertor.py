from logging import raiseExceptions
from webbrowser import Error


class UnitConvertor:

    length_units = {
        'millimeter': 1, 'centimeter': 10, 'meter': 1000, 'kilometer': 1_000_000,
        'inch': 25.4, 'foot': 304.8, 'yard': 914.4, 'mile': 1_609_344
    }

    weight_units = {
        'milligram': 1, 'gram': 1000, 'kilogram': 1_000_000,
        'ounce': 28_349.5, 'pound': 453_592
    }

    temperature_units = {'Celsius', 'Fahrenheit', 'Kelvin'}


    def convert_length(self, value: float, from_unit: str, to_unit:str)-> float:
        """Converts length units - supporting the units in length_units"""
        try:
            return value * (self.length_units[to_unit] / self.length_units[from_unit])
        except KeyError:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported')
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')


    def convert_weight(self, value: float, from_unit: str, to_unit: str)-> float:
        """Converts weight units - supporting the units in weight_units"""
        try:
            return value * (self.length_units[to_unit] / self.length_units[from_unit])
        except KeyError:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported.')
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')


    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """Converts temperature units - supporting the units in temperature_units with specific formulas"""
        try:
            if from_unit=='Celsius' and to_unit == 'Fahrenheit':
                return (value * 9/5) + 32
            elif from_unit=='Fahrenheit' and to_unit == 'Celsius':
                return (value - 32) * 5/9
            elif from_unit=='Kelvin' and to_unit == 'Celsius':
                return value - 273.15
            elif from_unit=='Celsius' and to_unit == 'Kelvin':
                return value + 273.15
            elif from_unit=='Fahrenheit' and to_unit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
            elif from_unit=='Kelvin' and to_unit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32
        except KeyError:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported.')
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')



def main():
    convertor = UnitConvertor()
    pass


if __name__ == '__main__':
    main()