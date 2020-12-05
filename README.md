# quoridor-projet-3-antho-loic
Repertoire pour la partie 3 du projet Quoridor GLO-1901

____________________________________________________________________________________________________________________________________
Quoridor - phase 3
Objectifs
Écrire un programme d'envergure qui fait l'intégration d'un grand nombre des principes présentés dans ce cours.

Critères d'évaluation
Bundle Git (10%)
Vous avez soumis sur le serveur du cours un bundle Git valide qui contient l'historique de votre projet. Cet historique doit comporter au moins dix (10) révisions distinctes et significatives depuis la date de début de ce projet. Ceci implique notamment de ne pas attendre la fin du projet avant de faire vos premières révisions («commit»). Cela implique aussi que vous fassiez régulièrement des révisions, c'est-à-dire chaque fois que vous complétez une étape de votre développement. Finalement, on s'attend à ce que chaque membre de l'équipe ait été l'auteur d'au moins deux révisions.

Assurez-vous que votre projet soit à la racine de votre dépôt, dans la branche master.

Normes de programmation (10%)
Le programme respecte tous les préceptes du PEP-8.

L'évaluation de ce critère sera basée sur le rapport pylint produit lors de la soumission de votre projet (voir onglet «Soumission»). N'attendez pas le jour de la remise avant de vérifier la conformité de votre programme. Vous devez minimiser le nombre de messages produit par ce rapport. Votre note sera proportionnelle à la note produite par pylint, mais pas nécessairement linéairement.

Ligne de commande (10%)
Le programme respecte les spécifications de l'énoncé concernant les options de la ligne de commande. Ceci inclut notamment:

celle qui permet d'obtenir de l'aide;
celle qui permet de jouer en mode manuel;
celle qui permet de jouer en mode automatique;
celle qui permet de jouer en mode graphique.
Classe Quoridor (20%)
Votre classe Quoridor respecte toutes les spécifications de l'énoncé du projet 2.

Classe QuoridorX (20%)
Votre classe QuoridorX respecte toutes les spécifications de cet énoncé. Ceci inclut notamment:

la classe QuoridorX est définie dans un module nommé quoridorx;
la classe QuoridorX est dérivée de la clase Quoridor;
on peut faire avec une instance de QuoridorX les mêmes choses qu'avec une instance de Quoridor;
la construction d'une instance de QuoridorX provoque la création d'une fenêtre graphique et l'affichage d'un damier avec les deux jetons dans leur position initiale;
l'appel de la méthode afficher permet de mettre à jour la représentation graphique de l'état actuel du damier.
Mode automatique (20%)
En mode automatique, votre programme est capable de jouer une partie complète avec le serveur, sans engendrer d'erreur, et en affichant l'état du damier en art ascii pour chaque coup joué.

Mode graphique et automatique (10%)
En mode graphique et automatique, votre programme est capable de jouer un partie complète avec le serveur, en affichant l'état du damier graphiquement pour chaque coup joué.

Stratégie de jeu (10% en bonus)
En mode automatique, votre programme est capable de battre le serveur.

Ce projet vaut 10% de votre note finale.

Directives
Prenez connaissance de l'énoncé du projet à l'onglet .
À l'onglet , lisez tous les documents afférents.
Soumettez votre bundle Git à l'onglet .
Vous pouvez soumettre aussi souvent que nécessaire, mais éviter de le faire inutilement.
Dans tous les cas, n'attendez pas l'échéance pour vous assurer que vous maîtrisez le processus!
Le cas échéant, posez vos questions dans le .
Échéance
Ce projet doit être complété au plus tard le lundi 14 décembre  à  23:59.
_____________________________________________________________________________________________________________________________
Quoridor - étape 3
Pour ce troisième TP, on vous demande de rajouter quelques options à la ligne de commande, d'optimiser votre stratégie de jeu dans la classe Quoridor, et de développer par héritage une nouvelle classe nommée QuoridorX (notez le X majuscule), permettant d'afficher l'état du jeu dans une fenêtre graphique.

Ligne de commande
Votre programme doit faire en sorte de supporter les options suivantes pour la ligne de commande:

python main.py --help pour avoir de l'aide.
python main.py idul pour jouer en mode manuel contre le serveur avec le nom idul.
python main.py -a idul pour jouer en mode automatique contre le serveur avec le nom idul.
python main.py -x idul pour jouer en mode manuel contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.
python main.py -ax idul pour jouer en mode automatique contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.
Dans le mode manuel (par défaut), votre boucle de jeu doit demander au joueur humain d'entrer son coup, puis le transmettre au serveur afin qu'à son tour celui-ci puisse jouer son coup. Dans le mode automatique, votre programme doit jouer automatiquement contre le serveur sans aucune intervention humaine. Dans le mode graphique, votre programme doit ouvrir une fenêtre afin de dessiner une représentation graphique de l'état du damier, contrairement aux modes précédents qui affichent ce dernier en art ascii. Vous avez carte blanche quant à l'apparence de votre représentation graphique.

Comme pour le projet 1, faites en sorte d'avoir une fonction analyser_commande dans votre module main, et que celle-ci retourne le résultat de la méthode parse_args de la classe ArgumentParser:

1
import argparse
2
​
3
​
4
def analyser_commande():
5
    # créer un analyseur de ligne de commande
6
    parser = argparse.ArgumentParser()
7
    
8
    # insérer ici les bons appels à la méthode add_argument
9
    
10
    return parser.parse_args()
La fonctionnalité help de votre programme devrait être identique à la suivante:

usage: main.py [-h] [-a] [-x] idul

Jeu Quoridor - phase 3

positional arguments:
  idul               IDUL du joueur.

