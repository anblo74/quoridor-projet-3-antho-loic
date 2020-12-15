
# -*- coding: utf-8 -*-

import turtle
import quoridor

"""
Le module quoridorX.py contient:
- Classe QuoridorX
- Méthode d'affichage graphique d'un damier avec Turtle
--------------------------------------------------------
La classe QuoridorX est définie par héritage de la classe Quoridor du module quoridor.py

La méthode d'affichage graphique d'un damier est définie par la méthode __str___
Elle remplace alors le print() en art ASCII de la classe mère Quoridor
Elle affiche à l'aide de la librairie turtle une représentation graphique du damier dans une fenêtre externe
Explication de l'implantation:
    Importer la librairie turtle
    Faire le setup avec une résolution de 800 x 800
    Définir une relation entre la position du damier et les pixels
    Générer le self.board de base
        Faire un carré
        Délimiter les cases
        Ajouter les numéros de case
    Ajouter des éléments selon l'état de la partie
        Ajouter la position des joueurs
        Ajouter la position des murs verticaux
        Ajouter la position des murs horizontaux
        
À changer:
Mettre la génération du damier de base dans le constructeur de QuoridorX
Garder la même fenêtre ouverte lors de l'exécution
Marquer les positions avec un carré de couleur et l'indiquer dans la légende
Se rappeler des derniers carrés et les effacer lors de l'update de la position
Ajouter une fenêtre en mode manuel graphique pour inscrire les positions

"""

class QuoridorX(quoridor.Quoridor):

    def __init__(self, joueurs, murs):
        quoridor.Quoridor.__init__(self, joueurs, murs=None)
        try:
            if self.board.tracer() == False:
                self.afficher()
        except:
            #Initialiser une fenêtre
            self.board = turtle.Screen()
            self.board.title("Jeu de Quoridor")

            width = 600
            height = 600

            self.board_w = int(width * 0.60)
            self.board_h = int(height * 0.60)

            self.origin_x = -self.board_w/2
            self.origin_y = -self.board_h/2
            self.origin = (self.origin_x, self.origin_y)

            self.board.setup(width, height)
            self.tony = turtle.Turtle()
            self.board.tracer(False)
            self.tony.hideturtle()

            self.tony.pencolor("white")
            self.board.bgcolor("black")

            print("Affichage durant init")
            self.afficher()

    def afficher(self):

        #Aller à la position de démarrage
        self.tony.clear()
        
        self.tony.penup()
        self.tony.goto(self.origin)
        self.tony.pendown()
        self.tony.pensize(1)

        #Faire une grille de 10 x 10
        #Tracer les lignes verticales
        for i in range(1, 11):
            self.tony.penup()
            self.tony.forward(i * self.board_w // 10)
            self.tony.setheading(90)
            self.tony.pendown()
            self.tony.forward(self.board_h)
            self.tony.penup()
            self.tony.goto(self.origin)
            self.tony.setheading(0)
            self.tony.pendown()

        #Tracer les lignes horizontales
        for i in range(1, 11):
            self.tony.penup()
            self.tony.setheading(90)
            self.tony.forward(i * self.board_h // 10)
            self.tony.pendown()
            self.tony.setheading(0)
            self.tony.forward(self.board_w)
            self.tony.penup()
            self.tony.goto(self.origin)
            self.tony.pendown()

        #Ajouter la numérotation des rangs verticaux
        self.tony.penup()
        self.tony.forward(self.board_w // 20)
        self.tony.setheading(90)
        self.tony.forward(self.board_h // 40 + self.board_h //10)
        for i in range(1, 10):
            self.tony.write(str(i), align='center', font=('Arial', '15', 'normal'))
            self.tony.forward(self.board_h // 10)
            
        #Ajouter la numérotation des rangs verticaux
        self.tony.goto(self.origin)
        self.tony.forward(self.board_h // 40)
        self.tony.setheading(0)
        self.tony.forward(self.board_w // 20 + self.board_w //10)
        for i in range(1, 10):
            self.tony.write(str(i), align='center', font=('Arial', '15', 'normal'))
            self.tony.forward(self.board_w // 10)
        
        self.tony.goto(self.origin)

        #Inscrire la position des joueurs sur le damier
        position_joueur = (self.etat_partie['joueurs'][0]['pos'], self.etat_partie['joueurs'][1]['pos'])
        for i in range(0, 2):
            self.tony.goto(self.origin_x + self.board_w //20, self.origin_y + self.board_h //40)
            self.tony.forward(position_joueur[i][0] * self.board_w // 10)
            self.tony.setheading(90)
            self.tony.forward(position_joueur[i][1] * self.board_h //10)
            self.tony.write(str(i+1), align='center', font=('Arial', '15', 'normal'))
            self.tony.setheading(0)

        #Ajout de la position des murs verticaux
        position_murs_verticaux = self.etat_partie['murs']['verticaux']

        self.tony.pensize(10)

        for i in range(len(position_murs_verticaux)):
            self.tony.goto(self.origin)
            self.tony.setheading(0)
            self.tony.forward(position_murs_verticaux[i][0] * self.board_w // 10)
            self.tony.setheading(90)
            self.tony.forward(position_murs_verticaux[i][1] * self.board_h // 10)
            self.tony.pendown()
            self.tony.forward(2 * self.board_h // 10)
            self.tony.penup()

        #Ajout position murs horizontaux
        position_murs_horizontaux = self.etat_partie['murs']['horizontaux']

        self.tony.setheading(0)

        for i in range(len(position_murs_horizontaux)):
            self.tony.goto(self.origin)
            self.tony.forward(position_murs_horizontaux[i][0] * self.board_w // 10)
            self.tony.setheading(90)
            self.tony.forward(position_murs_horizontaux[i][1] * self.board_h // 10)
            self.tony.setheading(0)
            self.tony.pendown()
            self.tony.forward(2 * self.board_w // 10)
            self.tony.penup()

        self.tony.goto(self.origin)
