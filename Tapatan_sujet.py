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


######################
# Variables globales
global previousChoix


######################   
    # Programme pour jouer au tapatan (jeu des neuf trous)
    # version 1: l'ordinateur choisit une place au hasard

class Jeu :
    def __init__(self,mp=[-1,-1,-1],op=[-1,-1,-1],j=0):
        self.mesPlaces=[]
        self.ordiPlaces=[]
        self.joueur=j
        for i in range(3):
             self.mesPlaces.append(mp[i])
             self.ordiPlaces.append(op[i])
    
    def voisin(self):#retourne une liste contenant [pion à bouger,place libre à occuper]
        voisin=[]
        for i in range(3):
            for j in range(9):
                if j not in self.mesPlaces and j not in self.ordiPlaces:
                    if self.joueur==1 and self.isVoisine(self.mesPlaces[i],j):voisin.append([i,j])
                    elif self.joueur==0 and self.isVoisine(self.ordiPlaces[i],j):voisin.append([i,j])
        return voisin
    
    def isVoisine(self,c1,c2):
        if c1==4 or c2==4: return True
        if c1>c2:c1,c2=c2,c1
        if (c1==0 and (c2==1 or c2==3))or(c1==1 and c2==2)or(c1==2 and c2==5)or\
           (c1==3 and c2==6)or(c1==5 and c2==8)or(c1==6 and c2==7)or(c1==7 and c2==8): return True
        return False
    
    
    def finished(self):#retourne 1 si l'humain gagne, 0 si c'est l'ordi, -1 dans les autres cas
        winner=-1
        gagne=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
        if sorted(self.mesPlaces) in gagne: winner=1
        if sorted(self.ordiPlaces) in gagne: winner=0
        return winner 


########################
# fonctions


def changeDebut():
    global coup,score,avertissement,previousChoix
    if coup!=0 and score!=[0,0]:
        avertissement=True
        fenMessage('Attention! Le score va être perdu...')


def fenMessage(s):#bandeau d'avertissement
    global band,mess1,mess2
    band=cadre.create_rectangle(5,75,298,325,width=3,fill='light yellow')
    mess1=cadre.create_text(150,150,text=s,font="Arial 12",fill='red')
    mess2=cadre.create_text(150,250,text='Cliquer ici pour valider ce choix'\
                            ,font="Arial 11",fill='red')


def eraseMessage():
    global coup,score,tour,band,mess1,mess2,avertissement
    score=[0,0]
    monScore.configure(text="0")
    ordiScore.configure(text="0")
    cadre.delete(band)
    cadre.delete(mess1)
    cadre.delete(mess2)
    avertissement=False
    rejouer()


def rejouer():
    global coup,resteAjouer,possible,debut,detectionPion,choixPion,mesPlaces\
           ,ordiPlaces,tour,gagnant,avertissement,band,mess1,mess2,previousChoix
    for i in range(3):
        cadre.coords(pion0[i],i*100+50,50)
        cadre.coords(pion1[i],i*100+50,350)
    coup,resteAjouer,possible=0,[0,1,2],[]
    debut,detectionPion,choixPion=True,False,-1
    mesPlaces,ordiPlaces,gagnant=[-1,-1,-1],[-1,-1,-1],-1
    if avertissement:
        cadre.delete(band)
        cadre.delete(mess1)
        cadre.delete(mess2)
        choixDebut.set(previousChoix)
        avertissement=False
    previousChoix=choixDebut.get()
    for i in range(9): possible.append(True)
    if choixDebut.get()==0:tour=joueurDebut[0]
    elif choixDebut.get()==1:tour=joueurDebut[randint(0,1)*2]
    else:tour=joueurDebut[2]
    message.configure(text="à {} de jouer".format(tour))
    if tour=="l'ordi": ordinateur()
    print('\nNouvelle partie')
    

def notGagne(j):
    global coup,gagnant
    if coup<5:return True
    gagnant=Jeu(mesPlaces,ordiPlaces,j).finished()
    if gagnant>=0:
        message.configure(text="Gagnant : {}".format(joueurDebut[gagnant*2]))
        score[gagnant]+=1
        monScore.configure(text=str(score[1]))
        ordiScore.configure(text=str(score[0]))
        print("Le gagnant est {}, le score est humain:{} - ordi:{}".\
              format(joueurDebut[gagnant*2],score[1],score[0]))
        return False
    return True


def ordinateur():
    global coup,possible,tour,debut,ordiPlaces
    choixPion,choixPlace,anciennePlace=-1,-1,-1
    if debut:
        choixPion=coup//2
        choixPlace=randint(0,8)#jeu provisoirement aléatoire
        while not possible[choixPlace]:choixPlace=randint(0,8)
    else:
        listeChoixPion=Jeu(mesPlaces,ordiPlaces).voisin()
        randy=randint(0,len(listeChoixPion)-1)
        choixPion=listeChoixPion[randy][0]
        choixPlace=listeChoixPion[randy][1]#jeu provisoirement aléatoire
        anciennePlace=ordiPlaces[choixPion]
    coup+=1
    print('coups no:',str(coup))
    print("L'ordi place son pion {} à la case {}".format(choixPion,choixPlace))
    possible[choixPlace]=False #on occupe une place qui était libre
    if coup==6: debut=False
    x1,y1=choixPlace%3*100+50,choixPlace//3*100+100
    cadre.coords(pion0[choixPion],x1,y1)
    ordiPlaces[choixPion]=choixPlace
    if notGagne(0):
        tour="l'humain"
        message.configure(text="à {} de jouer".format(tour))
    if not debut:
        possible[anciennePlace]=True #on libère une place


