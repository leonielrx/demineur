# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:58:52 2024

@author: Formation
"""

###Fichier de constante qui gère les différents niveaux###

niv_case = {
    0: 4,
    1: 10,
    2: 18,
    3: 24
}

niv_bombe = {
    1: 10,
    2: 40,
    3: 99
}

directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Haut-gauche, Haut, Haut-droit
        (0, -1),          (0, 1),     # Gauche,         Droite
        (1, -1), (1, 0), (1, 1)       # Bas-gauche, Bas, Bas-droit
    ]