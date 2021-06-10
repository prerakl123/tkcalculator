# from idlelib.colorizer import ColorDelegator, color_config
# from idlelib.percolator import Percolator
# from tkinter import *
#
# root = Tk()
# text = Text(root)
# text.pack()
# # color_config(text)
# Percolator(text).insertfilter(ColorDelegator())
# mainloop()



















# from_date = '2020-01-02'
# from_date = from_date.split('-') if '-' in from_date else from_date.split('/') if '/' in from_date else \
#     from_date.split()
# print(from_date)
# from_date = '2020/01/02'
# from_date = from_date.split('-') if '-' in from_date else from_date.split('/') if '/' in from_date else \
#     from_date.split()
# print(from_date)
# from_date = '2020 Apr 12'
# from_date = from_date.split('-') if '-' in from_date else from_date.split('/') if '/' in from_date else \
#     from_date.split()
# print(from_date)































# Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> 10**-50
# 1e-50
# >>> s = '120e-9'
# >>> decial = s.split('e')
# >>> format(((float(decial[0]))*(10**int(decial[1]))), '.8f')
# '0.00000012'
# >>> s = '120e-09'
# >>> decial = s.split('e')
# >>> format(((float(decial[0]))*(10**int(decial[1]))), '.8f')
# '0.00000012'
# >>> type(format(((float(decial[0]))*(10**int(decial[1]))), '.8f'))
# <class 'str'>
# >>> type(float(format(((float(decial[0]))*(10**int(decial[1]))), '.8f')))
# <class 'float'>
# >>> float(format(((float(decial[0]))*(10**int(decial[1]))), '.8f'))
# 1.2e-07
# >>> float(24000000)
# 24000000.0
# >>> float(2400000000000000000000)
# 2.4e+21
# >>> float(24000000000000000)
# 2.4e+16
# >>> float(240000000000)
# 240000000000.0
# >>> float(2400000000000)
# 2400000000000.0
# >>> float(24000000000000)
# 24000000000000.0
# >>> float(240000000000000)
# 240000000000000.0
# >>> float(2400000000000000)
# 2400000000000000.0
# >>> float(24000000000000000)
# 2.4e+16
# >>> print("%e" % 10**100)
# 1.000000e+100
# >>> print("%e" % 4.5*10**100)
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     print("%e" % 4.5*10**100)
# OverflowError: cannot fit 'int' into an index-sized integer
# >>> print("%e" % 4.5*(10**100))
# Traceback (most recent call last):
#   File "<pyshell#21>", line 1, in <module>
#     print("%e" % 4.5*(10**100))
# OverflowError: cannot fit 'int' into an index-sized integer
# >>> print("%e" % 1**100)
# 1.000000e+00
# >>> print("%e" % 10**1000)
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     print("%e" % 10**1000)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**500)
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     print("%e" % 10**500)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**400)
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     print("%e" % 10**400)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**200)
# 1.000000e+200
# >>> print("%e" % 10**300)
# 1.000000e+300
# >>> print("%e" % 10**360)
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     print("%e" % 10**360)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**350)
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     print("%e" % 10**350)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**330)
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     print("%e" % 10**330)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**320)
# Traceback (most recent call last):
#   File "<pyshell#31>", line 1, in <module>
#     print("%e" % 10**320)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**310)
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     print("%e" % 10**310)
# OverflowError: int too large to convert to float
# >>> print("%e" % 10**302)
# 1.000000e+302
# >>> print("%e" % 10**303)
# 1.000000e+303
# >>> print("%e" % 10**305)
# 1.000000e+305
# >>> print("%e" % 10**307)
# 1.000000e+307
# >>> print("%e" % 10**308)
# 1.000000e+308
# >>> print("%e" % 10**309)
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     print("%e" % 10**309)
# OverflowError: int too large to convert to float
# >>> import decimal as d
# >>> h = d.Decimal('10**309')
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     h = d.Decimal('10**309')
# decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
# >>> h = d.Decimal(10**309)
# >>> h.exp
# <built-in method exp of decimal.Decimal object at 0x000001E8834AC7A0>
# >>> h.exp()
# Traceback (most recent call last):
#   File "<pyshell#43>", line 1, in <module>
#     h.exp()
# decimal.Overflow: [<class 'decimal.Overflow'>]
# >>> h
# Decimal('1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
# >>> format(h, '.6e')
# '1.000000e+309'
# >>> format(h, '.8f')
# '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.00000000'
# >>> format(h, '.3e')
# '1.000e+309'
# >>> format(h, '.4e')
# '1.0000e+309'
# >>> h = d.Decimal(5*10**309)
# >>> h = d.Decimal(4.5*(10**309))
# Traceback (most recent call last):
#   File "<pyshell#50>", line 1, in <module>
#     h = d.Decimal(4.5*(10**309))
# OverflowError: int too large to convert to float
# >>> h = d.Decimal(4.5*(10**109))
# >>> format(h, '.4e')
# '4.5000e+109'
# >>> format(h, '.4d')
# Traceback (most recent call last):
#   File "<pyshell#53>", line 1, in <module>
#     format(h, '.4d')
# ValueError: invalid format string
# >>> format(h, '.4f')
# '44999999999999996054401922698028506882896851942671915240757339993667745517598509633596438973283938845486743552.0000'
# >>> format(h, '.4g')
# '4.500e+109'
# >>> format(h, '.5g')
# '4.5000e+109'
# >>> format(h, '.5h')
# Traceback (most recent call last):
#   File "<pyshell#57>", line 1, in <module>
#     format(h, '.5h')
# ValueError: invalid format string
# >>> format(h, '.5i')
# Traceback (most recent call last):
#   File "<pyshell#58>", line 1, in <module>
#     format(h, '.5i')
# ValueError: invalid format string
# >>> format(h, '.5a')
# Traceback (most recent call last):
#   File "<pyshell#59>", line 1, in <module>
#     format(h, '.5a')
# ValueError: invalid format string
# >>> format(h, '.4b')
# Traceback (most recent call last):
#   File "<pyshell#60>", line 1, in <module>
#     format(h, '.4b')
# ValueError: invalid format string
# >>> format(h, '.4c')
# Traceback (most recent call last):
#   File "<pyshell#61>", line 1, in <module>
#     format(h, '.4c')
# ValueError: invalid format string
# >>> format(h, '.4d')
# Traceback (most recent call last):
#   File "<pyshell#62>", line 1, in <module>
#     format(h, '.4d')
# ValueError: invalid format string
# >>> format(h, '.4e')
# '4.5000e+109'
# >>> format(h, '.4f')
# '44999999999999996054401922698028506882896851942671915240757339993667745517598509633596438973283938845486743552.0000'
# >>> format(h, '.4g')
# '4.500e+109'
# >>> format(h, '.8g')
# '4.5000000e+109'
# >>> format(h, '.85')
# '4.499999999999999605440192269802850688289685194267191524075733999366774551759850963360E+109'
# >>> format(h, '.5g')
# '4.5000e+109'
# >>>

































