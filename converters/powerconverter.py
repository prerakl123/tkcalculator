class Power:
    W, kW, hsp, ftlb, BTU, thm = [0] * 6


class PowerConverter:
    def __init__(self):
        self.power = Power()
        self.watt_conversion_value_table = {
            'W': 1, 'kW': 1000, 'hsp': 745.699, 'ftlb': 0.022597, 'BTU': 17.58427, 'thm': 29307.22
        }
        self.name_conversion_table = {
            'watt': 'W', 'kilowatt': 'kW', 'horsepower': 'hsp', 'footpound': 'ftlb', 'british thermal unit': 'BTU',
            'btu': 'BTU', 'britishthermalunit': 'BTU', 'therm': 'thm', 'us thermal unit': 'thm',
            'usthermalunit': 'thm'
        }
        self.power_units = [u for u in list(Power.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_watt_value = self.watt_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_watt_value = self.watt_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid power unit type "{from_type}"')

        value = value * from_type_watt_value

        for i in self.power:
            self.power.__setattr__(i, value / self.watt_conversion_value_table[i])
        return self.power


if __name__ == '__main__':
    c = PowerConverter()
    s = c.convert(89469124.14, 'kW')
    print(s.__dict__)
