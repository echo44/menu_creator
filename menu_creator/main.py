# -*- coding: utf-8 -*-
import gui_app as ga
from tkinter import *
import functions as fn

try:
    fn.load_menu()
except BaseException:
    pass


root = Tk()
app = ga.Application(root)
root.title("Генератор меню")

root.mainloop()