# import time
# import multiprocessing
#
#
# def calc_square(numbers):
#     for i in numbers:
#         time.sleep(3)  # artificial time-delay
#         print('square: ', str(i * i))
#
#
# def calc_cube(numbers):
#     for i in numbers:
#         time.sleep(3)
#         print('cube: ', str(i * i * i))
#
#
# if __name__ == "__main__":
#     arr = [2, 3, 8, 9]
#     p1 = multiprocessing.Process(target=calc_square, args=(arr,))
#     p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
#     # creating two Process here p1 & p2
#     p1.start()
#     p2.start()
#     # starting Processes here parallel by using start function.
#     p1.join()
#     # this join() will wait until the calc_square() function is finished.
#     p2.join()
#     # this join() will wait unit the calc_cube() function is finished.
#     print("Successes!")



























# import time
# import threading
#
#
# def calc_square(numbers):
#     print("Calculate square numbers: ")
#     for i in numbers:
#         time.sleep(2)  # artificial time-delay
#         print('square: ', str(i * i))
#
#
# def calc_cube(numbers):
#     print("Calculate cube numbers: ")
#     for i in numbers:
#         time.sleep(2)
#         print('cube: ', str(i * i * i))
#
#
# if __name__ == "__main__":
#     arr = [2, 3, 8, 9]
#     t1 = threading.Thread(target=calc_square, args=(arr,))
#     t2 = threading.Thread(target=calc_cube, args=(arr,))
#     # creating two threads here t1 & t2
#     t1.start()
#     t2.start()
#     # starting threads here parallel by using start function.
#     t1.join()
#     # this join() will wait until the cal_square() function is finished.
#     t2.join()
#     # this join() will wait unit the cal_cube() function is finished.
#     print("Successes!")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #     MULTI PROCESSING     # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import time
# from converters import CurrencyConverter
# from converters import DigitalStorageConverter
# import multiprocessing
#
# c_con = CurrencyConverter()
# ds_con = DigitalStorageConverter()
#
#
# def ask_conversion():
#     val_list = [[7692436, 'KB'], [152894, 'GB'], [89523, 'MiB'], [714689, 'B'], [69746823, 'PB'],
#                 [72589256784296, 'b'], [6489231, 'Kib'], [564295, 'TB'], [6358923, 'GiB'], [57265944, 'EiB'],
#                 [6258936893, 'Eib'], [6589235440, 'PiB'], [89576237523590, 'Gib'], [6258936203560, 'EB'],
#                 [1092741856, 'Tib']]
#     for values in val_list:
#         val, unit1 = float(values[0]), values[1]
#         conv = ds_con.convert(val, unit1)
#         time.sleep(2)
#         print(conv.__dict__)
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=ask_conversion)
#     p2 = multiprocessing.Process(target=c_con.update_currencies,)
#     p1.start()
#     p2.start()
#     print('that\'s done')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #     MULTI PROCESSING     # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# from converters.deletethis import abcd
# abcd()






