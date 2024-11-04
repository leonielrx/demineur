# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:03:31 2024

@author: Formation
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QMessageBox, QGridLayout, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
import initialisation as g
import Case as c
import Case_bombe as cb
import Case_vide as cv

class Window(QMainWindow):
    
    def __init__(self):
        """Initialisation du jeu"""
        
        super().__init__()
        self.level = self.ask_for_level()
        
        # Initialisation de la grille de jeu avec le niveau sélectionné
        if self.level:
            self.grille = g.Grille(self.level)  # Créez l'objet grille en passant le niveau
            self.grille.gen_grille_jeu()
            print(f"Grille générée pour le niveau {self.level}")  # Confirmez que la grille est générée
            self.initUI(self.grille)
        
        else:
            sys.exit()  # Fermer si aucun niveau n'est sélectionné
        
    def ask_for_level(self):
        
        # Demande le niveau à l'utilisateur
        level, ok = QInputDialog.getInt(self, "Sélection du niveau", "Choisissez un niveau (1, 2 ou 3):", min=1, max=3)
        return level if ok else None
    
    def initUI(self, grille):
        
        self.setWindowTitle('Démineur')
        self.setGeometry(100, 100, 600, 600)

        # Configuration du widget central avec une disposition en grille
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid_layout = QGridLayout()
        central_widget.setLayout(self.grid_layout)

        # Générer les cases de la grille sous la forme de bouttons
        self.buttons = []
        for row in range(len(self.grille.cases)):
            button_row = []
            for col in range(len(self.grille.cases[row])):
                case = self.grille.cases[row][col]
                button = QPushButton(str(case.value) if case.decouv else "")
                button.setFixedSize(QSize(40, 40))
                button.clicked.connect(lambda _, r=row, c=col: self.reveal_cell(r, c, grille))
                button.setContextMenuPolicy(Qt.CustomContextMenu)
                button.customContextMenuRequested.connect(lambda _, r=row, c=col: self.poser_drapeau(r, c))  # Connexion pour clic droit
                self.grid_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

        # Afficher l'état initial de la grille
        grille.afficher()
        
    def reveal_cell(self, row, col, grille):
        """Révèle une case et gère la logique associée."""
        case = self.grille.cases[row][col]
        
        if case.decouv:
            return  # Si la case est déjà révélée, on ne fait rien.

        # Appeler la méthode decouverte pour rendre la case visible
        case.decouverte()
        
        # Mettez à jour l'interface
        self.update_interface()

        if isinstance(case, cb.CaseBombe):
                QMessageBox.warning(self, "Vous avez perdu", "Vous avez cliqué sur une mine!")
                self.reveal_all_cells()  # Révèle toutes les cases, y compris les bombes
        else:
            # Vérifiez si toutes les cases vides ont été révélées
            if self.check_victory():
                QMessageBox.information(self, "Vous avez gagné", "Félicitations, vous avez révélé toutes les cases vides!")
                self.reveal_all_cells()  # Révèle toutes les cases pour montrer la victoire
        
    def poser_drapeau(self, row, col):
        """Ajoute ou enlève un drapeau sur la case sélectionnée."""
        case = self.grille.cases[row][col]
    
        # Vérifiez si la case a déjà un drapeau
        if case.drap:
            case.remove_d()  # Retire le drapeau si déjà présent
            self.buttons[row][col].setText("")  # Enlève le symbole de drapeau visuellement
        else:
            case.drapeau()  # Ajoute le drapeau
            self.buttons[row][col].setText("D")  # Affiche le symbole de drapeau
    
        self.update_interface()  # Actualiser l'interface si nécessaire
            
    def update_interface(self):
        """Met à jour l'affichage des boutons en fonction de l'état de la grille."""
        for row in range(len(self.grille.cases)):
            for col in range(len(self.grille.cases[row])):
                # Assurez-vous que chaque élément est bien une instance de Case ou de ses sous-classes
                case = self.grille.cases[row][col]  # Pas besoin de créer une nouvelle instance ici
    
                # Vérifier si la case est découverte
                if case.decouv:
                    if isinstance(case, cv.CaseVide):
                        # Affiche la valeur de la case vide (nombre de mines adjacentes)
                        self.buttons[row][col].setText(str(case.value) if case.value >= 0 else "")
                    elif isinstance(case, cb.CaseBombe):
                        # Affiche un symbole ou une lettre pour la bombe
                        self.buttons[row][col].setText("B")
                elif case.drap:
                    self.buttons[row][col].setText("D")
                else:
                    self.buttons[row][col].setText("")  # Réinitialiser pour les cases non révélées
                    
    def check_victory(self):
        """Vérifie si toutes les cases vides ont été révélées."""
        for row in self.grille.cases:
            for case in row:
                if isinstance(case, cv.CaseVide) and not case.decouv:
                    return False  # Si une case vide n'est pas découverte, le joueur n'a pas gagné
        return True  # Si toutes les cases vides sont découvertes, le joueur a gagné

    def reveal_all_cells(self):
        """Révèle toutes les cases de la grille."""
        for row in self.grille.cases:
            for case in row:
                case.decouverte()  # Marquez chaque case comme découverte
        self.update_interface()
     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())










































