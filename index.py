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
        self.player1_color = "white"
        self.player2_color = "black"
        self.player1_score = 0
        self.player2_score = 0
        self.player_color_turn = "white"
        self.dict_coor_button = {}
        self.list_tmp_coor_button = []
        self.big_frame = Frame(width=int(root.winfo_screenwidth() / 2), height=int(root.winfo_screenheight() / 2))
        self.big_frame.pack(fill="both", expand=True)
        self.grid_frame = Frame(width=int(root.winfo_screenwidth() / 2), height=int(root.winfo_screenheight() / 2))
        self.grid_frame.place(in_=self.big_frame, anchor="c", relx=.5, rely=.5)
        self.black = Image.open("black.png")
        self.white = Image.open("white.png")
        self.black_checkers = ImageTk.PhotoImage(self.black)
        self.white_checkers = ImageTk.PhotoImage(self.white)
        self.menu()
        self.init_case()
        self.label_player = Label(self.big_frame, text="It's the player {0} to play".format(self.player_color_turn)).pack()

    def change_turn(self):
        if self.player_color_turn == "black":
            self.player_color_turn = "white"
        else:
            self.player_color_turn = "black"
        self.display_info("Changing turn !!", "It's the player {0} to play".format(self.player_color_turn))
        self.label_player = Label(self.big_frame, text="It's the player {0} to play".format(self.player_color_turn)).pack()

    """ @TODO: check for dame white & black """
    def check_button_coor(self, coor_ligne, coor_colonne):
        self.refresh_grid()
        if self.dict_coor_button[coor_ligne][coor_colonne] == "normal_{0}".format(self.player_color_turn):
            self.display_possibility_normal_button_coor(coor_ligne, coor_colonne)
        elif self.dict_coor_button[coor_ligne][coor_colonne] == "dame_{0}".format(self.player_color_turn):
            self.display_info("DAME", "C'est une DAME !!")
        elif self.dict_coor_button[coor_ligne][coor_colonne] == "empty":
            self.display_error("Missclick ?", "You can't choose an empty case !!")
        elif self.dict_coor_button[coor_ligne][coor_colonne] == "void":
            self.display_error("Missclick ?", "You can't choose the void case !!")
        elif self.dict_coor_button[coor_ligne][coor_colonne] != self.player_color_turn:
            self.display_error("Missclick ?", "You can't choose the enemy pawn !!")

    """ @TODO: """
    def display_possibility_normal_button_coor(self, ligne, colonne):
        self.remove_selected_grid()
        if self.player_color_turn == "white":
            if colonne == 0:
                if self.dict_coor_button[ligne - 1][colonne + 1] == "empty":
                    self.list_tmp_coor_button.append([ligne - 1, colonne + 1])
            elif colonne == 9:
                if self.dict_coor_button[ligne - 1][colonne - 1] == "empty":
                    self.list_tmp_coor_button.append([ligne - 1, colonne - 1])
            else:
                if self.dict_coor_button[ligne - 1][colonne - 1] == "empty":
                    self.list_tmp_coor_button.append([ligne - 1, colonne - 1])
                if self.dict_coor_button[ligne - 1][colonne + 1] == "empty":
                    self.list_tmp_coor_button.append([ligne - 1, colonne + 1])
        self.refresh_grid()

    """ First display of all case """
    def init_case(self):
        num_ligne = 10
        num_colonne = 10
        count_max_black_checkers = 20
        count_max_white_checkers = 20
        count_black_checkers = 0
        count_white_checkers = 0
        for ligne in range(num_ligne):
            self.dict_coor_button[ligne] = {}
            for colonne in range(num_colonne):
                if ligne % 2 == 0 and colonne % 2 == 0:
                    Button(self.grid_frame, bg="burlywood").grid(row=ligne, column=colonne)
                    self.dict_coor_button[ligne][colonne] = "void"
                elif ligne % 2 == 0 and colonne % 2 != 0:
                    if ligne > 5:
                        if count_white_checkers < count_max_white_checkers:
                            Button(self.grid_frame, image=self.white_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_white_checkers = count_white_checkers + 1
                            self.dict_coor_button[ligne][colonne] = "normal_white"
                        else:
                            Button(self.grid_frame, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_coor_button[ligne][colonne] = "empty"
                    else:
                        if count_black_checkers < count_max_black_checkers:
                            Button(self.grid_frame, image=self.black_checkers, bg="peru", command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(row=ligne, column=colonne)
                            count_black_checkers = count_black_checkers + 1
                            self.dict_coor_button[ligne][colonne] = "normal_black"
                        else:
                            Button(self.grid_frame, bg="peru", command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(row=ligne, column=colonne)
                            self.dict_coor_button[ligne][colonne] = "empty"
                elif ligne % 2 != 0 and colonne % 2 == 0:
                    if ligne > 5:
                        if count_white_checkers < count_max_white_checkers:
                            Button(self.grid_frame, image=self.white_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_white_checkers = count_white_checkers + 1
                            self.dict_coor_button[ligne][colonne] = "normal_white"
                        else:
                            Button(self.grid_frame, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_coor_button[ligne][colonne] = "empty"
                    else:
                        if count_black_checkers < count_max_black_checkers:
                            Button(self.grid_frame, image=self.black_checkers, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            count_black_checkers = count_black_checkers + 1
                            self.dict_coor_button[ligne][colonne] = "normal_black"
                        else:
                            Button(self.grid_frame, bg="peru",
                                   command=lambda row=ligne, column=colonne: self.check_button_coor(row, column)).grid(
                                row=ligne, column=colonne)
                            self.dict_coor_button[ligne][colonne] = "empty"
                elif ligne % 2 != 0 and colonne % 2 != 0:
                    Button(self.grid_frame, bg="burlywood").grid(row=ligne, column=colonne)
                    self.dict_coor_button[ligne][colonne] = "void"

    """ Method to display the selected case and to remove the selected case """
    def refresh_grid(self):
        for index, array_coor in enumerate(self.list_tmp_coor_button):
            Button(self.grid_frame, bg="red",
                   command=lambda row=array_coor[0], column=array_coor[1]: self.check_button_coor(row, column)).grid(
                row=array_coor[0], column=array_coor[1])

    def remove_selected_grid(self):
        for index, array_coor in enumerate(self.list_tmp_coor_button):
            Button(self.grid_frame, bg="peru",
                   command=lambda row=array_coor[0], column=array_coor[1]: self.check_button_coor(row, column)).grid(
                row=array_coor[0], column=array_coor[1])
        self.list_tmp_coor_button = []

    """ Method to display info or error quickly """
    def display_error(self, error_title, error_message):
        messagebox.showerror(error_title, error_message)

    def display_info(self, info_title, info_message):
        messagebox.showinfo(info_title, info_message)

    """ Method for the menu """
    def about(self):
        self.display_info("About this game", "{0} version {1}\n made by {2}".format(self.app_name, self.version, self.author))

    def quit(self):
        print("Quitting client")
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