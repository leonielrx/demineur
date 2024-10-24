# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:06:19 2024

@author: Formation
"""

import cste
import numpy as np
import random
import Case 
import Case_bombe as cb
import Case_vide as cv
import initialisation as g

###Les méthodes pour le joueur###
def decouvrir_case(grille, ligne, colonne):
    """"""
    grille.cases[ligne, colonne].decouverte()
    
def poser_drapeau(grille, ligne, colonne):
    """"""
    grille.cases[ligne, colonne].drapeau()
    
def remove_drapeau(grille, ligne, colonne):
    """"""
    grille.cases[ligne, colonne].remove_d()
    
    

class Play():
    
    def __init__(self):
        
        self.fini = False
        niv = input("Quel niveau ?")
        niv = int(niv)
        
        grille_jeu = Grille(niv)
        grille_jeu.gen_grille_jeu()
        grille_jeu.afficher()
        
        while not self.fini:
#        for i in range(5):
            choice = input ("Cliquer une case ou posez un drapeau") #répondre C pour cliquer ou D pour mettre un drapeau; R retirer
            
            
            if choice == "C": 
                ligne = input("Ligne de la case à cliquer ?")
                colonne = input("Colonne de la case à cliquer ?")
            
                ligne = int(ligne)
                colonne = int(colonne)
                
                decouvrir_case(grille_jeu, ligne, colonne)
                grille_jeu.afficher()
                
                if isinstance(grille_jeu.cases[ligne, colonne], cb.CaseBombe):
                    print("tu as touché une bombe: PERDU !")
                    self.fini = True
                    
                
            elif choice == "D":
                ligne = input("Ligne du drapeau ?")
                colonne = input("Colonne du drapeau ?")
            
                ligne = int(ligne)
                colonne = int(colonne)
                
                poser_drapeau(grille_jeu, ligne, colonne)
                grille_jeu.afficher()
                
                for ligne in grille_jeu.cases:
                    for case in ligne:
                        if isinstance(case, cv.CaseVide) and not case.decouv:
                            # Si une case vide n'est pas découverte, le jeu n'est pas fini
                            break
                        elif isinstance(case, cb.CaseBombe) and not case.drap:
                            # Si une case bombe n'est pas marquée d'un drapeau, le jeu n'est pas fini
                            break
                        
                        else:
                            print("BRAVO ! Tu as gagné !")
                            self.fini = True
                
            else: 
                ligne = input("Ligne du drapeau à retirer?")
                colonne = input("Colonne du drapeau à retirer?")
            
                ligne = int(ligne)
                colonne = int(colonne)
                
                remove_drapeau(grille_jeu, ligne, colonne)
                grille_jeu.afficher()
                
                

            
        
    