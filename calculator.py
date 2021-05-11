from tkinter import (
    Tk, Frame, Spinbox, Scrollbar, TOP, BOTH, N, S, E, W, NSEW
)
from calc_types import (
    ANGLECONVERTER, AREACONVERTER, CURRENCYCONVERTER, DATATRANSFERRATECONVERTER, DATEDIFFERENCE,
    DIGITALSTORAGECONVERTER, ENERGYCONVERTER, LENGTHCONVERTER, POWERCONVERTER, PRESSURECONVERTER, REGULAR, SCIENTIFIC,
    SPEEDCONVERTER, TEMPERATURECONVERTER, TIMECONVERTER, VOLUMECONVERTER, WEIGHTANDMASSCONVERTER
)
from unit_converters import (
    AngleConverterFrame, AreaConverterFrame, CurrencyConverterFrame, DataTransferRateConverterFrame,
    DigitalStorageConverterFrame, EnergyConverterFrame, LengthConverterFrame, PowerConverterFrame,
    PressureConverterFrame, SpeedConverterFrame, TemperatureConverterFrame, TimeConverterFrame, VolumeConverterFrame,
    WeightAndMassConverterFrame
)
# import datedifference
from regular_calculator import RegularCalculator
from scientific_calculator import ScientificCalculator


class Calculator(Frame):
    """
    Main Calculator frame that can be embedded
    into any window. 
    """
    
    def __init__(self, master, _type=REGULAR, **kw):
        """
        Initialize the Calculator frame. This frame contains frames
        for other calculator types.
        
        :param master: Parent widget in which the frame is to be inserted
        :param _type: Calculator type
        """
        Frame.__init__(self, master, **kw)

        self.current_calculator_type = _type
        self.main_frame = Frame(self, bd=1)
        self.main_frame.pack()
        
    def _change_frame(self, frame):
        """
        Change the current calculator type to `frame`
        
        :param frame: name of the calculator frame to be changed into
        """
        pass

    def _load_frame(self, frame):
        pass

    def _remove_frame(self, frame):
        pass

    def get_current(self):
        pass

    def set(self, _type):
        pass

    def close(self):
        del self


def main():
    root = Tk()
    calc = Calculator(root)
    calc.pack(side=TOP, fill=BOTH, expand=True)
    root.after(6000, calc.close)
    root.mainloop()


if __name__ == '__main__':
    main()