# from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
# from PyQt5.QtCore import QSize
# import sys
# import initialisation as g

# class MinesweeperWindow(QMainWindow):
        
#     def __init__(self):
        
#         super().__init__()
        
#         # Demander le niveau de difficulté
#         self.level = self.ask_for_level()
        
#         # Initialisation de la grille de jeu avec le niveau sélectionné
#         if self.level:
#             self.grille = g.Grille(self.level)  # Assurez-vous que le constructeur de Grille accepte un niveau
#             self.grille. gen_grille_jeu()
#             self.initUI()
#         else:
#             QMessageBox.warning(self, "Aucun niveau", "Aucun niveau sélectionné. L'application va se fermer.")
#             sys.exit()  # Fermer si aucun niveau n'est sélectionné

#     def ask_for_level(self):
#         # Demande le niveau à l'utilisateur
#         level, ok = QInputDialog.getInt(self, "Sélection du niveau", "Choisissez un niveau (1, 2 ou 3):", min=1, max=3)
#         if ok:
#             return level
#         return None

#     def initUI(self):
#         self.setWindowTitle(f'Démineur - Niveau {self.level}')
#         self.setGeometry(100, 100, 600, 600)
#         self.show()
        
#     # def initUI(self):
        
#     #     self.setWindowTitle('Démineur')
#     #     self.setGeometry(100, 100, 600, 600)
        
#     #     # Configuration de la disposition en grille
#     #     central_widget = QWidget()
#     #     self.setCentralWidget(central_widget)
#     #     self.grid_layout = QGridLayout()
#     #     central_widget.setLayout(self.grid_layout)
        
#     #     # Créer les boutons pour chaque case
#     #     self.buttons = []
#     #     for row in range(self.grille.rows):  # Assurez-vous que self.grille.rows existe
#     #         button_row = []
#     #         for col in range(self.grille.cols):  # Assurez-vous que self.grille.cols existe
#     #             button = QPushButton("")
#     #             button.setFixedSize(QSize(40, 40))
#     #             button.clicked.connect(lambda _, r=row, c=col: self.reveal_cell(r, c))
#     #             self.grid_layout.addWidget(button, row, col)
#     #             button_row.append(button)
#     #         self.buttons.append(button_row)

#     # def reveal_cell(self, row, col):
#     #     case = self.grille.get_case(row, col)  # Récupérez l’objet Case correspondant
        
#     #     if case.is_mine:
#     #         self.show_mine(row, col)
#     #         self.game_over()
#     #     else:
#     #         self.update_cell(row, col, case.adjacent_mines)
#     #         if case.adjacent_mines == 0:
#     #             self.reveal_adjacent_cells(row, col)
        
#     #     # Marquer la case comme révélée
#     #     case.is_revealed = True

#     # def show_mine(self, row, col):
#     #     self.buttons[row][col].setText("💣")
#     #     self.buttons[row][col].setStyleSheet("background-color: red;")

#     # def update_cell(self, row, col, adjacent_mines):
#     #     self.buttons[row][col].setText(str(adjacent_mines))
#     #     self.buttons[row][col].setStyleSheet("background-color: lightgray;")

#     # def reveal_adjacent_cells(self, row, col):
#     #     # Révélez les cellules adjacentes (exemple simple, adaptation à prévoir selon votre logique)
#     #     for adj_row in range(row - 1, row + 2):
#     #         for adj_col in range(col - 1, col + 2):
#     #             if 0 <= adj_row < self.grille.rows and 0 <= adj_col < self.grille.cols:
#     #                 adj_case = self.grille.get_case(adj_row, adj_col)
#     #                 if not adj_case.is_revealed:
#     #                     self.reveal_cell(adj_row, adj_col)

#     # def game_over(self):
#     #     msg = QMessageBox()
#     #     msg.setText("Game Over! Vous avez touché une mine.")
#     #     msg.exec_()

# # Exécuter l'application
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MinesweeperWindow()
#     window.show()
#     sys.exit(app.exec_())
