# -*- coding: utf-8 -*-
from tkinter import *
import functions as fn

#view


class Application(Frame):
    """Make GUI"""
    def __init__(self, master):
        super(Application, self).__init__()
        self.gen_menu = Button(self, text="Сгенерить меню на день",
        command=fn.make_menu)
        self.show_menu = Button(self, text="Посмотреть все меню",
        command=fn.show_menu)
        self.add_dish = Button(self, text="Добавить блюдо", command=fn.add_dish)
        self.del_dish = Button(self, text="Удалить блюдо", command=fn.del_dish)
        self.set_buttons()
        self.grid()

    def set_buttons(self):
        """Set layout"""
        self.gen_menu.pack(fill=X)
        self.show_menu.pack(fill=X)
        self.add_dish.pack(fill=X)
        self.del_dish.pack(fill=X)