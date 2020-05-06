import csv
from phrase import *
from translation import *
from random import choices


class Main:
    items = []
    root = None

    def __init__(self, root):
        self.root = root
        self.phrase = Phrase(self.root, "first phrase")
        self.translation = Translation(self.phrase.labels)

        # self.button = Button(self.root, text="change", command=self.change)
        # self.button.pack()

        self.open_csv()
        self.change()

    def open_csv(self):
        with open("data.csv", encoding="utf-8") as csv_file:
            values = csv.reader(csv_file, delimiter=";")
            for v in values:
                self.items.append(v)

    def change(self):
        item = choices(self.items)[0]
        self.phrase.change_text(item[0])
        self.translation.change_text(item[1])

        self.root.after(5000, self.change)
