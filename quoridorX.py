
# -*- coding: utf-8 -*-
import copy
import networkx as nx


class QuoridorError(Exception):
    pass
class Quoridor:

    """Classe pour encapsuler le jeu Quoridor.
    Attributes:
        état (dict): état du jeu tenu à jour.
    Examples:
        >>> q.Quoridor()
    """


    def __init__(self, joueurs, murs= None):  #Constructeur de la classe Quoridor.

        """Constructeur de la classe Quoridor.
        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.
        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie. Un joueur est soit une chaîne de caractères soit un dictionnaire.
                Dans le cas d'une chaîne, il s'agit du nom du joueur. Selon le rang du joueur dans
                l'itérable, sa position est soit (5,1) soit (5,9), et chaque joueur peut
                initialement placer 10 murs. Dans le cas où l'argument est un dictionnaire,
                celui-ci doit contenir une clé 'nom' identifiant le joueur, une clé 'murs'
                spécifiant le nombre de murs qu'il peut encore placer, et une clé 'pos' qui
                spécifie sa position (x, y) actuelle. Notez que les positions peuvent être sous
                forme de tuple (x, y) ou de liste [x, y].
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions (x, y) des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions (x, y) des murs verticaux. Par défaut, il
                n'y a aucun mur placé sur le jeu. Notez que les positions peuvent être sous
                forme de tuple (x, y) ou de liste [x, y].
                """


        #Exceptions à vérifier
        if len(joueurs) != 2:  #S'il n'y a pas 2 éléments dans la liste joueurs
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")

        if murs is not None and (joueurs[0]["murs"] not in range(0, 11) \
        or joueurs[1]["murs"] not in range(0, 11)):
            #Si murs est présent et murs dans dictionnaire joueurs
            # n'est pas entre 0 et 10
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer \
            est plus grand que 10, ou négatif.")

        if murs is not None and type(murs) is not dict:
            #Si murs est présent et qu'il n'est pas de type dict
            raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")

        if len(murs['horizontaux']) + len(murs['verticaux']) + \
        joueurs[0]["murs"] + joueurs[1]["murs"] != 20:
            #La somme des nbr murs déjà placé et murs restant à jouer = 20
            raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")

        if not hasattr(joueurs, '__iter__'):   #Si joueurs n'est pas itérable
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")

        if type(joueurs[0]) is dict: #S'il y a un dictionnaire associé à joueur
            if not isinstance(joueurs[0]['pos'], (tuple, list)) \
            or not isinstance(joueurs[1]['pos'], (tuple, list)) \
            or len(joueurs[0]['pos']) != 2 \
            or len(joueurs[1]['pos']) != 2 :
                #Si la valeur de 'pos' n'est pas un (tuple OU list) ou
                # que la valeur de 'pos' n'a pas 2 valeurs
                raise QuoridorError("La position d'un joueur est invalide.")



        if type(murs) == dict:  #Si murs contient un dictionnaire
            for i in range (len(murs['horizontaux'])):
                #Pour les murs horizontaux, itérer sur chaque position de mur placé
                if not isinstance(murs['horizontaux'][i], (tuple, list)) \
                or len(murs['horizontaux']) != 2:
                    #Si les murs horizontaux ne sont pas des tuples ou list ou
                    # qui ne sont pas des pairs
                    raise QuoridorError("La position d'un mur est invalide.")

            for i in range (len(murs['verticaux'])):
                #Pour les murs verticaux, itérer sur chaque position de mur placé
                if not isinstance(murs['verticaux'][i], (tuple, list)) or \
                    len(murs['verticaux']) != 2:
                    #Si les murs verticaux ne sont pas des tuples ou
                    # list ou qui ne sont pas des pairs
                    raise QuoridorError("La position d'un mur est invalide.")


        self.joueurs = copy.deepcopy(joueurs)
        self.murs = copy.deepcopy(murs)

        self.etat_partie = self.état_partie()

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """

        grille = self.etat_partie

        #Store le nom des joueurs et leurs nbr de murs
        nom_1 = grille['joueurs'][0]['nom']
        nom_2 = grille['joueurs'][1]['nom']
        nbr_mur1 = grille['joueurs'][0]['murs']
        nbr_mur2 = grille['joueurs'][1]['murs']
        #longueur des noms pour pouvoir calculer nbr d'espace apres le nom
        l1 = len(nom_1)
        l2 = len(nom_2)
        #le nombre d'espace qu'il faut ajouter après chaque noms
        s1, s2 = 1, 1
        if l1 < l2:
            s1 += l2 - l1
        if l1 > l2:
            s2 += l1 - l2

        #constructeur pour le haut de page (la legende pissa)
        haut_page = "Légende:"
        haut_page += '\n' +  f'   1={nom_1},' + s1 * ' ' + 'murs=' + nbr_mur1 * '|'
        haut_page += '\n' +  f'   2={nom_2},' + s2 * ' ' + 'murs=' + nbr_mur2 * '|'

        #Constructeur damier
        damier = ' '*3+'-'*35+'\n'
        damier += ('  |'+' '*35+'|\n').join(
            [f'{i} |'+' '.join(
                [' . ' for _ in range(9)]
                )+'|\n' for i in range(9, 0, -1)]
            )
        damier += '-'*2+'|'+'-'*35+'\n'
        damier += '  | '+'   '.join([f'{i+1}' for i in range(9)])

        #transformer le damier en matrice pour faciliter manipulation
        damier = [list(ligne) for ligne in damier.split('\n')]

        #Ajouter coord des joueur sur le damier
        a, b = grille['joueurs'][0]['pos']
        damier[-2*b-1][4*a] = '1'
        a, b = grille['joueurs'][1]['pos']
        damier[-2*b-1][4*a] = '2'

        #Murs horizontaux
        for pos in grille['murs']['horizontaux']:
            x, y = pos
            for k in range(7):
                damier[-2*y][4*x-1+k] = '-'

        #Murs verticaux
        for pos in grille['murs']['verticaux']:
            x, y = pos
            for k in range(3):
                damier[-2*y-3+k][4*x-2] = '|'

        #Afficher le damier en string
        damier = haut_page + '\n' + '\n'.join(''.join(list(ligne)) for ligne in damier)

        return damier

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (Tuple[int, int]): Le tuple (x, y) de la position
            du jeton (1<=x<=9 et 1<=y<=9).
        """

        if joueur != 1 and joueur != 2:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')

        if position[0] > 9 or position[1] > 9 or position[0] < 1 or position[1] < 1:
            raise QuoridorError('La position est invalide (en dehors du damier)')

        for i in list(self.graphe.successors(self.current_position)):

            if i == position:
                return
            if type(i) == str:
                #Le dernier item de la liste est un str, alors
                # rendu là on sait qu'on a fini d'itérer
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")


    def état_partie(self):
        """Produire l'état actuel de la partie.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                Notez que les positions doivent être sous forme de tuple (x, y) uniquement.

        Examples:

            {
                'joueurs': [
                    {'nom': nom1, 'murs': n1, 'pos': (x1, y1)},
                    {'nom': nom2, 'murs': n2, 'pos': (x2, y2)},
                ],
                'murs': {
                    'horizontaux': [...],
                    'verticaux': [...],
                }
            }


            Les murs actuellement placés sur le damier sont énumérés dans deux listes de
            positions (x, y). Les murs ont toujours une longueur de 2 cases et leur position
            est relative à leur coin inférieur gauche. Par convention, un mur horizontal se
            situe entre les lignes y-1 et y, et bloque les colonnes x et x+1. De même, un
            mur vertical se situe entre les colonnes x-1 et x, et bloque les lignes y et y+1.
        """
        etat_partie = {
                            'joueurs': [{}, {}],
                            'murs': {
                                'horizontaux': [],
                                'verticaux': [],
                            }
                        }   # initialise le dictionnaire de base de l'état de jeu


        if self.murs != None:   #Si la partie est start
            etat_partie['murs'] = self.murs    #Ajouter les murs à l'état

        if type(self.joueurs[0]) == dict:   #Si la partie est start
            etat_partie['joueurs'][0] = self.joueurs[0]    #Ajouter joueur 1 à l'état
            etat_partie['joueurs'][1] = self.joueurs[1]    #Ajouter joueur 2 à l'état

        elif type(self.joueurs[0]) == str:  #Si la partie vient de start
            etat_partie['joueurs'][0] = {"nom": self.joueurs[0], "murs": 10, "pos": (5, 1)}
            #Ajouter position initiale joueur 1
            etat_partie['joueurs'][1] = {"nom": self.joueurs[1], "murs": 10, "pos": (5, 9)}
            #Ajouter position initiale joueur 2

        """
        Est ce que les blocs suivants sont vraiment requis?
        Ex: Si est rendu ici dans le code, on peut considérer que les exceptions
        sont tous gérée. Donc si joueur 1 est un dict, on sait que joueur 2 l'est aussi.
        
        De plus, possible de remplacer le elif plus haut en else? Pcq si pas un dict, c'est un str
        
        #if type(self.joueurs[1]) == dict:
        #    self.etat['joueurs'] += self.joueurs[1]

        #elif type(self.joueurs[1]) == str:
        #    self.etat['joueurs'] += {"nom": self.joueurs[0], "murs": 10, "pos": (5, 1)}
        """

        return etat_partie

    def jouer_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, Tuple[int, int]]: Un tuple composé du type et de la position du coup joué.
        """

        """Pour simplifier la tache, on va appeler les méthodes placer_murs, deplacer_jeton et
        les fonctions de la methode graph qui nous permettent de trouver les deplacements admisibles
        et les deplacements les plus rapides
        exemple: si on ecrit: nx.shortest_path(graphe, (5,6), 'B1'), ca nous retourne
        [(5, 6), (4, 7), (3, 7), (2, 7), (2, 8), (2, 9), 'B1'], ce qui equivaut a une liste de tous
        les points qu'il faut parcourir pour arriver a l'objectif B1"""

        """Exemple du retour généré par la fonction
        (type de move, (x,y))
        type de move == D or MH or MV
        - Déplacement
        - Mur Horizontal
        - Mur Vertical

        (x,y) == position où on pose le mur ou le jeton"""

        if joueur != 1 and joueur != 2:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')
        if self.partie_terminée() != False:
            raise QuoridorError("La partie est déjà terminée.")

        self.graphe = construire_graphe([self.joueurs[0]['pos'], self.joueurs[1]['pos']], \
        self.murs['horizontaux'], self.murs['verticaux'])

        self.current_position = tuple(self.etat_partie['joueurs'][joueur - 1]['pos'])

        next_move = nx.shortest_path(self.graphe, self.current_position, f"B{joueur}")[1]
        # next_move est une position (x,y) ou le joueur doit bouger
        self.déplacer_jeton(joueur, next_move)
        self.joueurs[joueur - 1]['pos'] = next_move

        return ('D', next_move)



    def partie_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        if self.etat_partie['joueurs'][0]['pos'][1] == 9:
            return self.etat_partie['joueurs'][0]['nom']
        if self.etat_partie['joueurs'][1]['pos'][1] == 1:
            return self.etat_partie['joueurs'][1]['nom']
        else:
            return False

    def placer_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (Tuple[int, int]): le tuple (x, y) de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').
        """
        if joueur != 1 and joueur != 2:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')
        if self.etat_partie['joueurs'][joueur - 1]['murs'] == 0:
            raise QuoridorError('Le joueur a déjà placé tous ses murs.')
        if (orientation == 'horizontal' and position[1] == 1) \
        or (orientation == 'vertical' and position[0] == 1):
            raise QuoridorError('La position est invalide pour cette orientation')

        if orientation == 'horizontal':  # ce qu'il faut verifier avant de placer un mur horizontal
            for i in self.etat_partie['murs']['horizontaux']:
                if i[1] == position[1]:
                    if i[0] == position[0] or i[0] == position[0] -1 or i[0] == position[0] + 1:
                        raise QuoridorError('Un mur occupe déjà cette position')
            for i in self.etat_partie['murs']['verticaux']:
                if i[0] == position[0]:
                    if i[1] == position[1] -1:
                        raise QuoridorError('Un mur occupe déjà cette position')

        if orientation == 'vertical':  # ce qu'il faut verifier avant de placer un mur vertical
            for i in self.etat_partie['murs']['verticaux']:
                if i[0] == position[0]:
                    if i[1] == position[1] or i[1] == position[1] +1 or i[1] == position[1] - 1:
                        raise QuoridorError('Un mur occupe déjà cette position')
            for i in self.etat_partie['murs']['horizontaux']:
                if i[0] == position[0]:
                    if i[1] == position[1] +1:
                        raise QuoridorError('Un mur occupe déjà cette position')

        if orientation == 'vertical':
            self.etat_partie['murs']["verticaux"] += position
        if orientation == 'horizontal':
            self.etat_partie['murs']["horizontaux"] += position
        if not (nx.has_path(self.graphe, self.etat_partie['joueurs'][0]['pos'], 'B1') \
        and nx.has_path(self.graphe, self.etat_partie['joueurs'][1]['pos'], 'B2')):
            raise QuoridorError("La position est invalide pour cette orientation")

        """
        2e approche pour verifier si un mur occupe deja cette position (code incomplet):
        v_interdit = []
        h_interdit = []
            for i in self.etat_partie['murs']['horizontaux']:
                h_interdit =+ i
                h_interdit =+ ((i[0] - 1), i[1])
                h_interdit =+ ((i[0] + 1), i[1])
                v_interdit =+ (i[0] + 1, i[1] - 1)
            for i in self.etat_partie['murs']['verticaux']
        if orientation == 'vertical':
        if orientation == 'horizontal': """


def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """Construire un graphe de la grille.

    Crée le graphe des déplacements admissibles pour les joueurs.
    Vous n'avez pas à modifer cette fonction.

    Args:
        joueurs (List[Tuple]): une liste des positions (x,y) des joueurs.
        murs_horizontaux (List[Tuple]): une liste des positions (x,y) des murs horizontaux.
        murs_verticaux (List[Tuple]): une liste des positions (x,y) des murs verticaux.

    Returns:
        DiGraph: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):

        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe
