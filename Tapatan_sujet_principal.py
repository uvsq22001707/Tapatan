#########################################
#informations liées au groupe
# groupe Miashs Td1 groupe 5
# Gouyer Roxane
# Alioune Ndiaye
# Momar SAMBE
# Maxime Jouan
#Pote Die
########################
# import des librairies
import tkinter as tk
from random import randint
from tkinter.ttk import Label

########################
# Constantes
Hauteur = 400
Largeur =300

######################
# Variables globale



########################
# fonctions


def tracePlateau():                           #fonction qui va tracer le plateau
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


def cree_pion():                                 #fonction qui va créé les pions à leurs points de départs
    for i in range(3):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='red')
    for i in range(12,15):
        xt,yt=i%3*100+50,i//3*100
        if i>11:yt-=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='blue')


def coord(x, y):    #fonction détectant les clics de la souris
    return x , y


def test_clic(event):                                                          #fonction pour placer un pion en fonction du clic.
    i, j = coord(event.x, event.y)
    if partie_en_cours(piontableau):
        if i > 40 and i < 60 and j > 90 and j <110 and piontableau[0] == 1:          #emplacement pion 1
            if tour[0] == 1 or tour[0] == 3 or tour[0] ==5:
                cadre.create_oval(40,90,60,110,width=0,fill='red')
                if tour[0] == 1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                    cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                    cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[0]=2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(40,90,60,110,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[0]=3
            tour[0] += 1
            
    
        if i > 140 and i < 160 and j > 90 and j <110 and piontableau[1] == 1:      #emplacement pion 2
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
                cadre.create_oval(140,90,160,110,width=0,fill='red')
                if tour[0] == 1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                   cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[1]= 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] ==6:
                cadre.create_oval(140,90,160,110,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[1] = 3
            tour[0] += 1
        
        if i > 240 and i < 260 and j > 90 and j <110 and piontableau[2] == 1:       #emplacement pion 3
            if tour[0] == 1 or tour[0] == 3 or  tour[0] == 5:
                cadre.create_oval(240,90,260,110,width=0,fill='red')
                if tour[0] == 1:
                    cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                    cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                    cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[2] = 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(240,90,260,110,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[2] = 3
            tour[0] += 1
    
        if i > 40 and i < 60 and j > 175 and j <210 and piontableau[3] == 1:       #emplacement pion  4
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
                cadre.create_oval(40,190,60,210,width=0,fill='red')
                if tour[0]==1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                   cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[3] = 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(40,190,60,210,width=0,fill='blue')
                if tour[0]==2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6 :
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[3] = 3
            tour[0] += 1
    
        if i > 140 and i < 160 and j > 190 and j <210 and piontableau[4] == 1:        #emplacement pion  5
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
                cadre.create_oval(140,190,160,210,width=0,fill='red')
                if tour[0]==1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                   cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[4] = 2  
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(140,190,160,210,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[4] = 3
            tour[0] += 1
    
    
        if i > 240 and i < 260 and j > 190 and j <210 and piontableau[5] == 1:          #emplacement pion 6
            if tour[0] == 1 or tour[0] == 3  or tour[0] == 5:
                cadre.create_oval(240,190,260,210,width=0,fill='red')
                if tour[0] == 1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                   cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[5] = 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(240,190,260,210,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[5] = 3
            tour[0] += 1
        
        if i > 40 and i < 60 and j > 290 and j <310 and piontableau[6] == 1:             #emplacement pion 7
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
                cadre.create_oval(40,290,60,310,width=0,fill='red')
                if tour[0] == 1:
                    cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                    cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[6] = 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(40,290,60,310,width=0,fill='blue')
                if tour[0] ==0:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[6] = 3
            tour[0] += 1
        
        if i > 140 and i < 160 and j > 290 and j <310 and piontableau[7] == 1:            #emplacement pion 8
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
               cadre.create_oval(140,290,160,310,width=0,fill='red')
               if tour[0] ==1:
                   cadre.create_oval(45,45,55,55,width=0,fill='white')
               elif tour[0] == 3:
                   cadre.create_oval(145,45,155,55,width=0,fill='white')
               elif tour[0] == 5:
                   cadre.create_oval(245,45,255,55,width=0,fill='white')
               piontableau[7] = 2
            elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6:
                cadre.create_oval(140,290,160,310,width=0,fill='blue')
                if tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[7] = 3
            tour[0] += 1
    
        if i > 240 and i < 260 and j > 290 and j <310 and piontableau[8] == 1:            #emplacement pion 9
            if tour[0] == 1 or tour[0] == 3 or tour[0] == 5:
                cadre.create_oval(240,290,260,310,width=0,fill='red')
                if tour[0] == 1:
                    cadre.create_oval(45,45,55,55,width=0,fill='white')
                elif tour[0] == 3:
                    cadre.create_oval(145,45,155,55,width=0,fill='white')
                elif tour[0] == 5:
                    cadre.create_oval(245,45,255,55,width=0,fill='white')
                piontableau[8] = 2
            elif tour[0] == 4 or tour[0] == 2 or tour[0] == 6:
                cadre.create_oval(240,290,260,310,width=0,fill='blue')
                if tour[0] == 4:
                    cadre.create_oval(145,345,155,355,width=0,fill='white')
                elif tour[0] == 2:
                    cadre.create_oval(45,345,55,355,width=0,fill='white')
                elif tour[0] == 6:
                    cadre.create_oval(245,345,255,355,width=0,fill='white')
                piontableau[8] = 3
            tour[0] += 1


def mouvement(event):                        #fonction utilisé pour déplacer un pion
    i, j = coord(event.x, event.y)
    global rouge_ou_bleu
    global touche_ou_pas
    if partie_en_cours(piontableau) and prendre_poser[0] == 0 :                                      #partie pour prendre le pion
        if i > 40 and i < 60 and j > 90 and j <110  and rouge_ou_bleu[0] == piontableau[0]:
            cadre.create_oval(40,90,60,110,width=0,fill='black')
            cadre.create_oval(47,97,53,103,width=0,fill='white')
            piontableau[0]= 1
            touche_ou_pas = 1 
        
        if i > 140 and i < 160 and j > 90 and j <110 and piontableau[1] != 1 and rouge_ou_bleu[0] == piontableau[1]:
            cadre.create_oval(140,90,160,110,width=0,fill='black')
            cadre.create_oval(147,97,153,103,width=0,fill='white')
            piontableau[1]=1
            touche_ou_pas = 2
        if i > 240 and i < 260 and j > 90 and j <110 and piontableau[2] != 1 and rouge_ou_bleu[0] == piontableau[2]:
            cadre.create_oval(240,90,260,110,width=0,fill='black')
            cadre.create_oval(247,97,253,103,width=0,fill='white')
            piontableau[2]=1
            touche_ou_pas = 3
        
        if i > 40 and i < 60 and j > 175 and j <210 and piontableau[3] != 1 and rouge_ou_bleu[0] == piontableau[3]:
            cadre.create_oval(40,190,60,210,width=0,fill='black')
            cadre.create_oval(47,197,53,203,width=0,fill='white')
            piontableau[3]=1
            touche_ou_pas = 4
        if i > 140 and i < 160 and j > 190 and j <210 and piontableau[4] != 1 and rouge_ou_bleu[0] == piontableau[4]:
            cadre.create_oval(140,190,160,210,width=0,fill='black')
            cadre.create_oval(147,197,153,203,width=0,fill='white')
            piontableau[4]=1
            touche_ou_pas = 9
        
        if i > 240 and i < 260 and j > 190 and j <210 and piontableau[5] != 1 and rouge_ou_bleu[0] == piontableau[5]:
            cadre.create_oval(240,190,260,210,width=0,fill='black')
            cadre.create_oval(247,197,253,203,width=0,fill='white')
            piontableau[5]=1
            touche_ou_pas = 5
        if i > 40 and i < 60 and j > 290 and j <310 and piontableau[6] != 1 and rouge_ou_bleu[0] == piontableau[6]:
            cadre.create_oval(40,290,60,310,width=0,fill='black')
            cadre.create_oval(47,297,53,303,width=0,fill='white')
            piontableau[6]=1
            touche_ou_pas = 6
        
        if i > 140 and i < 160 and j > 290 and j <310 and piontableau[7] != 1 and rouge_ou_bleu[0] == piontableau[7]:
            cadre.create_oval(140,290,160,310,width=0,fill='black')
            cadre.create_oval(147,297,153,307,width=0,fill='white')
            piontableau[7]=1
            touche_ou_pas = 7
        
        if i > 240 and i < 260 and j > 290 and j <310 and piontableau[8] != 1 and rouge_ou_bleu[0] == piontableau[8]:
            cadre.create_oval(240,290,260,310,width=0,fill='black')
            cadre.create_oval(247,297,253,307,width=0,fill='white')
            piontableau[8]=1
            touche_ou_pas =8
        prendre_poser[0] = 1
    elif partie_en_cours(piontableau) and prendre_poser[0] == 1 and tour[0]>=7:                                 #partie pour déposer le pion
        if i > 40 and i < 60 and j > 90 and j <110 and piontableau[0] == 1 and (touche_ou_pas == 1 or touche_ou_pas == 2 or touche_ou_pas == 4 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(40,90,60,110,width=0,fill='blue')
                piontableau[0] =3
            else:
                cadre.create_oval(40,90,60,110,width=0,fill='red')
                piontableau[0] =2
        if i > 140 and i < 160 and j > 90 and j <110 and piontableau[1] == 1 and (touche_ou_pas == 1 or touche_ou_pas == 2 or touche_ou_pas == 3 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(140,90,160,110,width=0,fill='blue')
                piontableau[1] =3
            else:
                cadre.create_oval(140,90,160,110,width=0,fill='red')
                piontableau[1] =2
        if i > 240 and i < 260 and j > 90 and j <110 and piontableau[2]==1 and (touche_ou_pas == 2 or touche_ou_pas == 3 or touche_ou_pas == 5 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(240,90,260,110,width=0,fill='blue')
                piontableau[2] =3
            else:
                cadre.create_oval(240,90,260,110,width=0,fill='red')
                piontableau[2] =2
        if i > 40 and i < 60 and j > 175 and j <210 and piontableau[3]==1 and (touche_ou_pas == 1 or touche_ou_pas == 4 or touche_ou_pas == 6 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(40,190,60,210,width=0,fill='blue')
                piontableau[3] =3
            else:
                cadre.create_oval(40,190,60,210,width=0,fill='red')
                piontableau[3] =2
        if i > 140 and i < 160 and j > 190 and j <210 and piontableau[4]==1:
            if tour[0] %2 ==0:
                cadre.create_oval(140,190,160,210,width=0,fill='blue')
                piontableau[4] =3
            else:
                cadre.create_oval(140,190,160,210,width=0,fill='red')
                piontableau[4] =2
        if i > 240 and i < 260 and j > 190 and j <210 and piontableau[5]==1 and (touche_ou_pas == 3 or touche_ou_pas == 5 or touche_ou_pas == 8 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(240,190,260,210,width=0,fill='blue')
                piontableau[5] =3
            else:
                cadre.create_oval(240,190,260,210,width=0,fill='red')
                piontableau[5] =2
        if 40 and i < 60 and j > 290 and j <310 and piontableau[6]== 1 and (touche_ou_pas == 4 or touche_ou_pas == 6 or touche_ou_pas == 7 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(40,290,60,310,width=0,fill='blue')
                piontableau[6] =3
            else:
                cadre.create_oval(40,290,60,310,width=0,fill='red')
                piontableau[6] =2
        if i > 140 and i < 160 and j > 290 and j <310 and piontableau[7]== 1 and (touche_ou_pas == 6 or touche_ou_pas == 7 or touche_ou_pas == 8 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(140,290,160,310,width=0,fill='blue')
                piontableau[7] =3
            else:
                cadre.create_oval(140,290,160,310,width=0,fill='red')
                piontableau[7] =2
        if i > 240 and i < 260 and j > 290 and j <310 and piontableau[8]== 1 and( touche_ou_pas == 5 or touche_ou_pas == 7 or touche_ou_pas == 8 or touche_ou_pas == 9):
            if tour[0] %2 ==0:
                cadre.create_oval(240,290,260,310,width=0,fill='blue')
                piontableau[8] =3
            else:
                cadre.create_oval(240,290,260,310,width=0,fill='red')
                piontableau[8] =2
        if rouge_ou_bleu[0] == 2:
            rouge_ou_bleu[0] = 3
        elif rouge_ou_bleu[0] == 3:
            rouge_ou_bleu[0] =2
        prendre_poser[0]=0
        tour[0] += 1


def partie_en_cours(piontableau):                                         #fonction détectant si 3 pions sont alignés ou non
    if piontableau[0] == piontableau[1] and piontableau[1] == piontableau[2] and piontableau[0] != 1 :
        return False
    elif piontableau[3] == piontableau[4] and piontableau[4] == piontableau[5] and piontableau[3] != 1:
        return False
    elif piontableau[6] == piontableau[7] and piontableau[7] == piontableau[8] and piontableau[6] != 1:
        return False
    elif piontableau[0] == piontableau[3] and piontableau[3] == piontableau[6] and piontableau[0] != 1:
        return False
    elif piontableau[1] == piontableau[4] and piontableau[4] == piontableau[7] and piontableau[1] != 1:
        return False
    elif piontableau[2] == piontableau[5] and piontableau[5] == piontableau[8] and piontableau[2] != 1:
        return False
    elif piontableau[0] == piontableau[4] and piontableau[4] == piontableau[8] and piontableau[0] != 1:
        return False
    elif piontableau[2] == piontableau[4] and piontableau[4] == piontableau[6] and piontableau[2] != 1:
        return False
    else:
        return True


def manche_placement(event):                                   #fonction qui va faire déroulé toute les étapes d'un tour 
    i, j = coord(event.x, event.y)                             #lors de la phase de placement
    if partie_en_cours(piontableau) and tour[0]<7:
        test_clic(event)
        if partie_en_cours(piontableau):
            return
        else:
            recommencer_une_manche()


def manche_deplacement(event):                                #fonction qui va faire déroulé toute les étapes d'un tour
    i, j = coord(event.x, event.y)                            #lors de la phase de déplacement
    if partie_en_cours(piontableau) and tour[0]>=7:
        mouvement(event)
        if partie_en_cours(piontableau):
            return
        else:
            recommencer_une_manche()


def recommencer_une_manche():                                #fonction de fin de tour qui va attribuer les points et annoncer le vainqueur
    global nombre_manche
    global score1
    global score2
    if tour[0] %2 ==0:
        if nombre_manche ==1 or nombre_manche ==3 or nombre_manche == 5:
            score1 +=1
        else:
            print("le joueur 2 gagné")
            score2 += 1
    else:
        if nombre_manche ==2 or nombre_manche ==4 or nombre_manche == 6:
            print("le joueur 1 à gagné")
            score1 += 1
        else:
            print("le joueur 2 gagné")
            score2 += 1
    if score1 ==3:
        label = Label(cadre, text='Victoire du Joueur 1')
        label.pack(ipadx=20, ipady=20)
    elif score2==3:
        label = Label(cadre, text='Victoire du Joueur 2')
        label.pack(ipadx=20, ipady=20)
    else:
        cadre.create_rectangle(0,0,300,400,width=0,fill='white')
        fonct_aff_score()
        tracePlateau()
        cree_pion()
        tour[0]= 1
        nombre_manche += 1
        global piontableau
        piontableau = [1,1,1,1,1,1,1,1,1]


def fonct_aff_score():                                        #fonction qui va afficher les scores
    cadre2=tk.Canvas(fen, bg='white', width=50, height=50)
    cadre3=tk.Canvas(fen, bg='white', width=50, height=50)
    cadre2.grid(row=1,column=1,columnspan=1)
    cadre3.grid(row=1,column=3,columnspan=1)
    label2 = Label(cadre2, text = 'Le score du Joueur 1 est de :')
    label2.pack(ipadx=20, ipady=20)
    label2 = Label(cadre3, text = 'Le score du Joueur 2 est de :')
    label2.pack(ipadx=20, ipady=20)
    if score1 ==0:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=1)
        cadre4.create_text(10,10,text=0)
    if score1 ==1:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=1)
        cadre4.create_text(10,10,text=1)
    if score1 ==2:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=1)
        cadre4.create_text(10,10,text=2)
    if score1 ==3:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=1)
        cadre4.create_text(10,10,text=3)
    if score2 ==0:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=3)
        cadre4.create_text(10,10,text=0)
    if score2 ==1:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=3)
        cadre4.create_text(10,10,text=1)
    if score2 ==2:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=3)
        cadre4.create_text(10,10,text=2)
    if score2 ==3:
        cadre4=tk.Canvas(fen, bg='white', width=20, height=20)
        cadre4.grid(row=2,column=1,columnspan=3)
        cadre4.create_text(10,10,text=3)

###################################
#fonction créé variables
def tour_joueur():      #fonction pour la variable tour
    global tour
    tour = [1]


def var_rouge_bleu():      #fonction pour la variable rouge_ou_bleu
    global rouge_ou_bleu
    rouge_ou_bleu =[2]


def pion_existant():      #fonction pour la variable pionexistant
    global piontableau
    piontableau = [1,1,1,1,1,1,1,1,1]

def moment_clic():        #fonction pour la variable prendre_poser
    global prendre_poser
    prendre_poser = [0]

def rond_qui_touche():    #fonction pour la variable touche_ou_pas
    global touche_ou_pas
    touche_ou_pas = 0

def score_joueur():     ##fonction pour la variable score_joueur
    global score1
    global score2
    global nombre_manche
    nombre_manche = 1
    score1 = 0
    score2 = 0


########################
# programme principal
fen = tk.Tk()
fen.title('Tapatan')
#créé le canvas
cadre= tk.Canvas(fen, bg='white', width=Largeur, height=Hauteur)
cadre.grid(row=5,column=1,columnspan=3)
#fonction utilisé
rond_qui_touche()
score_joueur()
var_rouge_bleu()
tracePlateau()
fonct_aff_score()
cree_pion()
tour_joueur()
pion_existant()
moment_clic()
#fonction on l'on utilise une touche
cadre.bind("<Button-1>",manche_placement)
cadre.bind("<Button-3>",manche_deplacement)
fen.mainloop()