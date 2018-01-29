# -*- coding: utf-8 -*-
from tkinter import *
import functions as fn
import menu as mn


class Application(Frame):
    """Make GUI"""

    def __init__(self, master):
        super(Application, self).__init__()
        self.gen_menu = Button(self, text="Сгенерить меню на день", command=self.make_menu)
        self.show_menu = Button(self, text="Посмотреть все меню", command=self.show_menu)
        self.add_dish = Button(self, text="Добавить блюдо",command=self.add_dish)
        self.del_dish = Button(self, text="Удалить блюдо",command=self.del_dish)

        self.set_buttons()
        self.grid()

    def set_buttons(self):
        """Set layout"""
        self.gen_menu.pack(fill=X)
        self.show_menu.pack(fill=X)
        self.add_dish.pack(fill=X)
        self.del_dish.pack(fill=X)

    def make_menu(self):
        """Making menu"""

        def vk_window():
            """Make window for VK"""

            def send():
                """Sending menu 2 vk"""
                l = login.get()
                p = password.get()
                menu = text.get("1.0", END)
                fn.send_2_vk(l, p, menu)
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
            menu = fn.make_rand_menu()
            text.delete('1.0', END)
            text.insert(END, menu)

        win = Toplevel()
        win.title("Твое меню")
        menu = fn.make_rand_menu()
        text = Text(win, height=20, width=45)
        text.pack()
        text.insert(END, menu)

        b = Button(win, text="Отправить ингридиенты в ВК", command=vk_window)
        b.pack(side="bottom")

        b2 = Button(win, text="Сгенерить другое меню", command=reroll_menu)
        b2.pack(side="bottom")

    def show_menu(self):
        """Show menu"""
        win = Toplevel()
        win.title("Все меню")
        menu = fn.print_menu()
        text = Text(win)
        text.pack()
        text.insert(END, menu)

    def add_dish(self):
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
                mn.breakfast[n] = i
                show_suc_win()

            elif (c.lower() == "обед"):
                mn.dinner[n] = i
                show_suc_win()

            elif (c.lower() == "ужин"):
                mn.supper[n] = i
                show_suc_win()

            else:
                err = Toplevel()
                err.title("ОШИБКА")
                err.geometry("300x100")
                Button(err, text="Ok", command=err.destroy).pack(side="bottom")
                Label(err, text="Категория должна быть: затрак, обед или ужин").pack()

            fn.pickle_menu()

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

    def del_dish(self):
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
                mn.breakfast.pop(n)
                show_suc_win()

            elif (c.lower() == "обед"):
                mn.dinner.pop(n)
                show_suc_win()

            elif (c.lower() == "ужин"):
                mn.supper.pop(n)
                show_suc_win()

            else:
                err = Toplevel()
                err.title("ОШИБКА")
                err.geometry("300x100")
                Button(err, text="Ok", command=err.destroy).pack(side="bottom")
                Label(err, text="Категория должна быть: затрак, обед или ужин").pack()

            fn.pickle_menu()

        category = StringVar()
        name = StringVar()
        win = Toplevel()
        win.title("Удаляем блюда из меню")

        cat_label = Label(win, text="Категория")
        name_label = Label(win, text="Название")

        cat_ent = Entry(win, textvariable=category)
        name_ent = Entry(win, textvariable=name)

        b = Button(win, text="Удалить блюдо из меню",command=delete)

        cat_label.grid(row=0, column=0)
        name_label.grid(row=1, column=0)

        cat_ent.grid(row=0, column=1, padx=5, pady=5)
        name_ent.grid(row=1, column=1, padx=5, pady=5)
        b.grid(row=3, column=0, padx=5, pady=5, sticky="e")


try:
    fn.load_menu()
except BaseException:
    pass

#test 4 git

root = Tk()
app = Application(root)
root.title("Генератор меню")

root.mainloop()