optional arguments:
  -h, --help         show this help message and exit
  -a, --automatique  Activer le mode automatique.
  -x, --graphique    Activer le mode graphique.
Stratégie de jeu
Pour ce projet final, afin d'implanter le mode automatique, vous devez coder votre meilleure stratégie de jeu pour la méthode jouer_coup de votre classe Quoridor. Faites de votre mieux en vous inspirant de ce que vous trouverez sur le web. Votre objectif est de battre le serveur qui implante une stratégie relativement simple. Ce ne sera pas nécessairement facile d'y arriver, mais c'est tout à fait faisable.

La bonne approche pour aborder ce type de problème où deux adversaires s'affrontent à tour de rôle s'appelle l'algorithme du minimax. Il s'agit d'une stratégie où l'on explore récursivement les différentes options de coups suivants en cherchant à maximiser notre position lorsque c'est à notre tour de jouer, et en la minimisant lorsque c'est à l'adversaire de jouer. Ainsi, on suppose que les deux joueurs feront toujours de leur mieux pour gagner la partie. Lorsque bien implantée, cette stratégie permet de choisir le meilleur coup à jouer, surtout lorsqu'on la combine avec la stratégie d'élagage alpha-beta qui permet d'accélérer significativement le processus.

Notez bien que le serveur n'implante pas l'approche minimax, de sorte que vous n'êtes absolument pas obligé de le faire pour le battre. En fait, ne considérez cette approche que si vous êtes très à l'aise avec la programmation, que vous recherchez un défi, que vous n'avez pas froid aux yeux, et que vous avez réussi à saisir les détails de l'algorithme. Très concrètement, ceux qui ont encore de la difficulté avec la tour d'Hanoï devraient très certainement s'abstenir.

Voici quelques idées en vrac pour développer une approche ad hoc plus simple:

Utilisez le hasard pour décider si vous déplacez votre jeton ou si vous placez un mur.
Variez la probabilité de choisir le placement d'un mur en fonction du nombre de murs qui restent à placer.
Pour déplacer votre jeton, utilisez le plus court chemin dans le graphe du jeu.
Comparer votre plus court chemin avec celui de l'adversaire. Si ce dernier est plus court, placez un mur pour lui barrer le chemin sans barrer le vôtre.
Pour choisir l'emplacement d'un mur, considérez les emplacements le long du ou des plus courts chemins de l'adversaire. Faites attention de ne pas superposer des murs les uns sur les autres.
Lorsque l'adversaire s'approche du but, surtout si vous êtes vous-même plus loin du vôtre, forcez le placement d'un mur.
Etc.
Notez que ce ne sont que des suggestions et que certaines peuvent s'opposer.

Affichage graphique
Pour implanter le mode graphique, on vous demande de développer une classe graphique nommée QuoridorX qui hérite de votre classe Quoridor. Votre nouvelle classe doit permettre de faire tout ce que la classe de base peut faire, mais en ajoutant une méthode afficher pour afficher l'état actuel du damier dans une fenêtre graphique. Définissez votre classe QuoridorX dans un module nommé quoridorx.

Prenez garde de ne pas redéfinir inutilement dans QuoridorX ce qui est déjà défini dans Quoridor. Dans le constructeur de QuoridorX, commencez par faire appel au constructeur de Quoridor, puis faites les initialisations nécessaires pour créer la fenêtre graphique, puis appelez votre méthode afficher.

Pour créer votre fenêtre graphique et y dessiner un damier avec l'état actuel du jeu, vous devez obligatoirement utiliser le module de la librairie standard nommé turtle. N'utilisez aucun autre module graphique. Vous trouverez un mini tutoriel sur turtle à l'onglet des documents afférents de ce projet. Si vous rencontrez des difficultés, n'hésitez pas à poser vos questions sur le forum.

Conseils pratiques
Pour ce projet, votre bundle Git doit contenir les fichiers suivants: main.py, api.py, quoridor.py et quoridorx.py.
Il peut aussi contenir d'autres fichiers, par exemple des modules que vous auriez développé pour tester vos quatre modules ci-dessus, mais ne mettez pas n'importe quoi dans votre dépôt Git. Par exemple, votre dépôt ne devrait pas contenir les dossiers __pycache__ qui sont générés automatiquement par l'interpréteur Python, lorsqu'il exécute vos programmes. Il ne devrait surtout pas contenir vos bundles Git. De façon générale, ils ne doivent contenir que vos fichiers de code source, c'est-à-dire les fichiers dont vous avez vous-même produit le contenu. Tous les fichiers qui sont créés automatiquement par Python ou par d'autres programmes ne sont a priori pas intéressants, et ils occupent inutilement de l'espace.
À l'exception du module main, vos autres modules ne devraient rien exécuter lorsqu'on les importe. Si vous voulez inclure des tests dans ces modules, assurez-vous de les placer dans un bloc conditionnel (if) à l'expression __name__ == '__main__'.
Notez bien que la correction étant automatisée, vous avez intérêt à bien suivre les directives de cet énoncé. Si nous sommes obligés d'intervenir manuellement sur vos solutions, vous vous exposez à de fortes pénalités.
Si vous avez des questions, n'hésitez pas à les poser sur le forum.
_________________________________________________________________________________________
Roadmap
1 - Créer le rep github (done)
2 - Créer les modules et importer le code réutilisable (done)
3 - Écrire le plan de développement de chaque module (À améliorer)
4 - Implanter la logique du jeu dans main.py afin de tester le code futur (WIP)
5 - Refactorer le code importé (TODO)
6 - Coder la stratégie du jeu automatique dans la class Quoridor (TODO)
7 - Coder l'affichage graphique externe de la class QuoridorX (TODO)
8 - Débuger (TODO)
9 - Optimiser (TODO)
10 - Remettre le projet (TODO)