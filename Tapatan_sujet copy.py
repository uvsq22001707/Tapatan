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
pion0,pion1=[],[]

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

'''
def clic(event):
    global detectionPion,choixPion,xDeb,yDeb,gagnant,avertissement
    x1,y1,detectionPion=event.x,event.y,False
    if avertissement and 0<x1<300 and 70<y1<330:
        for i in range(3):
            [xDeb,yDeb]=cadre.coords(pion1[i])
            if (x1-xDeb)**2+(y1-yDeb)**2<400:#estimation du rayon du pion à 20
                choixPion=i
                if debut and resteAjouer.count(choixPion)==0 :
                    choixPion=-1
                    break
                detectionPion=True
                break
'''
def test_clic(event):
    for i in range(4,12):
        xt,yt=i%3*100+50,i//3*100
        pion1[i]=i*100+50,350
        [xDeb,yDeb]=cadre.coords(pion1[i])
        return (xt-xDeb)**2+(yt-yDeb)**2<400

    
#def Clic(event):
#    global a,C1,C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
#X = event.x
#Y = event.y

#for i in range(9): possible.append(True)
#if tour=="l'ordi": ordinateur()


########################
# programme principal
fen = tk.Tk()
fen.title('Tapatan')
joueurDebut=["Joueur 1","aléatoire","Joueur 2"]
tour=joueurDebut[randint(0,1)*2]
cadre= tk.Canvas(fen, bg='white', width=300, height=400)
cadre.grid(row=1,column=1,columnspan=3)
cadre.bind("<Button-1>",test_clic)
tracePlateau()
cree_pion()
fen.mainloop()
