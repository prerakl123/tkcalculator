class Length:
    nm, um, mm, cm, dm, m, dam, hm, km, M, yd, ft, inch, NM = [0] * 14


class LengthConverter:
    def __init__(self):
        self.length = Length()
        self.length_conversion_value_table = {
            'nm':      1, 'hm':       1e+11,
            'um':   1000, 'km':       1e+12,
            'mm':   1e+6, 'M': 1.609344e+12,
            'cm':   1e+7, 'yd':    9.144e+8,
            'dm':   1e+8, 'ft':    3.048e+8,
            'm':    1e+9, 'inch':   2.54e+7,
            'dam': 1e+10, 'NM':   1.852e+12

        }
        self.name_conversion_table = {
            'nanometer':  'nm', 'micrometer':    'um', 'millimeter':     'mm', 'centimeter': 'cm',
            'inch':     'inch', 'decimeter':     'dm', 'meter':           'm', 'decameter': 'dam',
            'hectometer': 'hm', 'kilometer':     'km', 'mile':            'M', 'yard':       'yd',
            'foot':       'ft', 'nauticalmiles': 'NM', 'nautical miles': 'NM'
        }

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_length_value = self.length_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_length_value = self.length_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid length unit type "{from_type}"')

        value = value * from_type_length_value

        for i in self.length:
            self.length.__setattr__(i, value / self.length_conversion_value_table[i])
        return self.length


if __name__ == '__main__':
    c = LengthConverter()
    s = c.convert(5 * (10 ** 45), 'ft')
    print(s.__dict__)
