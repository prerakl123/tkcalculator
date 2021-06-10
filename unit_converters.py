# unit_converters.py
from tkinter import Frame


class AngleConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class AreaConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class CurrencyConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class DataTransferRateConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class DigitalStorageConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class EnergyConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class LengthConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class PowerConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class PressureConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class SpeedConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class TemperatureConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class TimeConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class VolumeConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


class WeightAndMassConverterFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.pack_propagate(0)


CONVERTER_FRAME_CLASSES = [AngleConverterFrame, AreaConverterFrame, CurrencyConverterFrame,
                           DataTransferRateConverterFrame, DigitalStorageConverterFrame, EnergyConverterFrame,
                           LengthConverterFrame, PowerConverterFrame, PressureConverterFrame, SpeedConverterFrame,
                           TemperatureConverterFrame, TimeConverterFrame, VolumeConverterFrame,
                           WeightAndMassConverterFrame]

