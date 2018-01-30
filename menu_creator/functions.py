# -*- coding: utf-8 -*-
import vk_api
import menu
import random
import os
import pickle
from tkinter import *

#controller


def make_menu():
    """Making menu"""

    def vk_window():
        """Make window for VK"""
        def send():
            """Sending menu 2 vk"""
            l = login.get()
            p = password.get()
            menu = text.get("1.0", END)
            send_2_vk(l, p, menu)
            login.delete(0, END)
            password.delete(0, END)

        log = StringVar()
        passwd = StringVar()
        vk = Toplevel()
        vk.title("Отправляем ингридиенты в ВК")
        login_label = Label(vk, text="Логин")
        pass_label = Label(vk, text="Пароль")
        login = Entry(vk, textvariable=log)
        password = Entry(vk, show="*", textvariable=passwd)
        b = Button(vk, text="Отправить ингридиенты в ВК", command=send)
        login_label.grid(row=0, column=0)
        pass_label.grid(row=1, column=0)
        login.grid(row=0, column=1, padx=5, pady=5)
        password.grid(row=1, column=1, padx=5, pady=5)
        b.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    def reroll_menu():
        """Reroll menu"""
        menu = make_rand_menu()
        text.delete('1.0', END)
        text.insert(END, menu)

    win = Toplevel()
    win.title("Твое меню")
    menu_4_day = make_rand_menu()
    text = Text(win, height=20, width=45)
    text.pack()
    text.insert(END, menu_4_day)

    b = Button(win, text="Отправить ингридиенты в ВК", command=vk_window)
    b.pack(side="bottom")

    b2 = Button(win, text="Сгенерить другое меню", command=reroll_menu)
    b2.pack(side="bottom")


def show_menu():
    """Show menu"""
    win = Toplevel()
    win.title("Все меню")
    menu_4_day = print_menu()
    text = Text(win)
    text.pack()
    text.insert(END, menu_4_day)


def add_dish():
    """Adding dish"""

    def show_suc_win():
        """Show good window"""
        suc = Toplevel()
        suc.title("УСПЕШНО")
        suc.geometry("300x100")
        Button(suc, text="Ok", command=suc.destroy).pack(side="bottom")
        Label(suc, text="Блюдо успешно добавлно в меню").pack()

    def addition():
        """Add new dish 2 menu"""
        c = cat_ent.get()
        n = name_ent.get()
        i = ing_text.get("1.0", 'end-1c')

        if (c.lower() == "завтрак"):
            menu.breakfast[n] = i
            show_suc_win()

        elif (c.lower() == "обед"):
            menu.dinner[n] = i
            show_suc_win()

        elif (c.lower() == "ужин"):
            menu.supper[n] = i
            show_suc_win()

        else:
            err = Toplevel()
            err.title("ОШИБКА")
            err.geometry("300x100")
            Button(err, text="Ok", command=err.destroy).pack(side="bottom")
            Label(err, text="""Категория должна быть:
            затрак, обед или ужин""").pack()

        pickle_menu()

    category = StringVar()
    name = StringVar()
    win = Toplevel()
    win.title("Добавляем блюда в меню")

    cat_label = Label(win, text="Категория")
    name_label = Label(win, text="Название")
    ing_label = Label(win, text="Ингридиенты")

    cat_ent = Entry(win, textvariable=category)
    name_ent = Entry(win, textvariable=name)

    ing_text = Text(win)

    b = Button(win, text="Добавить блюдо в меню", command=addition)

    cat_label.grid(row=0, column=0)
    name_label.grid(row=1, column=0)
    ing_label.grid(row=2, column=0)

    cat_ent.grid(row=0, column=1, padx=5, pady=5)
    name_ent.grid(row=1, column=1, padx=5, pady=5)
    ing_text.grid(row=2, column=1)
    b.grid(row=3, column=0, padx=5, pady=5, sticky="e")


