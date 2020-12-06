
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
    Générer le board de base
        Faire un carré
        Délimiter les cases
        Ajouter les numéros de case
    Ajouter des éléments selon l'état de la partie
        Ajouter la position des joueurs
        Ajouter la position des murs verticaux
        Ajouter la position des murs horizontaux

"""

class QuoridorX(quoridor.Quoridor):

    def __init__(self, joueurs, murs=None):
        super().__init__(self, joueurs, murs)

    def __str__(self):
        board = turtle.Screen()
        board.title("Jeu de Quoridor")

        width = 600
        height = 600

        board_w = int(width * 0.60)
        board_h = int(height * 0.60)

        origin_x = -board_w/2
        origin_y = -board_h/2
        origin = (origin_x, origin_y)


        board.setup(width, height)
        tony = turtle.Turtle()

        #Aller à la position de démarrage
        tony.penup()
        tony.goto(origin)
        tony.pendown()

        #Faire le carré jouable
        """ tony.goto(origin_x + board_w, origin_y)
        tony.goto(origin_x + board_w, origin_y + board_h)
        tony.goto(origin_x, origin_y + board_h)
        tony.goto(origin) """

        #Générer une grille pour aider à la programation
        #On a 9 cases de jeu + 1 case avec un nombre
        #Faire une grille de 10 x 10
        #Tracer les lignes verticales
        for i in range(1, 10):
            tony.forward(i * board_w // 10)
            tony.setheading(90)
            tony.forward(board_h)
            tony.penup()
            tony.goto(origin)
            tony.setheading(0)
            tony.pendown()

        #Tracer les lignes horizontales
        for i in range(1, 10):
            tony.setheading(90)
            tony.forward(i * board_h // 10)
            tony.setheading(0)
            tony.forward(board_w)
            tony.penup()
            tony.goto(origin)
            tony.pendown()

        #Ajouter la numérotation des rangs verticaux
        tony.showturtle()
        tony.speed(1)
        tony.penup()
        tony.forward(board_w // 20)
        tony.setheading(90)
        tony.forward(board_h // 40 + board_h //10)
        for i in range(1, 10):
            tony.write(str(i), align='center', font=('Arial', '15', 'normal'))
            tony.forward(board_h // 10)
            
        #Ajouter la numérotation des rangs verticaux
        tony.goto(origin)
        tony.forward(board_h // 40)
        tony.setheading(0)
        tony.forward(board_w // 20 + board_w //10)
        for i in range(1, 10):
            tony.write(str(i), align='center', font=('Arial', '15', 'normal'))
            tony.forward(board_w // 10)
        
        tony.goto(origin)

        #Inscrire la position des joueurs sur le damier
        position_joueur = (self.etat_partie['joueurs'][0]['pos'], self.etat_partie['joueurs'][1]['pos'])
        #position_joueur = ((5,1),(5,9))
        for i in range(0, 2):
            tony.goto(origin_x + board_w //20, origin_y + board_h //40)
            tony.forward(position_joueur[i][0] * board_w // 10)
            tony.setheading(90)
            tony.forward(position_joueur[i][1] * board_h //10)
            tony.write(str(i+1), align='center', font=('Arial', '15', 'normal'))
            tony.setheading(0)

        #Ajout de la position des murs verticaux
        position_murs_verticaux = self.etat_partie['murs']['verticaux']

        tony.pensize(10)

        for i in range(len(position_murs_verticaux)):
            tony.goto(origin)
            tony.setheading(0)
            tony.forward(position_murs_verticaux[i][0] * board_w // 10)
            tony.setheading(90)
            tony.forward(position_murs_verticaux[i][1] * board_h // 10)
            tony.pendown()
            tony.forward(2 * board_h // 10)
            tony.penup()

        #Ajout position murs horizontaux
        position_murs_horizontaux = self.etat_partie['murs']['horizontaux']

        tony.setheading(0)

        for i in range(len(position_murs_horizontaux)):
            tony.goto(origin)
            tony.forward(position_murs_horizontaux[i][0] * board_w // 10)
            tony.setheading(90)
            tony.forward(position_murs_horizontaux[i][1] * board_h // 10)
            tony.setheading(0)
            tony.pendown()
            tony.forward(2 * board_w // 10)
            tony.penup()

        tony.goto(origin)