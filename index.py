#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry('{}x{}'.format(int(root.winfo_screenwidth() / 2), int(root.winfo_screenheight() / 2)))
root.wm_title("Python Checkers")

class Dame ():
    def __init__(self):
        self.app_name = "Checkers"
        self.version = "1.0.0"
        self.author = "isma91"
        self.dict_button = {}
        self.coor_ligne = 0
        self.coor_colonne= 0
        self.black = Image.open("black.png")
        self.white = Image.open("white.png")
        self.black_checkers = ImageTk.PhotoImage(self.black)
        self.white_checkers = ImageTk.PhotoImage(self.white)
        self.menu()
        self.display_case()

    def get_button_coor(self, coor_ligne, coor_colonne):
        print("{0}:{1}".format(coor_ligne, coor_colonne))

    def display_case(self):
        num_ligne = 10
        num_colonne = 10
        count_max_black_checkers = 20
        count_max_white_checkers = 20
        count_black_checkers = 0
        count_white_checkers = 0
        for ligne in range(num_ligne):
            self.dict_button[ligne] = {}
            for colonne in range(num_colonne):
                if ligne % 2 == 0 and colonne % 2 == 0:
                    Button(root, bg="burlywood").grid(row=ligne, column=colonne)
                    self.dict_button[ligne][colonne] = "void"
                elif ligne % 2 == 0 and colonne % 2 != 0:
                    if ligne > 5:
                        if count_white_checkers < count_max_white_checkers:
                            Button(root, image=self.white_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_white_checkers = count_white_checkers + 1
                            self.dict_button[ligne][colonne] = "white"
                        else:
                            Button(root, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_button[ligne][colonne] = "empty"
                    else:
                        if count_black_checkers < count_max_black_checkers:
                            Button(root, image=self.black_checkers, bg="peru", command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(row=ligne, column=colonne)
                            count_black_checkers = count_black_checkers + 1
                            self.dict_button[ligne][colonne] = "black"
                        else:
                            Button(root, bg="peru", command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(row=ligne, column=colonne)
                            self.dict_button[ligne][colonne] = "empty"
                elif ligne % 2 != 0 and colonne % 2 == 0:
                    if ligne > 5:
                        if count_white_checkers < count_max_white_checkers:
                            Button(root, image=self.white_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_white_checkers = count_white_checkers + 1
                            self.dict_button[ligne][colonne] = "white"
                        else:
                            Button(root, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_button[ligne][colonne] = "empty"
                    else:
                        if count_black_checkers < count_max_black_checkers:
                            Button(root, image=self.black_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_black_checkers = count_black_checkers + 1
                            self.dict_button[ligne][colonne] = "black"
                        else:
                            Button(root, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.get_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_button[ligne][colonne] = "empty"
                elif ligne % 2 != 0 and colonne % 2 != 0:
                    Button(root, bg="burlywood").grid(row=ligne, column=colonne)
                    self.dict_button[ligne][colonne] = "void"
        #print(self.dict_button)

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