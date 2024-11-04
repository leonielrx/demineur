# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:37:28 2024

@author: Formation
"""

import Case

class CaseBombe(Case.Case):
    
    def __init__(self, ligne, colonne, decouv = False, drap = False):
        """Constructeur des cases bombes: héritage et même attribut que la classe Case"""
        # Appel du constructeur de la classe parente
        super().__init__(ligne, colonne, decouv, drap)
        
    def __str__(self): 
        """Fonction d'affichage de la case"""

        return "B"    
        
        