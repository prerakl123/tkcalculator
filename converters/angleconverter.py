import math


class Angle:
    deg, rad, mrad, grad, arcm, arcs = [0] * 6
    circles = 0


class AngleConverter:
    def __init__(self):
        """
        π radians = 180 degrees
        π radians = 200 gradians
        """
        self.angle = Angle()
        self.deg_conversion_value_table = {
            'deg': 1, 'rad': 180 / math.pi, 'mrad': 180 / (1000 * math.pi), 'grad': 180 / 200, 'arcm': 1 / 60,
            'arcs': 1 / 3600
        }
        self.name_conversion_table = {
            'degree':   'deg',
            'radian':   'rad', 'milliradian': 'mrad', 'mradian': 'mrad',
            'gradian': 'grad',

            'second of arc': 'arcs', 'secondofarc': 'arcs', 'arcsec': 'arcs', 'arcsecond': 'arcs', 'arc second': 'arcs',
            'minute of arc': 'arcm', 'minuteofarc': 'arcm', 'arcmin': 'arcm', 'arcminute': 'arcm', 'arc minute': 'arcm'
        }
        self.one_circle_value = {
            'deg': 360, 'rad': 2 * math.pi, 'mrad': 2 * math.pi * 1000, 'grad': 400, 'arcs': 1296000, 'arcm': 21600
        }
        self.angle_units = ['deg', 'rad', 'grad', 'mrad', 'arcs', 'arcm']

    def convert(self, value: float, from_type: str) -> Angle:
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_deg_value = self.deg_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_deg_value = self.deg_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid angle unit type "{from_type}"')

        value = value * from_type_deg_value

        for i in self.angle_units:
            self.angle.__setattr__(i, value / self.deg_conversion_value_table[i])
        self.angle.circles = round(value / self.one_circle_value[from_type], 2)
        return self.angle


if __name__ == '__main__':
    c = AngleConverter()
    s = c.convert(9000, 'grad')
    print(s.__dict__)