def clic(event):
    global detectionPion,choixPion,xDeb,yDeb,gagnant,avertissement
    x1,y1,detectionPion=event.x,event.y,False
    if avertissement and 0<x1<300 and 70<y1<330: eraseMessage()
    if tour=="l'humain" and gagnant==-1:
        for i in range(3):
            [xDeb,yDeb]=cadre.coords(pion1[i])
            if (x1-xDeb)**2+(y1-yDeb)**2<400:#estimation du rayon du pion à 20
                choixPion=i
                if debut and resteAjouer.count(choixPion)==0 :
                    choixPion=-1
                    break
                detectionPion=True
                break


def drag(event):
    x1,y1=event.x,event.y
    if detectionPion:
        if x1<0:x1=0
        if x1>300:x1=300
        if y1<50:y1=50
        if y1>350:x1=350
        cadre.coords(pion1[choixPion],x1,y1)

 #   pion0.append(cadre.create_image(i*100+50,50,image=photo1))
 #   pion1.append(cadre.create_image(i*100+50,350,image=photo2))
def lache(event):
    global detectionPion,possible,choixPion,coup,tour,debut,mesPlaces,resteAjouer,xDeb,yDeb
    if detectionPion and gagnant==-1:
        x1,y1,x2,y2,choixPlace=event.x,event.y,0,0,-1
        for i in range(9):
            x2,y2=i%3*100+50,i//3*100+100
            if (x2-x1)**2+(y2-y1)**2<400:
                choixPlace=i
                break
        #print('choixPlace:',choixPlace,' xDeb:',xDeb,' yDeb:',yDeb)
        if not debut:listeChoixPion=Jeu(mesPlaces,ordiPlaces,1).voisin()
        if possible[choixPlace] and choixPlace>=0 and \
           (debut or (not debut and [choixPion,choixPlace] in listeChoixPion)):
            anciennePlace=mesPlaces[choixPion]
            cadre.coords(pion1[choixPion],x2,y2)
            mesPlaces[choixPion]=choixPlace
            coup+=1
            print('coups no:',str(coup))
            print("L'humain place le pion {} à la case {}".format(choixPion,choixPlace))
            if notGagne(1):
                tour="l'ordi"
                message.configure(text="à {} de jouer".format(tour))
                resteAjouer[choixPion]=-1
                possible[choixPlace]=False #on occupe une place qui était libre
                if not debut:
                    possible[anciennePlace]=True #on libère une place
                    print("possible:",possible)
                if coup==6: debut=False
                choixPion=-1
                ordinateur()
        else:cadre.coords(pion1[choixPion],xDeb,yDeb)
        detectionPion=False
    #else:cadre.coords(pion1[choixPion],xDeb,yDeb)


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
     

########################
# programme principal

fen = tk.Tk()
fen.title('Jeu des Neuf Trous')
joueurDebut=["l'ordi","aléatoire","l'humain"]
tour=joueurDebut[randint(0,1)*2]
cadre= tk.Canvas(fen, bg='light yellow', width=300, height=400)
cadre.grid(row=1,column=1,columnspan=3)
cadre.bind("<Button-1>",clic)
cadre.bind("<B1-Motion>",drag)
cadre.bind("<ButtonRelease-1>",lache)
#ordiScore=Label(fen,text="0")
#ordiScore.grid(row=2,column=1)
#message=Label(fen,text="à {} de jouer".format(tour))
#message.grid(row=2,column=2)
#monScore=Label(fen,text="0")
#monScore.grid(row=2,column=3)
#choixDebut=IntVar()
#choixDebut.set(1)
#for i in range(3): # Création des trois 'boutons radio' :
#    bouton=Radiobutton(fen,text=joueurDebut[i],variable=choixDebut,
#                       value=i,command=changeDebut)
#    bouton.grid(row=3,column=i+1)
#bouton=Button(fen,text="Rejouer",command=rejouer)
#bouton.grid(row=4,column=1,columnspan=3)
#photo1=PhotoImage(file="buttonBleu.gif")     
#photo2=PhotoImage(file="buttonArcEnCiel.gif")
photo1=cadre.create_oval(10,10,30,30,fill='blue')
photo2=cadre.create_oval(10,10,30,30,fill='red')



#initialisations des variables globales
debut,detectionPion,avertissement=True,False,False
possible,coup,score,resteAjouer=[],0,[0,0],[0,1,2]
mesPlaces,ordiPlaces,choixPion=[-1,-1,-1],[-1,-1,-1],-1
xDeb,yDeb,gagnant,previousChoix=0,0,-1,1
band,mess1,mess2=None,None,None
for i in range(9): possible.append(True)
pion0,pion1=[],[]
tracePlateau()
for i in range(3):# Création des six pions :
    pion0.append(photo1)#ordi
    pion1.append(photo2)#humain
if tour=="l'ordi": ordinateur()
fen.mainloop()

    