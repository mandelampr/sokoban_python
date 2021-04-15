
__author__ = "MOMPREMIER MANDELA"
__version__ = "1.0.0"
__date__ = "2020-28-04"

import pygame
from configuration_mawon_sokoban import *

class Grille:
    def __init__(self, fichier):
        self.ref_img = {
            MUR: pygame.image.load("images/mur.png"),
            CAISSE: pygame.image.load("images/caisse.jpg"),
            OBJECTIF: pygame.image.load("images/objectif.png"),
            CAISSE_OK: pygame.image.load("images/caisse_ok.jpg"),
        }
        self._is_fini = False
        with open (fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF :
                    self.coord_objec.append((x,y))


    def drawMap(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img in (VIDE, PLAYER) :
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x*SIZE, y*SIZE))

    
    def getPlayerPosition(self, grille):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == PLAYER :
                    return (x*SIZE, y*SIZE)


    #---Déplacement des caisses ---#
    def moveCaisse(self, x, y, pos):
        self.is_fini()
        if pos == "gauche":
            if self.lvtest[int(y)][int(x-2)] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[int(y)][int(x-1)] == CAISSE_OK:
                    self.lvtest[int(y)][int(x-1)] = OBJECTIF
                else:
                    self.lvtest[int(y)][int(x-1)] = VIDE
                if self.lvtest[int(y)][int(x-2)] == OBJECTIF:
                    self.lvtest[int(y)][int(x-2)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[int(y)][int(x-2)] = CAISSE
                    return True

        if pos == "droite":
            if self.lvtest[int(y)][int(x+2)] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[int(y)][int(x+1)] == CAISSE_OK:
                    self.lvtest[int(y)][int(x+1)] = OBJECTIF
                else:
                    self.lvtest[int(y)][int(x+1)] = VIDE
                if self.lvtest[int(y)][int(x+2)] == OBJECTIF:
                    self.lvtest[int(y)][int(x+2)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[int(y)][int(x+2)] = CAISSE
                    return True

        if pos == "haut":
            if self.lvtest[int(y-2)][int(x)] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[int(y-1)][int(x)] == CAISSE_OK:
                    self.lvtest[int(y-1)][int(x)] = OBJECTIF
                else:
                    self.lvtest[int(y-1)][int(x)] = VIDE
                if self.lvtest[int(y-2)][int(x)] == OBJECTIF:
                    self.lvtest[int(y-2)][int(x)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[int(y-2)][int(x)] = CAISSE
                    return True

        if pos == "bas":
            if self.lvtest[int(y+2)][int(x)] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[int(y+1)][int(x)] == CAISSE_OK:
                    self.lvtest[int(y+1)][int(x)] = OBJECTIF
                else:
                    self.lvtest[int(y+1)][int(x)] = VIDE
                if self.lvtest[int(y+2)][int(x)] == OBJECTIF:
                    self.lvtest[int(y+2)][int(x)] = CAISSE_OK
                    return True
                else:
                    self.lvtest[int(y+2)][int(x)] = CAISSE
                    return True
        return False

    def is_fini(self):
        lis = [self.lvtest[int(y)][int(x)] for (x, y) in self.coord_objec]
        return lis.count(CAISSE_OK) == len(self.coord_objec) or self._is_fini

    def set_is_fini(self, fini):
        self._is_fini = fini

if __name__ == '__main__' :
    g = Grille()
    g.genMap("lv1")
