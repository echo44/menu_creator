# -*- coding: utf-8 -*-
import vk_api
import menu
import random
import os
import pickle


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