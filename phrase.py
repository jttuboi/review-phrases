import tkinter as tk
from effects import *
from tkinter import ttk


#################################################
# this widget is a label
#################################################
class Phrase(object):
    labels = []

    def __init__(self, widget, first_full_phrase=''):
        self.widget = widget

        self.create_label(first_full_phrase)

        # self.change_text("aaaa, bbbb, cccc.")
        # self.change_text("*aaaa*, bbbb, cccc.")
        # self.change_text("aaaa, *bbbb*, cccc.")
        # self.change_text("aaaa, bbbb, *cccc.*")
        # self.change_text("*aaaa, bbbb, cccc.*")
        # self.change_text("*aaaa*, *bbbb*, cccc.")
        # self.change_text("*aaaa*, bbbb, *cccc.*")
        # self.change_text("*aaaa*, *bbbb*, *cccc.*")

    def change_text(self, new_full_phrase):
        strings = split(new_full_phrase)

        for l in self.labels:
            l.pack_forget()
        self.labels.clear()

        for s in strings:
            self.create_label(s.get("string"), font=s.get("font"))

    def create_label(self, phrase, font=Font.NORMAL):
        label = tk.Label(self.widget,
                         text=phrase,
                         justify=tk.LEFT,
                         background="#66ff66",
                         font=font.value)
        label.pack(side="left")
        self.labels.append(label)
