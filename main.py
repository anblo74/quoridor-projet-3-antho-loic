import quoridor
import quoridorX
import argparse
from api import initialiser_partie, jouer_coup

"""
Définir une fonction qui accepte les arguments de la ligne de commande:
python main.py --help pour avoir de l'aide.
python main.py idul pour jouer en mode manuel contre le serveur avec le nom idul.
python main.py -a idul pour jouer en mode automatique contre le serveur avec le nom idul.
python main.py -x idul pour jouer en mode manuel contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.
python main.py -ax idul pour jouer en mode automatique contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique
_____________________________________________________
La fonctionnalité --help affiche la réponse suivante:
usage: main.py [-h] [-a] [-x] idul

Jeu Quoridor - phase 3

positional arguments:
    idul               IDUL du joueur.

optional arguments:
    -h, --help         show this help message and exit
    -a, --automatique  Activer le mode automatique.
    -x, --graphique    Activer le mode graphique.
___________________________________________________

Voir code partie 1 pour référence

========================================================
Le module main.py permet de faire rouler le jeu. Il doit respecter le fonctionnement voulu par le professeur:
Dans le mode manuel (par défaut), votre boucle de jeu doit demander au joueur humain d'entrer son coup,
puis le transmettre au serveur afin qu'à son tour celui-ci puisse jouer son coup.
Dans le mode automatique, votre programme doit jouer automatiquement contre le serveur sans aucune intervention humaine.
Dans le mode graphique, votre programme doit ouvrir une fenêtre afin de dessiner une représentation graphique de l'état du damier,
contrairement aux modes précédents qui affichent ce dernier en art ascii.
Vous avez carte blanche quant à l'apparence de votre représentation graphique.
------------------------------------------------------------------------------
Ce qu'il faut programmer:

Par défaut, lorsqu'il n'y a pas d'argument optionnel dans la CLI on start le mode manuel.
    Mode manuel: (mix partie 1 & 2)
    Envoyer un POST pour initialiser la partie
    Initialiser un objet de classe Quoridor avec un deep copy
    Afficher à l'écran le damier en ASCII
    Tant que la partie n'est pas finie:
        Demander le type de coup (D, MH, MV)
        Indiquer la position (x, y) du déplacement
        Transmettre via un PUT au serveur le move du joueur
        Initialiser la réponse du serveur comme un objet de classe Quoridor
        Afficher à l'écran en ASCII l'état de la partie
        Si la partie est terminée, afficher le nom du gagnant
        
Lorsque l'argument -a est utilisé dans la CLI, on start le mode automatique.
    Mode automatique: (semblable partie 2)
        Envoyer un POST pour initialiser la partie
        Initialiser un objet de classe Quoridor avec un deep copy
        Afficher le damier à l'écran en ASCII
        Tant que la partie n'est pas fini:
            Le programme choisi le meilleur move possible
            Transmettre via un PUT au serveur le move du joueur
            Initialiser la réponse du serveur comme un objet de classe Quoridor
            Afficher à l'écran en ASCII l'état de la partie
            Si la partie est terminée, afficher le nom du gagnant

Lorsque l'argument -x est utilisé dans la CLI, on active le mode graphique
    Mode graphique: (s'ajoute aux modes du jeu)
        Initialiser la partie en envoyant un POST au serveur.
        Initialiser un objet de classe QuoridorX avec un deep copy
        Afficher le damier sous forme graphique dans une fenêtre externe
        Tant que la partie n'est pas finie:
            Choisir le coup selon le mode actif
            Transmettre via un PUT au serveur le move du joueur
            Initialiser la réponse du serveur comme un objet de classe QuoridorX
            Afficher le damier sous forme graphique dans une fenêtre externe
            Si la partie est terminée, afficher le nom du gagnant

"""

def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description= "Jeu Quoridor - phase 3")
    parser.add_argument('idul', help = 'IDUL du joueur')
    parser.add_argument('-a', '--automatique', action = 'store_true', help = 'Activer le mode automatique.')
    parser.add_argument('-x', '--graphique', action = 'store_true', help = 'Activer le mode graphique.')
    return parser.parse_args()


if __name__ == "__main__":

    ###Analyse les arguments de la CLI
    #Retourne l'idul du joueur
    idul = analyser_commande().idul

    #Retourne True si -a présent, sinon False
    mode_auto = analyser_commande().automatique

    #Retourne True si -x présent, sinon False
    mode_graph = analyser_commande().graphique


    ###Initialise la partie
    #Envoyer un POST pour initialer la partie
    ID, partie_initial = initialiser_partie(idul)

    ##Crée l'objet de jeu avec la classe demandée
    #Si le mode graphique est actif, utiliser la classe QuoridorX
    if mode_graph == True:
        partie = quoridorX.QuoridorX(partie_initial['joueurs'], partie_initial['murs'])

    #Si le mode graphique est inactif, utiliser la classe Quoridor
    else:
        partie = quoridor.Quoridor(partie_initial['joueurs'], partie_initial['murs'])

    #Afficher le damier selon la classe
    print(partie)

    ###Exécuter ce code tant qu'il n'y a pas de gagnant
    while not partie.partie_terminée():
        ##Le joueur 1 choisi son coup selon le mode spécifié
        #Si le mode automatique est activé, choisir automatique le coup
        if mode_auto == True:
            mvmt_j1 = partie.jouer_coup(1)
            #TODO
            type_coup = 0
            position = 0

        #Si le mode manuel est activé, l'utilisateur choisi le coup à jouer
        else:
            #Demander au joueur de spécifier son coup
            print("Type de coup disponible :\n "
                "- D : Déplacement\n "
                "- MH: Mur Horizontal\n "
                "- MV: Mur Vertical")

            #Détermine si le joueur utilise déplace le pion ou met un mur
            type_coup = input('Choisissez votre type de coup (D, MH ou MV) :').upper()

            #Définir la position relative de son coup
            position = (input('Définissez la position en X de votre coup :'),
            input('Définissez la position en Y de votre coup :'))

        #Envoyer le coup au serveur via un PUT
        ID, etat_partie = jouer_coup(ID, type_coup, position)

        ##Update l'objet de jeu avec l'état actuel et la classe demandée
        #Si le mode graphique est actif, utiliser la classe QuoridorX
        if mode_graph == True:
            partie = quoridorX.QuoridorX(etat_partie['joueurs'], etat_partie['murs'])

        #Si le mode graphique est inactif, utiliser la classe Quoridor
        else:
            partie = quoridor.Quoridor(etat_partie['joueurs'], etat_partie['murs'])

        #Afficher le damier selon la classe
        print(partie)

    print(partie.partie_terminée())