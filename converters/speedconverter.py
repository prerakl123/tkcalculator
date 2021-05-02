class Speed:
    mmps, cmps, dmps, mps, damps, hmps, kmps, ftps, Mps, mmpm, cmpm, dmpm, mpm, dampm, hmpm, kmpm, ftpm, Mpm, mmph, \
        cmph, dmph, mph, damph, hmph, kmph, ftph, Mph, knot = [0] * 28


class SpeedConverter:
    def __init__(self):
        self.speed = Speed()
        self.mmps_conversion_value_table = {
            'mmps':     1, 'ftps':      304.8, 'hmpm':  1666.66667, 'mph':   0.277778,
            'cmps':    10, 'Mps':    1.609e+6, 'kmpm': 16666.66667, 'damph':  2.77778,
            'dmps':   100, 'mmpm':  0.0166667, 'ftpm':        5.08, 'hmph':  27.77778,
            'mps':   1000, 'cmpm':   0.166667, 'Mpm':      26822.4, 'kmph': 277.77778,
            'damps': 1e+4, 'dmpm':    1.66667, 'mmph': 0.000277778, 'ftph': 0.0846667,
            'hmps':  1e+5, 'mpm':    16.66667, 'cmph':  0.00277778, 'Mph':     447.04,
            'kmps':  1e+6, 'dampm': 166.66667, 'dmph':   0.0277778, 'knot':   514.444
        }
        self.name_conversion_table = {
            'millimeter per second': 'mmps', 'millimeterpersecond': 'mmps', 'millimeter per minute': 'mmpm',
            'millimeterperminute':   'mmpm', 'millimeter per hour': 'mmph', 'millimeterperhour':     'mmph',
            'centimeter per second': 'cmps', 'centimeterpersecond': 'cmps', 'centimeter per minute': 'cmpm',
            'centimeterperminute':   'cmpm', 'centimeter per hour': 'cmph', 'centimeterperhour':     'cmph',
            'decimeter per second':  'dmps', 'decimeterpersecond':  'dmps', 'decimeter per minute':  'dmpm',
            'decimeterperminute':    'dmpm', 'decimeter per hour':  'dmph', 'decimeterperhour':      'dmph',
            'meter per second':       'mps', 'meterpersecond':       'mps', 'meter per minute':       'mpm',
            'meterperminute':         'mpm', 'meter per hour':       'mph', 'meterperhour':           'mph',
            'decameter per second': 'damps', 'decameterpersecond': 'damps', 'decameter per minute': 'dampm',
            'decameterperminute':   'dampm', 'decameter per hour': 'damph', 'decameterperhour':     'damph',
            'hectometer per second': 'hmps', 'hectometerpersecond': 'hmps', 'hectometer per minute': 'hmpm',
            'hectometerperminute':   'hmpm', 'hectometer per hour': 'hmph', 'hectometerperhour':     'hmph',
            'kilometer per second':  'kmps', 'kilometerpersecond':  'kmps', 'kilometer per minute':  'kmpm',
            'kilometerperminute':    'kmpm', 'kilometer per hour':  'kmph', 'kilometerperhour':      'kmph',
            'foot per second':       'ftps', 'footpersecond':       'ftps', 'foot per minute':       'ftpm',
            'footperminute':         'ftpm', 'foot per hour':       'ftph', 'footperhour':           'ftph',
            'mile per second':        'Mps', 'milepersecond':        'Mps', 'mile per minute':        'Mpm',
            'mileperminute':          'Mpm', 'mile per hour':        'Mph', 'mileperhour':            'Mph',
            'knot': 'knot'
        }
        self.speed_units = [u for u in list(Speed.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_mmps_value = self.mmps_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_mmps_value = self.mmps_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid speed unit type "{from_type}"')

        value = value * from_type_mmps_value

        for i in self.speed_units:
            self.speed.__setattr__(i, value / self.mmps_conversion_value_table[i])
        return self.speed


if __name__ == '__main__':
    c = SpeedConverter()
    s = c.convert(9834712.123, 'ftpm')
    print(s.__dict__)
