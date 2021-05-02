class WeightAndMass:
    mg, cg, dg, g, dag, hg, kg, ton, ct, oz, lb, stone, short_tons_us, long_tons_uk = [0] * 14


class WeightAndMassConverter:
    def __init__(self):
        self.weightandmass = WeightAndMass()
        self.mg_conversion_value_table = {
            'mg':      1,      'ton':                1e+9,
            'cg':     10,      'ct':                  200,
            'dg':    100,      'oz':             28349.52,
            'g':    1000,      'lb':             453592.4,
            'dag': 10000,      'stone':           6350293,
            'hg':   1e+5,      'short_tons_us': 907184740,
            'kg':   1e+6,      'long_tons_uk': 1016046909
        }
        self.name_conversion_table = {
            'milligram': 'mg',  'metric tonne': 'ton', 'short tons us': 'short_tons_us',
            'centigram': 'cg',  'tonne':        'ton', 'short ton':     'short_tons_us',
            'decigram':  'dg',  'carat':         'ct', 'us short ton':  'short_tons_us',
            'gram':       'g',  'ounce':         'oz', 'long tons uk':   'long_tons_uk',
            'decagram':  'dg',  'pound':         'lb', 'long ton':       'long_tons_uk',
            'hectogram': 'hg',  'stone':      'stone', 'uk long ton':    'long_tons_uk',
            'kilogram':  'kg',
        }
        self.weightandmass_units = [u for u in list(WeightAndMass.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s') if not from_type.endswith('us') else from_type
        if from_type in list(self.name_conversion_table.values()):
            from_type_mg_value = self.mg_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_mg_value = self.mg_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid mass unit type "{from_type}"')

        value = value * from_type_mg_value

        for i in self.weightandmass_units:
            self.weightandmass.__setattr__(i, value / self.mg_conversion_value_table[i])
        return self.weightandmass


if __name__ == '__main__':
    c = WeightAndMassConverter()
    s = c.convert(89324.13, 'tons')
    print(s.__dict__)
