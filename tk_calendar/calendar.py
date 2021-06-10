import calendar
import datetime as dt
from tkinter import *


class Calendar(Frame):
    """Calendar widget."""
    date = dt.date
    datetime = dt.datetime
    timedelta = dt.timedelta
    strptime = dt.datetime.strptime
    strftime = dt.datetime.strftime

    def __init__(self, master=None, **kw):
        Frame.__init__(self, master, **kw)
