"""
Use this file to test the Quoridor program with the API

Useful to find bug

Not to be included in the git bundle
"""

import quoridor
from api import initialiser_partie

"""
Processus

Fournir un nom de joueur
Demander à l'API d'initaliser la partie
Créer un objet de classe Quoridor avec les arguments de initialiser_partie()
Afficher à l'écran le damier
TANT QUE la partie n'est pas finie:
    Le joueur 1 décide s'il joue un mur ou bouge
    Le joueur joue son coup
    Demander à l'API d'envoyer le coup au serveur
    Créer un objet de type Quoridor avec la réponse de l'API
    Afficher à l'écran le damier
    Vérifier si la partie est gagnée ou non

Possible de faire une version où le logiciel fais jouer le joueur 2 local automatiquement
"""

if __name__ == "__main__":
    username = input("Insert name of player: ")
    ID, partie_initial = initialiser_partie(username)
    partie = quoridor.Quoridor(partie_initial['joueurs'], partie_initial['murs'])
    print(partie)

    while not partie.partie_terminée():

        mvmt_j1 = partie.jouer_coup(1)
        etat = partie.état_partie()
        mvmt_j2 = partie.jouer_coup(2)
        etat = partie.état_partie()

        print(partie)

    print(partie.partie_terminée())
