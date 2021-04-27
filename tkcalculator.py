from tkinter import *
from calc_types import *
from converters import *
import datedifference


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
        self.main_frame = Frame(self, bd=1)
        self.main_frame.pack()
        
    def change_frame(self, frame):
        """
        Change the current calculator type to `frame`
        
        :param frame: name of the calculator frame to be changed into
        """
        pass
