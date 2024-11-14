

class UnitConvertor:

    length_units = {
        'millimeter': 1, 'centimeter': 10, 'meter': 1000, 'kilometer': 1_000_000,
        'inch': 25.4, 'foot': 304.8, 'yard': 914.4, 'mile': 1_609_344
    }

    weight_units = {
        'milligram': 1, 'gram': 1000, 'kilogram': 1_000_000,
        'ounce': 28_349.5, 'pound': 453_592
    }

    temperature_units = {'celsius', 'fahrenheit', 'kelvin'}


    def convert_length(self, value: float, from_unit: str, to_unit:str)-> float:
        """Converts length units - supporting the units in length_units"""
        from_unit = from_unit.strip().lower()
        to_unit = to_unit.strip().lower()
        try:
            return value * (self.length_units[from_unit] / self.length_units[to_unit])
        except KeyError:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported')
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')


    def convert_weight(self, value: float, from_unit: str, to_unit: str)-> float:
        """Converts weight units - supporting the units in weight_units"""
        from_unit = from_unit.strip().lower()
        to_unit = to_unit.strip().lower()
        try:
            return value * (self.weight_units[from_unit] / self.weight_units[to_unit])
        except KeyError:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported.')
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')


    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """Converts temperature units - supporting the units in temperature_units with specific formulas"""
        from_unit = from_unit.strip().lower()
        to_unit = to_unit.strip().lower()
        if from_unit not in self.temperature_units or to_unit not in self.temperature_units:
            raise ValueError(f'Invalid units: `{from_unit}` or `{to_unit}` is not supported.')

        try:
            if from_unit=='celsius' and to_unit == 'fahrenheit':
                return (value * 9/5) + 32
            elif from_unit=='fahrenheit' and to_unit == 'celsius':
                return (value - 32) * 5/9
            elif from_unit=='kelvin' and to_unit == 'celsius':
                return value - 273.15
            elif from_unit=='celsius' and to_unit == 'kelvin':
                return value + 273.15
            elif from_unit=='fahrenheit' and to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
            elif from_unit=='kelvin' and to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
        except TypeError:
            raise TypeError('Invalid input value. Please enter a numeric value(integer or float).')


    def convert(self, conversion_type: str, value: float, from_unit: str, to_unit: str):
        """Handles the conversion type to use the right conversion method"""
        match conversion_type:
            case 'length':
                return self.convert_length(value, from_unit, to_unit)
            case 'weight':
                return self.convert_weight(value, from_unit, to_unit)
            case 'temperature':
                return self.convert_temperature(value, from_unit, to_unit)
            case _:
                raise Exception('Invalid conversion type.')

def main():
    convertor = UnitConvertor()
    conversion_type = input("Enter conversion type (length, weight, temperature): ").strip().lower()
    try:
        value = float(input(f"Enter the value to convert: "))
    except ValueError:
        print('Invalid input value. Please enter a numeric value(integer or float).')
        return

    from_unit = input("Enter unit to convert from: ").strip().lower()
    to_unit = input("Enter unit to convert to: ").strip().lower()

    try:
        result = convertor.convert(conversion_type, value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()