def del_dish():
    """Deleting dish"""

    def show_suc_win():
        """Show good window"""
        suc = Toplevel()
        suc.title("УСПЕШНО")
        suc.geometry("300x100")
        Button(suc, text="Ok", command=suc.destroy).pack(side="bottom")
        Label(suc, text="Блюдо успешно удалено из меню").pack()

    def delete():
        """Delete dish from menu"""
        c = cat_ent.get()
        n = name_ent.get()

        if (c.lower() == "завтрак"):
            menu.breakfast.pop(n)
            show_suc_win()

        elif (c.lower() == "обед"):
            menu.dinner.pop(n)
            show_suc_win()

        elif (c.lower() == "ужин"):
            menu.supper.pop(n)
            show_suc_win()

        else:
            err = Toplevel()
            err.title("ОШИБКА")
            err.geometry("300x100")
            Button(err, text="Ok", command=err.destroy).pack(side="bottom")
            Label(err, text="""Категория должна быть:
            затрак, обед или ужин""").pack()

        pickle_menu()

    category = StringVar()
    name = StringVar()
    win = Toplevel()
    win.title("Удаляем блюда из меню")

    cat_label = Label(win, text="Категория")
    name_label = Label(win, text="Название")

    cat_ent = Entry(win, textvariable=category)
    name_ent = Entry(win, textvariable=name)

    b = Button(win, text="Удалить блюдо из меню", command=delete)

    cat_label.grid(row=0, column=0)
    name_label.grid(row=1, column=0)

    cat_ent.grid(row=0, column=1, padx=5, pady=5)
    name_ent.grid(row=1, column=1, padx=5, pady=5)
    b.grid(row=3, column=0, padx=5, pady=5, sticky="e")


def send_2_vk(log, paswd, menu):
    """Send menu 2 vk"""
    vk = vk_api.VkApi(login=log, password=paswd)
    vk.auth()
    log = ""
    paswd = ""
    id_vk = vk.method('users.get', {})
    vk.method('messages.send', {'user_id': id_vk[0]["id"], 'message': menu})
    os.remove("vk_config.v2.json")


def make_rand_menu():
    """Generating random menu"""
    random.seed()
    a = random.randint(1, len(menu.breakfast))
    b = 1
    menu_str = "Завтрак \n"   # string with menu

    for key in menu.breakfast:
        if (a == b):
            menu_str += key + ": " + menu.breakfast[key]
        b += 1
    b = 1

    a = random.randint(1, len(menu.dinner))
    menu_str += "\nОбед \n"
    for key in menu.dinner:
        if (a == b):
            menu_str += key + ": " + menu.dinner[key]
        b += 1
    b = 1

    a = random.randint(1, len(menu.supper))
    menu_str += "\nУжин \n"
    for key in menu.supper:
        if (a == b):
            menu_str += key + ": " + menu.supper[key]
        b += 1

    return menu_str


def print_menu():
    """Print menu"""
    menu_str = "Завтрак \n"
    for key in menu.breakfast:
        menu_str += key + ": " + menu.breakfast[key] + "\n"
    menu_str += "\nОбед \n"
    for key in menu.dinner:
        menu_str += key + ": " + menu.dinner[key] + "\n"
    menu_str += "\nУжин \n"
    for key in menu.supper:
        menu_str += key + ": " + menu.supper[key] + "\n"
    return menu_str


def pickle_menu():
    """Pickle menu"""
    with open('breakfast.pickle', 'wb') as f:
        pickle.dump(menu.breakfast, f)
        f.close()
    with open('dinner.pickle', 'wb') as f:
        pickle.dump(menu.dinner, f)
        f.close()
    with open('supper.pickle', 'wb') as f:
        pickle.dump(menu.supper, f)
        f.close()


def load_menu():
    """Unpicle menu"""
    with open('breakfast.pickle', 'rb') as f:
        menu.breakfast = pickle.load(f)
        f.close()
    with open('dinner.pickle', 'rb') as f:
        menu.dinner = pickle.load(f)
        f.close()
    with open('supper.pickle', 'rb') as f:
        menu.supper = pickle.load(f)
        f.close()
