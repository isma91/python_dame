#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('{}x{}'.format(int(root.winfo_screenwidth() / 2), int(root.winfo_screenheight() / 2)))
root.wm_title("Python Checkers")

class Dame ():
    def __init__(self):
        self.app_name = "Checkers"
        self.version = "1.0.0"
        self.author = "isma91"
        self.menu()

    """ Method to display info or error quickly """
    def display_error(self, error_message):
        messagebox.showerror("Some trouble here !!", error_message)

    def display_info(self, info_message):
        messagebox.showinfo("Some info here !!", info_message)

    """ Method for the menu """
    def about(self):
        self.display_info("{0} version {1}\n made by {2}".format(self.app_name, self.version, self.author))

    def quit(self):
        print("quitting client")
        root.destroy()

    """ Method to display the menu """
    def menu(self):
        menubar = Menu(root)

        menu_file = Menu(menubar, tearoff=0)
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=lambda: self.quit())
        menubar.add_cascade(label="File", menu=menu_file)

        menu_about = Menu(menubar, tearoff=0)
        menu_about.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=menu_about)

        root.config(menu=menubar)

checkers = Dame()
root.mainloop()