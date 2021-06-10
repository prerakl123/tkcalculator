# __main__.py
from calculator import *
from customwidgets import ShrinkingWidthHeightWindow


class SlideMenu(ShrinkingWidthHeightWindow):
    pass


class CalculatorApplication(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.menu_frame = Frame(self)
        menu_window = SlideMenu(self)


def main():
    root = CalculatorApplication()
    root.mainloop()


if __name__ == '__main__':
    main()
