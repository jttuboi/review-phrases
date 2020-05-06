import tkinter as tk


#################################################
# this widget is a tooltip
#################################################
class Tooltip(object):

    def __init__(self, widget, text=''):
        self.wait_time = 500  # milliseconds
        self.wrap_length = 180  # pixels
        self.widget = widget
        self.text = tk.StringVar()
        self.text.set(text)
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.showtip)

    def unschedule(self):
        _id = self.id
        self.id = None
        if _id:
            self.widget.after_cancel(_id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a top-level window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw,
                         textvariable=self.text,
                         justify='left',
                         background="#ffffff",
                         relief='solid',
                         borderwidth=1,
                         wraplength=self.wrap_length)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

    def change_text(self, new_text):
        self.text.set(new_text)

    def __del__(self):
        print("deletando ", self.text)