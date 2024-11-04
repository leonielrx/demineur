# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:53:44 2024

@author: Formation
"""

class Case: 
    
    def __init__(self, ligne, colonne, decouv = False, drap = False):
        """Création d'une case définie par sa ligne et sa colonne, un paramètre de découverte par défault False, et un paramètre drapeau aussi initié à False"""
        
        self.ligne = ligne
        self.colonne = colonne
        self.decouv = decouv
        self.drap = drap
        
        
    def __str__(self): 
        """Fonction d'affichage de la case"""

        return "Case" 
  
        
    def decouverte(self):
        """Rend la case visible à l'affichange de la grille"""
        
        self.decouv = True
        
    def drapeau(self):
        """Pour poser un drapeau sur la case: permettre l'affichage d'un D sur la grille de jeu"""
        
        self.drap = True
        
    def remove_d(self):
        """Pour retirer un drapeau"""
        
        self.drap = False
        

        

####TEST####
#case = Case(1,2)
