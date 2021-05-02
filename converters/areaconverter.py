class Area:
    sqmm, sqcm, sqdm, sqm, sqdam, sqhm, sqkm, sqM, sqyd, sqft, sqinch, ha, acre = [0] * 13


class AreaConverter:
    def __init__(self):
        self.area = Area()
        self.area_conversion_value_table = {
            'sqmm':        1, 'sqcm':      100, 'sqdm':     1000, 'sqm':      1e+6, 'sqdam': 1e+8, 'sqhm': 1e+10,
            'sqkm':    1e+12, 'sqM':  2.59e+12, 'sqinch': 645.16, 'sqyard': 836127, 'sqft': 92903, 'ha':   1e+10,
            'acre': 4.047e+9
        }
        self.name_conversion_table = {
            'square millimeter': 'sqmm',     'squaremillmeter':  'sqmm',
            'square decimeter':  'sqdm',     'squaredecimeter':  'sqdm',
            'square meter':       'sqm',     'squaremeter':       'sqm',
            'square decameter': 'sqdam',     'squaredecameter': 'sqdam',
            'square hectometer': 'sqhm',     'squarehectometer': 'sqhm',
            'square kilometer':  'sqkm',     'squarekilometer':  'sqkm',
            'square mile':        'sqM',     'squaremile':        'sqM',
            'square inch':     'sqinch',     'squareinch':     'sqinch',
            'square yard':       'sqyd',     'squareyard':       'sqyd',
            'squarefoot':        'sqft',     'square foot':      'sqft',
            'hectare':             'ha',     'acre':             'acre'
        }
        self.area_units = [u for u in list(Area.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_area_value = self.area_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_area_value = self.area_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid area unit type "{from_type}"')

        value = value * from_type_area_value

        for i in self.area_units:
            self.area.__setattr__(i, value / self.area_conversion_value_table[i])
        return self.area


if __name__ == '__main__':
    c = AreaConverter()
    s = c.convert(79835462.1234, 'hm')
    print(s.__dict__)
