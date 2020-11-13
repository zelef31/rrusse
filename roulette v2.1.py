"""
importation de tous ce qu'il faut
"""
import sys
import time
from tkinter import messagebox
from math import *
import os
from random import randrange
from math import ceil
from tkinter import *
from tkinter.messagebox import *

class fenetre():
   def  __init__(self) :
        self.fenetre = Tk()
        canvas = Canvas(self.fenetre, width=2000, height=100)
        canvas.focus_set()
        canvas.bind("<Key>", self.clavier)
        canvas.pack()
        label = Label(self.fenetre, text = " cliques ici pour rentrer dans le casino fdp ")
        label.pack()
        Frame2 = Frame(self.fenetre, borderwidth=2)
        Frame2.pack(side=RIGHT, padx=200, pady=100)
        Bouton=Button(Frame2, text=" ici fdp  ", command=self.fenetre.destroy)
        Bouton.pack()
        self.fenetre.mainloop()
   def clavier(self, event) :
        touche=event.keysym
        if touche == "Escape":
            self.fenetre.destroy()
   def ctn(self) :
        self.fenetre.destroy()
        suite()

s=fenetre()


class ProgressBar:

    """
    Barre de progrssion
    """

    def __init__(self, steps, maxbar=100, title='Chargement du programme'):
        if steps <= 0 or maxbar <= 0 or maxbar > 200:
            raise ValueError

        self.steps = steps
        self.maxbar = maxbar
        self.title = title

        self.perc = 0
        self._completed_steps = 0

        self.update(False)

    def update(self, increase=True):
        if increase:
            self._completed_steps += 0.5

        self.perc = floor(self._completed_steps / self.steps * 100)

        if self._completed_steps > self.steps:
            self._completed_steps = self.steps

        steps_bar = floor(self.perc / 100 * self.maxbar)

        if steps_bar == 0:
            visual_bar = self.maxbar * ' '
        else:
            visual_bar = (steps_bar - 1) * '=' + '>' + (self.maxbar - steps_bar) * ' '

        sys.stdout.write('\r' + self.title + ' [' + visual_bar + '] ' + str(self.perc) + '%')
        sys.stdout.flush()


if __name__ == '__main__':
    bar = ProgressBar(50)

    i = 0
    while bar.perc != 100:
        bar.update()
        time.sleep(0.05)

        i += 1

"""
Message d'entrée
"""


time.sleep(0.5)

print("                                               Bienvenue dans le casino, réalisé par MAthéo BALESTER, Julien ASTRE, Dylan FOURNIER et Anthony DUALE")

time.sleep(0.5)

print("Vous allez entrer dans le casino ")

time.sleep(1)

class ProgressBar:

    """
    Barre de progrssion
    """

    def __init__(self, steps, maxbar=100, title='Entrée dans le casino'):
        if steps <= 0 or maxbar <= 0 or maxbar > 200:
            raise ValueError

        self.steps = steps
        self.maxbar = maxbar
        self.title = title

        self.perc = 0
        self._completed_steps = 0

        self.update(False)

    def update(self, increase=True):
        if increase:
            self._completed_steps += 0.5

        self.perc = floor(self._completed_steps / self.steps * 100)

        if self._completed_steps > self.steps:
            self._completed_steps = self.steps

        steps_bar = floor(self.perc / 100 * self.maxbar)

        if steps_bar == 0:
            visual_bar = self.maxbar * ' '
        else:
            visual_bar = (steps_bar - 1) * '=' + '>' + (self.maxbar - steps_bar) * ' '

        sys.stdout.write('\r' + self.title + ' [' + visual_bar + '] ' + str(self.perc) + '%')
        sys.stdout.flush()


if __name__ == '__main__':
    bar = ProgressBar(50)

    i = 0
    while bar.perc != 100:
        bar.update()
        time.sleep(0.02)

        i += 1

"""
Fin du second chargement, mettre ensuite le code du jeu
"""


argent = 1000

continuer_partie = True

print("                                            Bonjour, vous arrivez à la table de roulette avec la somme de", argent, "€.")

while continuer_partie: # Tant qu'on doit continuer la partie

    nombre_mise = -1

    while nombre_mise < 0 or nombre_mise > 49:

        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")

        try:

            nombre_mise = int(nombre_mise)

        except ValueError:

            print("Erreur : Vous n'avez pas saisi de nombre")

            nombre_mise = -1

            continue

        if nombre_mise < 0:

            print("Erreur : Ce nombre est négatif")

        if nombre_mise > 49:

            print("Erreur : ce nombre est supérieur à 49")

    mise = 0

    while mise <= 0 or mise > argent:

        mise = input("Combien voulez vous miser ? : ")

        try:

            mise = int(mise)

        except ValueError:

            print("Erreur : vous n'avez pas saisi de nombre")

            mise = -1

            continue

        if mise <= 0:

            print("Erreur : la mise saisie est négative ou nulle.")

        if mise > argent:

            print("Vous n'avez pas assez d'argent haha vous ne pouvez miser que", argent, "€")

    numero_gagnant = randrange(50)

    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    if numero_gagnant == nombre_mise:

        print("Bravo vous avez gagné ! Vous obtenez", mise * 3, "€ !")

        argent += mise * 3

    elif numero_gagnant % 2 == nombre_mise % 2:

        mise = ceil(mise * 0.5)

        print("Vous avez misé sur la bonne couleur, bien joué ! . Vous obtenez", mise, "€")

        argent += mise

    else:

        print("Et c'est perdu ! C'est pas pour cette fois. Vous perdez votre mise.")

        argent -= mise

    if argent <= 0:

        print("Vous êtes ruiné, haha ! C'est la fin de la partie, partez d'ici ! ")



        continuer_partie = False

    else:

        print("Vous avez à présent", argent, "€")

        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")

        if quitter == "o" or quitter == "O":

            print("Vous quittez le casino avec vos gains.")

            continuer_partie = False




os.system("pause")