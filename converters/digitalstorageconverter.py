class StorageUnits:
    b, Kb, Kib, Mb, Mib, Gb, Gib, Tb, Tib, Pb, Pib, Eb, Eib, Zb, Zib, Yb, Yib, B, KB, KiB, MB, MiB, GB, GiB, TB,\
        TiB, PB, PiB, EB, EiB, ZB, ZiB, YB, YiB = [0]*34


class DigitalStorageConverter:
    def __init__(self):
        self.storage = StorageUnits()
        self.bit_conversion_value_table = {
            'b': 1, 'Kb': 1000, 'Mb': 1000**2, 'Gb': 1000**3, 'Tb': 1000**4, 'Pb': 1000**5, 'Eb': 1000**6,
            'Zb': 1000**7, 'Yb': 1000**8, 'Kib': 1024, 'Mib': 1024**2, 'Gib': 1024**3, 'Tib': 1024**4, 'Pib': 1024**5,
            'Eib': 1024**6, 'Zib': 1024**7, 'Yib': 1024**8,
            'B': 8, 'KB': 8*1000, 'MB': 8*(1000**2), 'GB': 8*(1000**3), 'TB': 8*(1000**4), 'PB': 8*(1000**5),
            'EB': 8*(1000**6), 'ZB': 8*(1000**7), 'YB': 8*(1000**8), 'KiB': 8*1024, 'MiB': 8*(1024**2),
            'GiB': 8*(1024**3), 'TiB': 8*(1024**4), 'PiB': 8*(1024**5), 'EiB': 8*(1024**6), 'ZiB': 8*(1024**7),
            'YiB': 8*(1024**8)
        }
        "Values for the conversion of all the units in bits"
        self.name_conversion_table = {
            'bit': 'b', 'kilobit': 'Kb', 'megabit': 'Mb', 'gigabit': 'Gb', 'terabit': 'Tb', 'petabit': 'Pb',
            'exabit': 'Eb', 'zettabit': 'Zb', 'yottabit': 'Yb', 'kibibit': 'Kib', 'mebibit': 'Mib', 'Gibibit': 'Gib',
            'tebibit': 'Tib', 'pebibit': 'Pb', 'exbibit': 'Eib', 'zebibit': 'Zib', 'yobibit': 'Yib',
            'byte': 'B', 'kilobyte': 'KB', 'megabyte': 'MB', 'gigabyte': 'GB', 'terabyte': 'TB', 'petabyte': 'PB',
            'exabyte': 'EB', 'zettabyte': 'ZB', 'yottabyte': 'YB', 'kibibyte': 'KiB', 'mebibyte': 'MiB',
            'gibibyte': 'GiB', 'tebibyte': 'TiB', 'pebibyte': 'PiB', 'exbibyte': 'EiB', 'zebibyte': 'ZiB',
            'yobibyte': 'YiB'
        }
        "Shortforms for the names of the storage units"
        self.storage_units = [u for u in list(StorageUnits.__dict__.keys()) if not u.startswith('__')]

    def convert(self, value: float, from_type: str) -> StorageUnits:
        from_type = from_type.rstrip('s')
        if from_type in list(self.name_conversion_table.values()):
            from_type_bit_value = self.bit_conversion_value_table[from_type]
        elif from_type.lower() in list(self.name_conversion_table.keys()):
            from_type = self.name_conversion_table[from_type]
            from_type_bit_value = self.bit_conversion_value_table[from_type]
        else:
            raise KeyError(f'Invalid storage unit type "{from_type}"')

        value = value * from_type_bit_value

        for i in self.storage_units:
            self.storage.__setattr__(i, value / self.bit_conversion_value_table[i])
        return self.storage


if __name__ == '__main__':
    c = DigitalStorageConverter()
    s = c.convert(5 * (10 ** 45), 'KiB')
    print(s.__dict__)
