#########################################
#informations liées au groupe
# groupe Miashs Td1 groupe 5
# Gouyer Roxane
# Alioune Ndiaye
# Momar SAMBE
# Maxime Jouan

########################
# import des librairies
import tkinter as tk
from random import randint

########################
# Constantes
Hauteur = 400
Largeur =300


######################
# Variables globales



########################
# fonctions

def cree_pion():
    for i in range(3):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='red')
    for i in range(12,15):
        xt,yt=i%3*100+50,i//3*100
        if i>11:yt-=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='blue')

def tracePlateau():
    cadre.create_rectangle(50,100,250,300,width=5)
    cadre.create_line(50,100,250,300,width=5,fill='black')
    cadre.create_line(50,300,250,100,width=5,fill='black')
    cadre.create_line(50,200,250,200,width=5,fill='black')
    cadre.create_line(150,100,150,300,width=5,fill='black')
    for i in range(15):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        if i>11:yt-=50
        cadre.create_oval(xt-7,yt-7,xt+7,yt+7,width=5,fill='black')
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='light yellow')



def test_clic(event):
    i, j = coord(event.x, event.y)
    if i > 25 and i < 75 and j > 75 and j <125:
        if tableau == 0:
            cadre.create_oval(25,75,75,125,width=0,fill='red')
    if i > 125 and i < 175 and j > 75 and j <125:
        cadre.destroy()
    if i > 225 and i < 275 and j > 75 and j <125:
        cadre.destroy()
    if i > 25 and i < 75 and j > 175 and j <225:
        cadre.destroy()
    if i > 125 and i < 175 and j > 175 and j <225:
        cadre.destroy()
    if i > 225 and i < 275 and j > 175 and j <225:
        cadre.destroy()
    if i > 25 and i < 75 and j > 275 and j <325:
        cadre.destroy()
    if i > 125 and i < 175 and j > 275 and j <325:
        cadre.destroy()
    if i > 225 and i < 275 and j > 275 and j <325:
        cadre.destroy()

def coord(x, y):
    return x , y



def place_pion():

    


########################
# programme principal
fen = tk.TK()
fen.title('Tapatan')
cadre= tk.Canvas(fen, bg='white', width=Largeur, height=Hauteur)
cadre.grid(row=1,column=1,columnspan=3)
cadre.bind("<Button-1>",test_clic)
tracePlateau()
cree_pion()
fen.mainloop()
