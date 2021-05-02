class Time:
    ns, us, ms, s, min, hr, day, week, month, year, decade, century = [0] * 12


class TimeConverter:
    def __init__(self):
        self.time = Time()
        self.ns_conversion_value_table = {
            'ns':      1, 'day':      8.64e+13, 'us':    1000, 'week':     6.048e+14,
            'ms':   1e+6, 'month':   2.628e+15, 's':     1e+9, 'year':    3.1536e+16,
            'min': 6e+10, 'decade': 3.1536e+17, 'hr': 3.6e+12, 'century': 3.1536e+18

        }
        self.name_conversion_table = {
            'nanosecond':  'ns', 'microsecond':  'us', 'millisecond':  'ms', 'second': 's',
            'nano second': 'ns', 'micro second': 'us', 'milli second': 'ms',
            'nanosec':     'ns', 'microsec':     'us', 'millisec':     'ms', 'sec': 's',

            'minute':  'min', 'mth':        'month',
            'hour':     'hr', 'yr':          'year',
            'day':     'day', 'dec':       'decade',
            'week':   'week', 'cent':     'century',
            'month': 'month', 'centurie': 'century'
        }
        self.time_units = [u for u in list(Time.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str):
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_ns_value = self.ns_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_ns_value = self.ns_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid time unit type "{from_type}"')

        value = value * from_type_ns_value

        for i in self.time_units:
            self.time.__setattr__(i, value / self.ns_conversion_value_table[i])
        return self.time


if __name__ == '__main__':
    c = TimeConverter()
    s = c.convert(1892476.342, 'yrs')
    print(s.__dict__)
