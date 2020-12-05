
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
        damier = turtle.Screen()
        damier.title("Jeu de Quoridor")
        damier.setup(width=800, height=800)
        
        tony = turtle.Turtle()