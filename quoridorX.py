
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
        TODO

"""

class QuoridorX(Quoridor):

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
        tony.goto(origin_x + board_w, origin_y)
        tony.goto(origin_x + board_w, origin_y + board_h)
        tony.goto(origin_x, origin_y + board_h)
        tony.goto(origin)