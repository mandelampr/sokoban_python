
__author__ = "MOMPREMIER MANDELA"
__version__ = "1.0.0"
__date__ = "2020-28-04"

import pygame
import sys
from pygame.locals import *

from matrice import Grille
from player import Player
from configuration_mawon_sokoban import *

pygame.init()
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

screen_width=LARGEUR
screen_height=HAUTEUR
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

def main_menu():

    menu=True
    font = pygame.font.get_default_font()
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    game()
                elif event.key==pygame.K_F2:
                    pygame.quit()
                    quit()
                # if event.key==pygame.K_F3:
                #     pygame.quit()
                #     quit()

        # Main Menu UI
        screen.fill(black)
        title=text_format("Jeu sokoban", font, 40, red)
        title_sub = text_format("Bravo !", pygame.font.get_default_font(), 40, red)
        accueil = pygame.image.load("images/mawon.png")
        # Rafraichissement
        pygame.display.get_surface()
        text_jouer = text_format("F1: Jouer", font, 25, light_yellow)
        text_ajouter = text_format("F2: Ajouter un niveau", font, 25, light_yellow)
        text_menu = text_format("F3: Menu principal", font, 25, light_yellow)

        # Main Menu Text
        screen.blit(title, (40, 40))
        screen.blit(accueil, (40, 100))

        screen.blit(text_jouer, (40, 150))
        screen.blit(text_ajouter, (40, 200))
        screen.blit(text_menu, (40, 250))
        pygame.display.update()
        # clock.tick(FPS)
        pygame.display.set_caption("Sokoban")

def menu_reussite():

    menu=True
    continuer = True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_F4:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_F3:
                    continuer = False
        if not continuer:
            break
        # Main Menu UI
        screen.fill(black)
        title_sub1=text_format("Niveau réussi !", pygame.font.get_default_font(), 40, red)
        text_menu_sub = text_format("F3: Menu principal", pygame.font.get_default_font(), 25, light_yellow)
        text_suivant = text_format("F4: Niveau suivant", pygame.font.get_default_font(), 25, light_yellow)

        title_sub.get_rect()
        title_sub1.get_rect()
        text_menu_sub.get_rect()
        text_suivant.get_rect()

        # Main Menu Text
        screen.blit(title_sub, (40, 40))
        screen.blit(title_sub1, (40, 150))
        screen.blit(text_menu_sub, (40, 250))
        screen.blit(text_suivant, (40, 300))
        pygame.display.update()
        # clock.tick(FPS)
        pygame.display.set_caption("Sokoban")
    return continuer

def game():
    background = pygame.image.load("images/fond.jpg")

    screen.blit(background, (0, 0))

    _grille = Grille("fichiers/lv1")
    _grille.drawMap(screen)

    _player = Player(_grille)
    _player.drawPlayer(screen)

    pygame.display.flip()

    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F3:
                    continuer = False
                else:
                    _player.move(event.key)
                    if event.key == K_r:
                        _grille.genMap("fichiers/lv1")
                        _grille.drawMap(screen)
                        _player = Player(_grille)
                        _player.drawPlayer(screen)
        if _grille.is_fini():
            continuer = menu_reussite()
        screen.blit(background, (0, 0))
        _grille.drawMap(screen)
        _player.drawPlayer(screen)
        pygame.display.flip()


#Initialize the Game
main_menu()
pygame.quit()
quit()