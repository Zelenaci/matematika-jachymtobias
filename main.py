#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random

# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()

    def generuj(self):
        self.funkce = random.choice([self.plus, self.minus, self.krat, self.deleno])
        self.funkce()
        if self.funkce == self.minus:
            print("jo")
        else:
            print("ne")

    def plus(self):
        # vygeneruje příklad na sčítání
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")

    def minus(self):
        self.lbl.config(text="-")

    def krat(self):
        self.lbl.config(text="*")

    def deleno(self):
        # vygeneruje příklad na celočíselné dělení
        self.cisloB = random.randint(1, 9)
        self.vysledek = random.randint(1, 9)
        self.cisloA = self.cisloB * self.vysledek
        self.lbl.config(text="/")

    def about(self):
        self.plus

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
