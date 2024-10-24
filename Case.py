# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:53:44 2024

@author: Formation
"""

class Case: 
    
    def __init__(self, ligne, colonne, decouv = False, drap = False):
        """Création d'une case définie par sa ligne et sa colonne, paramètre découvert = False par défault"""
        
        self.ligne = ligne
        self.colonne = colonne
        self.decouv = decouv
        self.drap = drap
        
        
    def __str__(self): 
        """Fonction d'affichage de la case"""

        return "Case" 
  
        
    def decouverte(self):
        """Rend la case visible à l'utilisateur après l'initialisation de la grille, un clique ou une case vide entourée"""
        
        self.decouv = True
        
    def drapeau(self):
        """Rend la case visible à l'utilisateur après l'initialisation de la grille, un clique ou une case vide entourée"""
        
        self.drap = True
        
    def remove_d(self):
        """Rend la case visible à l'utilisateur après l'initialisation de la grille, un clique ou une case vide entourée"""
        
        self.drap = False
        

        

####TEST####
#case = Case(1,2)
