import tkinter as tk

from tooltip import *


#################################################
# this widget is a translation
#################################################
class Translation(object):
    tooltips = []

    def __init__(self, labels):
        self.labels = labels

    def change_text(self, new_text):
        for t in self.tooltips:
            del t
        self.tooltips.clear()

        for l in self.labels:
            self.create_tooltip(l, new_text)

    def create_tooltip(self, label, new_text):
        tooltip = Tooltip(label, new_text)
        self.tooltips.append(tooltip)
