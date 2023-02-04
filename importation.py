#Jfreez tuto salto progression

from tkinter import *
from tkinter import messagebox
#important filedialog et askopenfilename
from tkinter.filedialog import askopenfilename
import webbrowser


class MyWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        # TODO: Fill the content of the window

        self.geometry("1420x600")
        self.minsize(1420, 600)
        self.title("Facebook V.h4ck3rm4n04.0.1")
        self.config(background = 'darkgrey')


    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff = 0)
        menu_file.add_command(label = 'New',command = self.function)
        menu_file.add_command(label = 'open',command = self.open_file)
        menu_file.add_command(label = 'Save', command = self.save_file)
        menu_file.add_separator()
        menu_file.add_command(label = 'Exit', command = self.quit)
        menu_bar.add_cascade(label = 'Fichier', menu = menu_file)

        option_men = Menu(menu_bar, tearoff = 0)
        option_men.add_command(label = 'Follow',command = self.web)
        menu_bar.add_cascade(label = 'Programmeur', menu = option_men)

        self.config(menu = menu_bar)

    def open_file(self):
        file = askopenfilename(title = 'Choose an file',
            filetypes = [('All file', '.*')])
        print(file)

    def save_file(self):
        file = askopenfilename(title = 'Save anywhere',
            filetypes = [('All file', '.*')])
        print(file)

    def web(self):
        webbrowser.open_new('https://www.instagram.com/h4ck3rm4n04/?next=%2F')

    def function(self):
        print('JESUS EST GRAND')