# import os
# from converters import CurrencyConverter
#
# c = CurrencyConverter()
# c.update_currencies(os.getcwd() + '\\converters\\currencies')
























# lis = ['area', 'currency', 'datatransferrate', 'digitalstorage', 'energy', 'length', 'power', 'pressure', 'speed',
#        'temperature', 'time', 'volume', 'weightandmass']
#
# for i in lis:
#     with open(f'data/{i}_b64_UNICODE_bw', 'w') as bw_file, open(f'data/{i}_b64_UNICODE_color', 'w') as col_file:
#         print(f'{i} done')





























# import tkinter as tk
#
#
# def callback(detail):
#     print("detail: %s" % detail)
#
#
# def create_custom_event():
#     root.event_generate("<<Custom>>", data="Hello, world")
#
#
# root = tk.Tk()
#
# button = tk.Button(root, text="click me", command=create_custom_event)
# button.pack(side="top", padx=20, pady=20)
#
# cmd = root.register(callback)
# root.tk.call("bind", root, "<<Custom>>", cmd + " %d")
#
# root.mainloop()





































# import calendar
# import tkinter as tk
# import time
# from tkinter import ttk
#
#
# class MyDatePicker(tk.Toplevel):
#     """
#     Description:
#         A tkinter GUI date picker.
#     """
#
#     def __init__(self, widget=None, format_str=None):
#         """
#         :param widget: widget of parent instance.
#
#         :param format_str: print format in which to display date.
#         :type format_str: string
#
#         Example::
#             a = MyDatePicker(self, widget=self.parent widget,
#                              format_str='%02d-%s-%s')
#         """
#
#         super().__init__()
#         self.widget = widget
#         self.str_format = format_str
#
#         self.title("Date Picker")
#         self.resizable(0, 0)
#         self.geometry("+630+390")
#
#         self.init_frames()
#         self.init_needed_vars()
#         self.init_month_year_labels()
#         self.init_buttons()
#         self.space_between_widgets()
#         self.fill_days()
#         self.make_calendar()
#
#     def init_frames(self):
#         self.frame1 = tk.Frame(self)
#         self.frame1.pack()
#
#         self.frame_days = tk.Frame(self)
#         self.frame_days.pack()
#
#     def init_needed_vars(self):
#         self.month_names = tuple(calendar.month_name)
#         self.day_names = tuple(calendar.day_abbr)
#         self.year = time.strftime("%Y")
#         self.month = time.strftime("%B")
#
#     def init_month_year_labels(self):
#         self.year_str_var = tk.StringVar()
#         self.month_str_var = tk.StringVar()
#
#         self.year_str_var.set(self.year)
#         self.year_lbl = tk.Label(self.frame1, textvariable=self.year_str_var,
#                                  width=3)
#         self.year_lbl.grid(row=0, column=5)
#
#         self.month_str_var.set(self.month)
#         self.month_lbl = tk.Label(self.frame1, textvariable=self.month_str_var,
#                                   width=8)
#         self.month_lbl.grid(row=0, column=1)
#
#     def init_buttons(self):
#         self.left_yr = ttk.Button(self.frame1, text="←", width=5,
#                                   command=self.prev_year)
#         self.left_yr.grid(row=0, column=4)
#
#         self.right_yr = ttk.Button(self.frame1, text="→", width=5,
#                                    command=self.next_year)
#         self.right_yr.grid(row=0, column=6)
#
#         self.left_mon = ttk.Button(self.frame1, text="←", width=5,
#                                    command=self.prev_month)
#         self.left_mon.grid(row=0, column=0)
#
#         self.right_mon = ttk.Button(self.frame1, text="→", width=5,
#                                     command=self.next_month)
#         self.right_mon.grid(row=0, column=2)
#
#     def space_between_widgets(self):
#         self.frame1.grid_columnconfigure(3, minsize=40)
#
#     def prev_year(self):
#         self.prev_yr = int(self.year_str_var.get()) - 1
#         self.year_str_var.set(self.prev_yr)
#
#         self.make_calendar()
#
#     def next_year(self):
#         self.next_yr = int(self.year_str_var.get()) + 1
#         self.year_str_var.set(self.next_yr)
#
#         self.make_calendar()
#
#     def prev_month(self):
#         index_current_month = self.month_names.index(self.month_str_var.get())
#         index_prev_month = index_current_month - 1
#
#         #  index 0 is empty string, use index 12 instead,
#         # which is index of December.
#         if index_prev_month == 0:
#             self.month_str_var.set(self.month_names[12])
#         else:
#             self.month_str_var.set(self.month_names[index_current_month - 1])
#
#         self.make_calendar()
#
#     def next_month(self):
#         index_current_month = self.month_names.index(self.month_str_var.get())
#
#         try:
#             self.month_str_var.set(self.month_names[index_current_month + 1])
#         except IndexError:
#             #  index 13 does not exist, use index 1 instead, which is January.
#             self.month_str_var.set(self.month_names[1])
#
#         self.make_calendar()
#
#     def fill_days(self):
#         col = 0
#         #  Creates days label
#         for day in self.day_names:
#             self.lbl_day = tk.Label(self.frame_days, text=day)
#             self.lbl_day.grid(row=0, column=col)
#             col += 1
#
#     def make_calendar(self):
#         #  Delete date buttons if already present.
#         #  Each button must have its own instance attribute for this to work.
#         try:
#             for dates in self.m_cal:
#                 for date in dates:
#                     if date == 0:
#                         continue
#
#                     self.delete_buttons(date)
#
#         except AttributeError:
#             pass
#
#         year = int(self.year_str_var.get())
#         month = self.month_names.index(self.month_str_var.get())
#         self.m_cal = calendar.monthcalendar(year, month)
#
#         #  build dates buttons.
#         for dates in self.m_cal:
#             row = self.m_cal.index(dates) + 1
#             for date in dates:
#                 col = dates.index(date)
#
#                 if date == 0:
#                     continue
#
#                 self.make_button(str(date), str(row), str(col))
#
#     def make_button(self, date, row, column):
#         """
#         Description:
#             Build a date button.
#
#         :param date: date.
#         :type date: string
#
#         :param row: row number.
#         :type row: string
#
#         :param column: column number.
#         :type column: string
#         """
#         exec(
#             "self.btn_" + date + " = ttk.Button(self.frame_days, text=" + date
#             + ", width=5)\n"
#             "self.btn_" + date + ".grid(row=" + row + " , column=" + column
#             + ")\n"
#             "self.btn_" + date + ".bind(\"<Button-1>\", self.get_date)"
#         )
#
#     def delete_buttons(self, date):
#         """
#         Description:
#             Delete a date button.
#
#         :param date: date.
#         :type: string
#         """
#         exec(
#             "self.btn_" + str(date) + ".destroy()"
#         )
#
#     def get_date(self, clicked=None):
#         """
#         Description:
#             Get the date from the calendar on button click.
#
#         :param clicked: button clicked event.
#         :type clicked: tkinter event
#         """
#
#         clicked_button = clicked.widget
#         year = self.year_str_var.get()
#         month = self.month_str_var.get()
#         date = clicked_button['text']
#
#         self.full_date = self.str_format % (date, month, year)
#         print(self.full_date)
#         #  Replace with parent 'widget' of your choice.
#         try:
#             self.widget.delete(0, tk.END)
#             self.widget.insert(0, self.full_date)
#         except AttributeError:
#             pass
#
#
# if __name__ == '__main__':
#     def application():
#         MyDatePicker(format_str='%02d-%s-%s')
#
#     root = tk.Tk()
#     btn = tk.Button(root, text="test", command=application)
#     btn.pack()
#     root.mainloop()
