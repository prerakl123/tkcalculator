from tkinter import *


class FadingWindow(Toplevel):
    """
    Window with fade in and fade out effects.
    This window is not a regular window. The Windows
    decorators are turned off
    """

    def __init__(self, master, **kw):
        """
        Initialize the fading window to Toplevel
        :param master: parent widget
        """
        Toplevel.__init__(self, master, **kw)
        self.master = master
        # removes the windows decorators
        self.overrideredirect(1)
        # variable to stop or continue transition
        self.stopin = False
        self.stopout = False

    def fadein(self, event=None):
        """

        :param event: passed by functions and binders
        """
        alpha = self.attributes('-alpha')
        alpha += 0.05
        if alpha < 1.0 and self.stopin is False:
            self.attributes('-alpha', alpha)
            self.after(2, self.fadein)
        elif alpha == 1.0:
            self.stopin = True
            self.stopout = False
        self.lift()

    def fadeout(self, event=None):
        """

        :param event: passed by functions and binders
        """
        alpha = self.attributes('-alpha')
        alpha -= 0.05
        if alpha > 0.0 and self.stopout is False:
            self.attributes('-alpha', alpha)
            self.after(2, self.fadeout)
        elif alpha == 0:
            self.stopin = False
            self.stopout = True


class ShrinkingWindow(Toplevel):
    """
     Window with shrink and grow effects
     Windows decorators are turned off
    """

    def __init__(self, master, by_height=False, max_height=500, max_width=500, **kw):
        """
        Initialize the shrinking window.
        if `by_height` is True, shrinks window by height else by width
        upto `max_height` or `max_width` accordingly.

        :param master: parent widget
        :param by_height: shrink by height or width
        :param max_width: maximum width for "growing" window
        :param max_height: maximum height for "growing" window
        """
        Toplevel.__init__(self, master, **kw)
        self.overrideredirect(1)
        self.geometry('500x500')
        self.update_idletasks()
        self.update()

        self.master = master
        self.by_height = by_height
        self.max_height = max_height
        self.max_width = max_width
        self.stopgrow = False
        self.stopshrink = False
        self.org_height = int(self.geometry().split('+')[0].split('x')[0])
        self.org_width = int(self.geometry().split('+')[0].split('x')[1])

    def grow(self, event=None):
        height = int(self.geometry().split('+')[0].split('x')[0])
        width = int(self.geometry().split('+')[0].split('x')[1])
        self.lift()
        if self.by_height:
            height += 22
            if height < self.max_height and self.stopgrow is False:
                self.geometry(f"{width}x{height}")
                self.after(1, self.grow)
            elif height == self.max_height:
                self.geometry(f"{self.max_width}x{height}")
                self.stopgrow = True
                self.stopshrink = False
        else:
            width += 22
            if width < self.max_width and self.stopgrow is False:
                self.geometry(f"{width}x{height}")
                self.after(1, self.grow)
            elif width == self.max_width:
                self.geometry(f"{self.max_width}x{height}")
                self.stopgrow = True
                self.stopshrink = False

    def shrink(self, event=None):
        height = int(self.geometry().split('+')[0].split('x')[0])
        width = int(self.geometry().split('+')[0].split('x')[1])
        if self.by_height:
            height -= 22
            if height > 0 and self.stopshrink is False:
                self.geometry(f"{width}x{height}")
                self.after(1, self.shrink)
            elif height <= 0:
                self.stopgrow = False
                self.stopshrink = True
        else:
            width -= 22
            if width > 0 and self.stopshrink is False:
                self.geometry(f"{width}x{height}")
                self.after(1, self.shrink)
            elif width <= 0:
                self.stopgrow = False
                self.stopshrink = True


class FadingWindowMenu(FadingWindow):
    """
    This class is particularly for the tkcalculator,
    that's why it is inherited as a subclass of FadingWindow
    """

    def __init__(self, master, **kw):
        """
        Initialize the fading window side menu to the
        FadingWindow class which is initialized into the
        Toplevel widget of tkinter.

        :param master: parent widget
        """
        FadingWindow.__init__(self, master, **kw)


def main():
    # def _in(e):
    #     nonlocal visible
    #     visible = True
    #     cl.fadein(e)
    #
    # def _out(e):
    #     nonlocal visible
    #     visible = False
    #     cl.fadeout(e)
    #
    # def showwin(e=None):
    #     nonlocal visible
    #     cl.geometry(f'+{e.x_root+20}+{e.y_root+20}')
    #     if visible is True:
    #         _out(e)
    #     else:
    #         _in(e)
    #
    # visible = False
    # root = Tk()
    # root.geometry('500x500')
    # cl = FadingWindow(root, bg='red')
    # cl.attributes('-alpha', 0)
    # b = Label(root, text='Menu', font=('Consolas 14'))
    # b.bind('<ButtonRelease-1>', showwin)
    # b.pack()
    # root.mainloop()

    def _in(e):
        nonlocal visible
        visible = True
        cl.grow(e)

    def _out(e):
        nonlocal visible
        visible = False
        cl.shrink(e)

    def showwin(e=None):
        nonlocal visible
        cl.geometry(f'+{e.x_root+20}+{e.y_root+20}')
        if visible is True:
            _out(e)
        else:
            _in(e)

    visible = False
    root = Tk()
    root.geometry('500x500')
    cl = ShrinkingWindow(root, bg='red', by_height=True)
    cl.shrink()
    b = Label(root, text='Menu', font=('Consolas 14'))
    b.bind('<ButtonRelease-1>', showwin)
    b.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
