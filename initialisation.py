# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:33:28 2024

@author: Léonie Leroux
"""
import cste
import numpy as np
import random
import Case 
import Case_bombe as cb
import Case_vide as cv


class Grille:
    
    def __init__(self, niveau):
        """Initialise la grille avec un niveau spécifié, limité à 1 (facile), 2 (moyen), 3 (difficile)."""
        
        if niveau not in [0, 1, 2, 3]:
            raise ValueError("Le niveau doit être 0, 1 (facile), 2 (moyen), 3 (difficile).")
        self.niveau = niveau
        
        self.cases = np.empty((cste.niv_case[self.niveau], cste.niv_case[self.niveau]), dtype=object)  # Crée un tableau numpy vide de cases

        # Remplissage de la grille avec des objets Case
        for ligne in range(cste.niv_case[self.niveau]):
            for colonne in range(cste.niv_case[self.niveau]):
                self.cases[ligne, colonne] = Case.Case(ligne, colonne)
                
#    def afficher(self):
#        """affichage de la grille sous a forme d'une matrice"""
#
#        for ligne in self.cases:
#            l = []
#            for case in ligne:  # Utilise "case" pour itérer à travers les cases
#                if case.decouv:  # Vérifie si la case est découverte
#                    l.append(case.__str__())
#                    
#                elif case.drap:
#                    l.append("D")
#                    
#                else : 
#                    l.append("*")
#                    
#            print(l)
    def afficher(self):
        """Affichage de la grille sous la forme d'une matrice."""
        
        for ligne in self.cases:
            l = []  # Liste pour stocker la représentation de la ligne
            for case in ligne:  # Utilise "case" pour itérer à travers les cases
                if case.decouv:  # Vérifie si la case est découverte
                l.append(case.__str__())  # Ajoute la représentation de la case
                
                elif case.drap:  # Vérifie si le drapeau est posé
                    l.append("D")  # Ajoute "D" pour une case avec un drapeau
                    
                
                
                else: 
                    l.append("*")  # Ajoute "*" pour une case non découverte et sans drapeau
            
            print(" ".join(l))  # Affiche la ligne sous forme de chaîne, séparée par des espaces

                            

    def gen_grille_jeu(self):
        """génération de la grille de jeu lorsque l'utilisateur clique pour jouer"""
        
        # 1- Remplissage des bombres
        # 1-A Générer des indices aléatoires qui seront les indices des bombes
        pp = [(i,j) for i in range (cste.niv_case[self.niveau]) for j in range (cste.niv_case[self.niveau])]
        bombes = random.sample(pp, cste.niv_bombe[self.niveau])
        
        # 1-B Remplir la grille avec les bombes)
        for elem in bombes: 
            self.cases[elem[0], elem[1]] = cb.CaseBombe(elem[0], elem[1])
            
        # 2- Remplir avec les cases vides et leur donner une value
        # 2-A Parcourir la grille
        for ligne in range(cste.niv_case[self.niveau]):
            for colonne in range(cste.niv_case[self.niveau]):
                if isinstance(self.cases[ligne, colonne], cb.CaseBombe):
                    continue
                
                #2-B si ce n'est pas une case bombe
                else:
                    #2-C Compter les bombes adjacentes pour avec une value pour constuire une case vide
                    compteur = 0
                    
                    for dir in cste.directions:
                        vl = ligne + dir[0]
                        vc = colonne + dir[1]
                        
                        # Vérifier si les indices sont dans les limites de la matrice
                        if 0 <= vl < cste.niv_case[self.niveau] and 0 <= vc < cste.niv_case[self.niveau]:
                            # Vérifier si le voisin est une bombe (-1 ici)
                            if isinstance(self.cases[vl, vc], cb.CaseBombe):
                                compteur += 1
                                
                    self.cases[ligne, colonne] = cv.CaseVide(ligne, colonne, compteur)

        #3- Découvrir quelques cases pour que le joueur commence à jouer
        #on prend une case au hasard qui sera découverte ainsi que quelques cases autour
        #boucle: pour éviter de tomber sur une case bombe dès la première découverte 
        for i in range (10): 
            pc = random.sample(pp, 1)
        
            if isinstance(self.cases[pc[0][0], pc[0][1]], cb.CaseBombe):
                continue 
            
            else: 
                self.cases[pc[0][0], pc[0][1]].decouverte()
        
                for dir in cste.directions:
                    vl = pc[0][0] + dir[0]
                    vc = pc[0][1] + dir[1]
                                
                    # Vérifier si les indices sont dans les limites de la matrice
                    if 0 <= vl < cste.niv_case[self.niveau] and 0 <= vc < cste.niv_case[self.niveau]:
                        # Vérifier si le voisin est une bombe (-1 ici)
                        if isinstance(self.cases[vl, vc], cv.CaseVide):
                            self.cases[vl, vc].decouverte()
                            
            break                             






# Exemple d'utilisation
#grille = Grille(1)  # Crée une grille de 3x3
#grille.gen_grille_jeu()
#grille.afficher()  # Affiche la grille avec ses cases




