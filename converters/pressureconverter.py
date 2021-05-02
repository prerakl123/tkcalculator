class Pressure:
    bar, atm, Pa, kPa, torr, mmHg, lbsqinch = [0] * 7


class PressureConverter:
    def __init__(self):
        self.pressure = Pressure()
        self.bar_conversion_value_table = {
            'bar':           1, 'atm':   1.01325, 'Pa':            1e-5, 'kPa': 0.01,
            'torr': 0.00133322, 'mmHg': 0.001333, 'lbsqinch': 0.0689476
        }
        self.name_conversion_table = {
            'bar':        'bar', 'millimeters of mercury': 'mmHg', 'atmosphere':          'atm',
            'pascal':      'Pa', 'millimetermercury':      'mmHg', 'standard atmosphere': 'atm',
            'kilopascal': 'kPa', 'millimeter mercury':     'mmHg', 'torr': 'torr',

            'pounds per square inch': 'lbsqinch', 'pound square inch': 'lbsqinch',
            'poundpersquareinch':     'lbsqinch', 'poundsquareinch':   'lbsqinch'
        }
        self.pressure_units = [u for u in list(Pressure.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_bar_value = self.bar_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_bar_value = self.bar_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid pressure unit type "{from_type}"')

        value = value * from_type_bar_value

        for i in self.pressure_units:
            self.pressure.__setattr__(i, value / self.bar_conversion_value_table[i])
        return self.pressure


if __name__ == '__main__':
    c = PressureConverter()
    s = c.convert(9184761984.1243, 'torr')
    print(s.__dict__)
