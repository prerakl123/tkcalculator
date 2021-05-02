class Volume:
    ml, l, cubic_cm, cubic_m, cubic_inch, cubic_ft, cubic_yd, tsp_us, tbsp_us, floz_us, cup_us, pt_us, qt_us, gal_us, \
        tsp_uk, tbsp_uk, floz_uk, pt_uk, qt_uk, gal_uk = [0] * 20


class VolumeConverter:
    def __init__(self):
        self.volume = Volume()
        self.ml_conversion_value_table = {
            'ml':                1, 'l':            1000, 'cubic_cm':        1, 'cubic_m':     1e+6,
            'cubic_inch': 16.38706, 'cubic_ft': 28316.85, 'cubic_yd': 764554.9, 'tsp_us':  4.928922,
            'tbsp_us':    14.78676, 'floz_us':  29.57353, 'cup_us':   236.5882, 'pt_us':   473.1765,
            'qt_us':      946.3529, 'gal_us':   3785.412, 'tsp_uk':   5.919388, 'tbsp_uk': 17.75816,
            'floz_uk':    28.41306, 'pt_uk':    568.2613, 'qt_uk':    1136.523, 'gal_uk':   4546.09
        }
        self.name_conversion_table = {
            'millilitre': 'ml', 'litre': 'l',

            'cubic cm':         'cubic_cm', 'cubic m':          'cubic_m', 'cubic inch': 'cubic_inch',
            'cm cube':          'cubic_cm', 'm cube':           'cubic_m', 'inch cube':  'cubic_inch',
            'cubiccm':          'cubic_cm', 'cubicm':           'cubic_m', 'cubicinch':  'cubic_inch',
            'cubic centimeter': 'cubic_cm', 'cubic meter':      'cubic_m',
            'cubiccentimeter':  'cubic_cm', 'cubicmeter':       'cubic_m',
            'centimeter cube':  'cubic_cm', 'meter cube':       'cubic_m',
            'centimetercube':   'cubic_cm', 'metercube':        'cubic_m', 'inchcube':   'cubic_inch',

            'cubic ft':         'cubic_ft', 'cubic yd':        'cubic_yd', 'cup':            'cup_us',
            'ft cube':          'cubic_ft', 'yd cube':         'cubic_yd',
            'cubicft':          'cubic_ft', 'cubicyd':         'cubic_yd',
            'cubic feet':       'cubic_ft', 'cubic yard':      'cubic_yd',
            'cubicfeet':        'cubic_ft', 'cubicyard':       'cubic_yd',
            'feet cube':        'cubic_ft', 'yard cube':       'cubic_yd',
            'feetcube':         'cubic_ft', 'yardcube':        'cubic_yd',

            'us tea spoon':       'tsp_us', 'uk tea spoon':      'tsp_uk', 'pt us':           'pt_us',
            'us teaspoon':        'tsp_us', 'uk teaspoon':       'tsp_uk', 'ptus':            'pt_us',
            'usteaspoon':         'tsp_us', 'ukteaspoon':        'tsp_uk', 'pint us':         'pt_us',
            'teaspoon us':        'tsp_us', 'teaspoon uk':       'tsp_uk', 'pintus':          'pt_us',
            'tea spoon us':       'tsp_us', 'tea spoon uk':      'tsp_uk', 'us pint':         'pt_us',
            'teaspoonus':         'tsp_us', 'teaspoonuk':        'tsp_uk', 'us pt':           'pt_us',

            'us table spoon':    'tbsp_us', 'uk table spoon':   'tbsp_uk', 'pt uk':           'pt_uk',
            'us tablespoon':     'tbsp_us', 'uk tablespoon':    'tbsp_uk', 'ptuk':            'pt_uk',
            'ustablespoon':      'tbsp_us', 'uktablespoon':     'tbsp_uk', 'pint uk':         'pt_uk',
            'tablespoon us':     'tbsp_us', 'tablespoon uk':    'tbsp_uk', 'pintuk':          'pt_uk',
            'table spoon us':    'tbsp_us', 'table spoon uk':   'tbsp_uk', 'uk pint':         'pt_uk',
            'tablespoonus':      'tbsp_us', 'tablespoonuk':     'tbsp_uk', 'uk pt':           'pt_uk',

            'fluid oz us':       'floz_us', 'fluid oz uk':       'floz_uk', 'gallon us':     'gal_us',
            'us fluid oz':       'floz_us', 'uk fluid oz':       'floz_uk', 'gal us':        'gal_us',
            'fluidozus':         'floz_us', 'fluidozuk':         'floz_uk', 'gallonus':      'gal_us',
            'usfluidoz':         'floz_us', 'ukfluidoz':         'floz_uk', 'usgallon':      'gal_us',
            'fluid ounce us':    'floz_us', 'fluid ounce uk':    'floz_uk', 'us gallon':     'gal_us',
            'us fluid ounce':    'floz_us', 'uk fluid ounce':    'floz_uk', 'us gal':        'gal_us',
            'fluidounceus':      'floz_us', 'fluidounceuk':      'floz_uk',
            'usfluidounce':      'floz_us', 'ukfluidounce':      'floz_uk',
            'fl oz us':          'floz_us', 'fl oz uk':          'floz_uk', 'gallon uk':     'gal_uk',
            'us fl oz':          'floz_us', 'uk fl oz':          'floz_uk', 'gal uk':        'gal_uk',
            'fl ounce us':       'floz_us', 'fl ounce uk':       'floz_uk', 'gallonuk':      'gal_uk',
            'us fl ounce':       'floz_us', 'uk fl ounce':       'floz_uk', 'ukgallon':      'gal_uk',
            'flounceus':         'floz_us', 'flounceuk':         'floz_uk', 'uk gallon':     'gal_uk',
            'usflounce':         'floz_us', 'ukflounce':         'floz_uk', 'uk gal':        'gal_uk',

            'quarter us':          'qt_us', 'quarter uk':          'qt_uk',
            'qt us':               'qt_us', 'qt uk':               'qt_uk',
            'us quarter':          'qt_us', 'uk quarter':          'qt_uk',
            'usqt':                'qt_us', 'ukqt':                'qt_uk',
            'quarterus':           'qt_us', 'quarteruk':           'qt_uk',
            'us qt':               'qt_us', 'uk qt':               'qt_uk'
        }
        self.volume_units = [u for u in list(Volume.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s') if not from_type.endswith('us') else from_type
        if from_type in list(self.name_conversion_table.values()):
            from_type_ml_value = self.ml_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_ml_value = self.ml_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid volume unit type "{from_type}"')

        value = value * from_type_ml_value

        for i in self.volume_units:
            self.volume.__setattr__(i, value / self.ml_conversion_value_table[i])
        return self.volume


if __name__ == '__main__':
    c = VolumeConverter()
    s = c.convert(120389.14, 'qt us')
    print(s.__dict__)
