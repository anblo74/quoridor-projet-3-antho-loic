# -*- coding: utf-8 -*-
import requests

URL = "https://python.gel.ulaval.ca/quoridor/api/"


def lister_parties(idul):

    rep = requests.get(f'{URL}parties/' , params={'idul': f'{idul}'})
    #cas ou la requete se deroule normalement
    if rep.status_code == 200:
        rep = rep.json()
        return rep['parties']

    # Soulever Runtime_error et afficher le message contenue dans la cle "message" du dico
    if rep.status_code == 406:
        rep = rep.json()
        mess = rep['message']
        raise RuntimeError(f'{mess}')

def initialiser_partie(idul):
    rep = requests.post(f'{URL}partie/', data={'idul': f'{idul}'})
    if rep.status_code == 200:
    #retourne tupple avec id de la partie et etat initial de la nouvelle partie
        rep = rep.json()
        return (rep['id'], rep['état'])
    # Si erreur 406, le JSON va contenir un message d'erreur
    # Soulever Runtime_error et afficher ce message
    if rep.status_code == 406:
        rep = rep.json()
        mess = rep['message']
        raise RuntimeError(f'{mess}')

def jouer_coup(id_partie, type_coup, position):

    rep = requests.put(f'{URL}jouer/', data={'id': id_partie, 'type': type_coup, 'pos':position})
    if rep.status_code == 200:
        rep = rep.json()
        #La partie se termine et on affiche le nom du gagnant
        winner = rep['gagnant']
        if winner is not None:
            raise StopIteration(f'{winner}')
        #retourne un tupple avec id et etat de la partie
        return (rep['id'], rep['état'])

    if rep.status_code == 406:
        rep = rep.json()
        mess = rep['message']
        raise RuntimeError(f'{mess}')
