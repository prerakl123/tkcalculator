class Temperature:
    K, F, C = [0] * 3


class TemperatureConverter:
    def __init__(self):
        self.temperature = Temperature()

    def convert(self, value: float, from_type: str):
        if from_type.lower() in ['c', 'celsius']:
            self.temperature.K = value + 273.15
            self.temperature.F = (value * (9/5)) + 32
            self.temperature.C = value
        elif from_type.lower().rstrip('s') in ['fahrenheit', 'f']:
            self.temperature.K = ((value - 32) * (5 / 9)) + 273.15
            self.temperature.F = value
            self.temperature.C = (value - 32) * (5 / 9)
        elif from_type.lower().rstrip('s') in ['kelvin', 'k']:
            self.temperature.K = value
            self.temperature.F = ((value - 273.15) * (9 / 5)) + 32
            self.temperature.C = value - 273.15
        else:
            raise KeyError(f'Invalid temperature unit type "{from_type}"')

        return self.temperature


if __name__ == '__main__':
    c = TemperatureConverter()
    s = c.convert(98142.123, 'F')
