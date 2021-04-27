class DataTransfer:
    bps, Kbps, Kibps, Mbps, Mibps, Gbps, Gibps, Tbps, Tibps, Pbps, Pibps, Ebps, Eibps, Zbps, Zibps, Ybps, Yibps, Bps,\
        KBps, KiBps, MBps, MiBps, GBps, GiBps, TBps, TiBps, PBps, PiBps, EBps, EiBps, ZBps, ZiBps, YBps,\
        YiBps = [0] * 34


class DataTransferRateConverter:
    def __init__(self):
        self.data = DataTransfer()
        self.bitspersecond_value_conversion_table = {
            'bps': 1, 'Kbps': 1000, 'Mbps': 1000 ** 2, 'Gbps': 1000 ** 3, 'Tbps': 1000 ** 4, 'Pbps': 1000 ** 5,
            'Ebps': 1000 ** 6, 'Zbps': 1000 ** 7, 'Ybps': 1000 ** 8, 'Kibps': 1024, 'Mibps': 1024 ** 2,
            'Gibps': 1024 ** 3, 'Tibps': 1024 ** 4, 'Pibps': 1024 ** 5, 'Eibps': 1024 ** 6, 'Zibps': 1024 ** 7,
            'Yibps': 1024 ** 8, 'Bps': 8, 'KBps': 8 * 1000, 'MBps': 8 * (1000 ** 2), 'GBps': 8 * (1000 ** 3),
            'TBps': 8 * (1000 ** 4), 'PBps': 8 * (1000 ** 5), 'EBps': 8 * (1000 ** 6), 'ZBps': 8 * (1000 ** 7),
            'YBps': 8 * (1000 ** 8), 'KiBps': 8 * 1024, 'MiBps': 8 * (1024 ** 2), 'GiBps': 8 * (1024 ** 3),
            'TiBps': 8 * (1024 ** 4), 'PiBps': 8 * (1024 ** 5), 'EiBps': 8 * (1024 ** 6), 'ZiBps': 8 * (1024 ** 7),
            'YiBps': 8 * (1024 ** 8)
        }
        self.name_conversion_table = {
            'bit': 'b', 'kilobit': 'Kb', 'megabit': 'Mb', 'gigabit': 'Gb', 'terabit': 'Tb', 'petabit': 'Pb',
            'exabit': 'Eb', 'zettabit': 'Zb', 'yottabit': 'Yb', 'kibibit': 'Kib', 'mebibit': 'Mib', 'Gibibit': 'Gib',
            'tebibit': 'Tib', 'pebibit': 'Pb', 'exbibit': 'Eib', 'zebibit': 'Zib', 'yobibit': 'Yib',
            'byte': 'B', 'kilobyte': 'KB', 'megabyte': 'MB', 'gigabyte': 'GB', 'terabyte': 'TB', 'petabyte': 'PB',
            'exabyte': 'EB', 'zettabyte': 'ZB', 'yottabyte': 'YB', 'kibibyte': 'KiB', 'mebibyte': 'MiB',
            'gibibyte': 'GiB', 'tebibyte': 'TiB', 'pebibyte': 'PiB', 'exbibyte': 'EiB', 'zebibyte': 'ZiB',
            'yobibyte': 'YiB'
        }

    def convert(self, value: float, from_type: str):
        pass


if __name__ == '__main__':
    c = DataTransferRateConverter()
