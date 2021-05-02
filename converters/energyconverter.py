class Energy:
    J, kJ, Cal, kCal, Wh, kWh, eV, BTU, thm, ftlb = [0] * 10


class EnergyConverter:
    def __init__(self):
        self.energy = Energy()
        self.joule_conversion_value_table = {
            'J':                 1, 'kJ':       1000, 'Cal':   4.184, 'kCal':    4184, 'Wh':      3600,
            'kWh': 3.6 * (10 ** 6), 'eV': 1.6022e-19, 'BTU': 1055.06, 'thm': 1.055e+8, 'ftlb': 1.35582
        }
        "Values for the conversion of all the units in joules"
        self.name_conversion_table = {
            'joule':          'J', 'kilocalorie':  'kCal', 'electron-volt':         'eV', 'foot-pound': 'ftlb',
            'kilojoule':     'kJ', 'watt-hour':      'Wh', 'electronvolt':          'eV', 'foot.pound': 'ftlb',
            'calorie':      'Cal', 'watthour':       'Wh', 'british thermal unit': 'BTU', 'footpound':  'ftlb',
            'gram.calorie': 'Cal', 'watt.hour':      'Wh', 'britishthermalunit':   'BTU', 'foot pound': 'ftlb',
            'gram calorie': 'Cal', 'kilowatthour':  'kWh', 'us therm':             'thm',
            'gramcalorie':  'Cal', 'kilowatt.hour': 'kWh', 'ustherm':              'thm',
            'gram-calorie': 'Cal', 'kilowatt-hour': 'kWh', 'therm':                'thm'
        }
        "Short forms of all the units"
        self.energy_units = [i for i in list(Energy.__dict__.keys()) if not i.startswith('__')]

    def convert(self, value: float, from_type: str) -> Energy:
        from_type = from_type.rstrip('s')
        if from_type in list(self.joule_conversion_value_table.keys()):
            from_type_joule_value = self.joule_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_joule_value = self.joule_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid energy unit type "{from_type}"')

        value = value * from_type_joule_value

        for i in self.energy_units:
            self.energy.__setattr__(i, value / self.joule_conversion_value_table[i])
        return self.energy


if __name__ == '__main__':
    c = EnergyConverter()
    s = c.convert(4500.50, 'kJs')
    print(s.__dict__)
