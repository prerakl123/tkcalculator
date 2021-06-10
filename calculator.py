# calculator.py
from threading import Thread
from tkinter import (
    Tk, Frame, Spinbox, Scrollbar, TOP, BOTH, N, S, E, W, NSEW
)
from calculator_types_constants import (
    ANGLECONVERTER, AREACONVERTER, CURRENCYCONVERTER, DATATRANSFERRATECONVERTER, DATEDIFFERENCE,
    DIGITALSTORAGECONVERTER, ENERGYCONVERTER, LENGTHCONVERTER, POWERCONVERTER, PRESSURECONVERTER, REGULAR, SCIENTIFIC,
    SPEEDCONVERTER, TEMPERATURECONVERTER, TIMECONVERTER, VOLUMECONVERTER, WEIGHTANDMASSCONVERTER
)
from unit_converters import (
    AngleConverterFrame, AreaConverterFrame, CurrencyConverterFrame, DataTransferRateConverterFrame,
    DigitalStorageConverterFrame, EnergyConverterFrame, LengthConverterFrame, PowerConverterFrame,
    PressureConverterFrame, SpeedConverterFrame, TemperatureConverterFrame, TimeConverterFrame, VolumeConverterFrame,
    WeightAndMassConverterFrame, CONVERTER_FRAME_CLASSES
)
# import datedifference
from regular_calculator import RegularCalculator
from scientific_calculator import ScientificCalculator


def check_calculator_frame(_type: str) -> Frame:
    for i in CONVERTER_FRAME_CLASSES:
        if _type in i.__name__.rstrip('Frame'):
            return i
    return False


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
        self.config(width=500, height=500, bg='red')
        self.pack_propagate(0)

        self.current_calculator_type = _type
        self.main_frame = Frame(self, bd=1)
        self.main_frame.pack()

        self.current_active_frame: Frame = None
        self.threads = []
        self.key_bind_entries = []
        self._bind_keys()

    def _bind_keys(self):
        key_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<minus>', '<plus>', '<slash>', '<asterisk>',
                    '<equal>', '<BackSpace>', '<period>', '<braceleft>', '<braceright>']
        key_func_list = [self.on_0, self.on_1, self.on_2, self.on_3, self.on_4, self.on_5, self.on_6, self.on_7,
                         self.on_8, self.on_9, self.on_minus, self.on_plus, self.on_slash, self.on_asterisk,
                         self.on_equal, self.on_BackSpace, self.on_period, self.on_braceleft, self.on_braceright]
        for key, key_func in zip(key_list, key_func_list):
            self.bind_all(key, key_func)
        # if self.current_calculator_type
        
    def _change_frame(self, frame):
        """
        Change the current calculator type to `frame`
        
        :param frame: name of the calculator frame to be changed into
        """
        pass

    def _create_threads(self, target_list: list):
        """
        `target_list` should contain a list of dict objects and
        in each dict object there should be three key-value pairs:

        `target`: the target method or function
        `args`:   args for the `target`
        `kwargs`: kwargs for the `target`
        """
        del self.threads
        self.threads = []

        for target in target_list:
            if not isinstance(target['args'], tuple):
                raise ValueError('args for a function should be in a tuple form')
            if not isinstance(target['kwargs'], dict):
                raise ValueError('kwargs for a function should be in a dictionary form')
            if not isinstance(target['target'], object):
                raise ValueError('target should be a function')
            self.threads.append(Thread(target=target['target'], args=target['args'], kwargs=target['kwargs']))

    def _create_widgets(self):
        print('ys')

    def _load_frame(self, frame):
        pass

    def _remove_frame(self, frame):
        pass

    def get_current(self):
        pass

    def on_1(self):
        print(1)

    def on_2(self):
        print(2)

    def on_3(self):
        pass

    def on_4(self):
        pass

    def on_5(self):
        pass

    def on_6(self):
        pass

    def on_7(self):
        pass

    def on_8(self):
        pass

    def on_9(self):
        pass

    def on_0(self):
        pass

    def on_minus(self):
        pass

    def on_plus(self):
        pass

    def on_slash(self):
        pass

    def on_asterisk(self):
        pass

    def on_period(self):
        pass

    def on_equal(self):
        pass

    def on_BackSpace(self):
        pass

    def on_braceleft(self):
        pass

    def on_braceright(self):
        pass

    def set(self, _type):
        pass

    def close(self):
        del self


def main():
    root = Tk()
    root.config(bg='blue')
    lis = [Frame(root).pack()]
    for i in range(70):
        f = Frame(lis[-1], width=500, height=500, bg='red')
        f.pack(side=TOP, fill=BOTH, expand=True)
        f.pack_propagate(0)
        lis.append(f)
    calc = Calculator(lis[-1])
    calc.pack(side=TOP, fill=BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
