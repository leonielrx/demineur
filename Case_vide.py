# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:37:59 2024

@author: Formation
"""

import Case

class CaseVide(Case.Case):
    
    def __init__(self, ligne, colonne, value, decouv = False, drap = False):
        """Constructeur des cases bombes: héritage et même attribut que la classe Case 
        avec ajout de la valeur de la case qui dépend du nombre de bombe adjacent"""
        # Appel du constructeur de la classe parente
        super().__init__(ligne, colonne, decouv, drap)
        self.value = value
        
    def __str__(self): 
        """Fonction d'affichage de la case"""
        
        return str(self.value)      
        
###TEST####
#caseV = CaseVide(1,2,1)
#print(caseV)        