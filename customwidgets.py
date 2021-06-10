# customwidgets.py
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


class ScrollableFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.canvas = Canvas(self, relief=FLAT)
        v_scroll = Scrollbar(self, orient=VERTICAL)
        h_scroll = Scrollbar(self, orient=HORIZONTAL)

        v_scroll.config(command=self.canvas.yview)
        h_scroll.config(command=self.canvas.xview)
        self.canvas.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        v_scroll.pack(side=RIGHT, fill=Y)
        h_scroll.pack(side=BOTTOM, fill=X)
        self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)

        self.widget_frame = Frame(self.canvas)
        self.canvas.create_window(0, 0, window=self.widget_frame, anchor=NW)

        self.bind('<Configure>', self.on_interior_config)
        self.bind_all('<MouseWheel>', self.on_mouse_wheel)

    @staticmethod
    def pack_multiple_widgets(*widgets, **kwargs):
        if len(kwargs.items()) < 1:
            for i in widgets:
                i.pack()
        else:
            for i in widgets:
                i.pack(**kwargs)

    def on_interior_config(self, event=None):
        self.update_idletasks()
        width, height = self.widget_frame.winfo_reqwidth(), self.widget_frame.winfo_reqheight()
        self.canvas.config(scrollregion=(0, 0, width, height))

    def on_mouse_wheel(self, event=None):
        shift_scroll = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift_scroll:
            self.canvas.xview_scroll(scroll, 'units')
        else:
            self.canvas.yview_scroll(scroll, 'units')


class ShrinkingWidthHeightWindow(Toplevel):
    def __init__(self, widget: Widget, speed=5, by_height=False, max_height=500, max_width=500, **kw):
        Toplevel.__init__(self, widget, **kw)
        self.overrideredirect(1)
        self.update_idletasks()
        self.wm_attributes('-topmost', 1)
        self.config(highlightthickness=1, highlightbackground='black')
        widget.focus_force()

        self.visible = False

        self.widget = widget
        self.speed = speed
        self.by_height = by_height
        self.max_height = max_height
        self.max_width = max_width
        self.close_button = Label(self, text=" ✕ Close", font='Helvetica 12', bd=0, anchor=W, relief=FLAT)
        self.close_button.bind('<Enter>', lambda _=None: self.close_button.config(bg='red'))
        self.close_button.bind('<Leave>', lambda _=None: self.close_button.config(bg='white'))
        self.close_button.bind('<ButtonPress-1>', lambda _=None: self.close_button.config(bg='maroon'))
        self.close_button.bind('<ButtonRelease-1>', lambda _=None: [self.close_button.config(bg='white'),
                                                                    self.shrink()])
        self.close_button.pack(side=TOP, fill=X)
        self.widgets_frame = ScrollableFrame(self)
        self.widgets_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.widget.update_idletasks()
        self.geometry(f'0x0+{self.widget.winfo_rootx()}+{self.widget.winfo_rooty()}')
        self.wm_maxsize(max_width, max_height)

    def grow(self, event=None):
        self.widget.update_idletasks()
        self.update_idletasks()
        self.geometry(f'+{self.widget.winfo_rootx()}+{self.widget.winfo_rooty()}')
        self.wm_attributes('-alpha', 1)
        if self.by_height:
            height = self.winfo_height()
            if height >= self.max_height - self.speed:
                height = self.max_height
                self.geometry(f'{self.max_width}x{height}')
                self.widget.focus_force()
                return
            height += self.speed
            self.geometry(f'{self.max_width}x{height}')
        else:
            width = self.winfo_width()
            if width >= self.max_width - self.speed:
                width = self.max_width
                self.geometry(f'{width}x{self.max_height}')
                self.widget.focus_force()
                return
            width += self.speed
            self.geometry(f'{width}x{self.max_height}')
        self.after(1, self.grow)

    def shrink(self, event=None):
        self.widget.update_idletasks()
        self.update_idletasks()
        self.geometry(f'+{self.widget.winfo_rootx()}+{self.widget.winfo_rooty()}')
        if self.by_height:
            height = self.winfo_height()
            if height <= self.speed:
                height = 0
                self.geometry(f'{self.max_width}x{height}')
                self.wm_attributes('-alpha', 0)
                self.widget.focus_force()
                return
            height -= self.speed
            self.geometry(f'{self.max_width}x{height}')
        else:
            width = self.winfo_width()
            if width <= self.speed:
                width = 0
                self.geometry(f'{width}x{self.max_height}')
                self.wm_attributes('-alpha', 0)
                self.widget.focus_force()
                return
            width -= self.speed
            self.geometry(f'{width}x{self.max_height}')
        self.after(1, self.shrink)


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





    # def _in(e):
    #     nonlocal visible
    #     visible = True
    #     cl.grow(e)
    #
    # def _out(e):
    #     nonlocal visible
    #     visible = False
    #     cl.shrink(e)
    #
    # def showwin(e=None):
    #     nonlocal visible
    #     root.update_idletasks()
    #     cl.geometry(f'+{b.winfo_rootx()+2}+{b.winfo_rooty()+25}')
    #     if visible is True:
    #         _out(e)
    #     else:
    #         _in(e)
    #
    # visible = False
    # root = Tk()
    # root.geometry('500x500+0+0')
    # cl = ShrinkingWindow(root, bg='red', by_height=True)
    # cl.shrink()
    # b = Label(root, text='Menu', font=('Consolas 14'))
    # b.bind('<ButtonRelease-1>', showwin)
    # b.pack()
    # root.mainloop()





    # root = Tk()
    # root.geometry('100x100+300+50')
    # b = Button(root, text='OPEN', font='Consolas 12')
    # b.pack(side=LEFT)
    # # ShrinkingWidthHeightWindows(b)
    # wgt_list = []
    # sf = ScrollableFrame(root)
    # sf.pack(side=TOP, fill=BOTH, expand=TRUE)
    # for i in range(100):
    #     btn = Button(sf.widget_frame, text=f'Number {i}', width=100)
    #     wgt_list.append(btn)
    # sf.pack_multiple_widgets(*wgt_list, side=TOP)
    # root.mainloop()





    def cmd(e=None):
        nonlocal visible
        if visible:
            swwh.shrink()
            visible = False
        else:
            swwh.grow()
            visible = True

    visible = False
    root = Tk()
    root.geometry('500x500+200+200')
    btn = Button(root, text='Open', command=cmd)
    btn.pack()
    swwh = ShrinkingWidthHeightWindow(btn, 10, True, 600, 400)
    for i in range(100):
        Button(swwh.widgets_frame.widget_frame, text=f'Button {i}').pack(fill=BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
