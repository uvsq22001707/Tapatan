from tkinter import *
from tkinter.messagebox import *
def Clic(event):
    global a,C1,C2,C3,C1RC,C1R,C2RC,C2R,C3RC,C3R,L1RC,L1R,L2RC,L2R,L3RC,L3R,L1,L2,L3
X = event.x
Y = event.y

for i in range(9): possible.append(True)
pion0,pion1=[],[]
tracePlateau()
for i in range(3):# Création des six pions :
    pion0.append(cadre.create_image(i*100+50,50,image=photo1))
    pion1.append(cadre.create_image(i*100+50,350,image=photo2))
if tour=="l'ordi": ordinateur()
mainloop()
