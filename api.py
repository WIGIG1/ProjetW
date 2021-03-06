'Le module API sert à faire la communication avec le serveur de jeu Quoridor'



import requests


# URL de base 
URL_BASE = 'https://python.gel.ulaval.ca/quoridor/api/'


# La fonction lister parties requiert l'idul du joueur et retourne l'historique
def lister_parties(idul):
    """ La fonction lister parties retourne l'hitorique du joueur"""
    rep = requests.get(URL_BASE+'parties/', params={'idul': idul})
    if rep.status_code == 200:
        # La requête s'est déroulée normalement décoder le JSON
        rep = rep.json()
        if rep.get('message') is not None:
            # Si la réponse du serveur contient un message, la fonction soulève une erreur
            raise RuntimeError(rep['message'])
        # La fonction retourne l'historique du joueur
        return rep['parties']
        # La requête n'a pas fonctionner, la fonction affiche le code d'erreur
    return f"Le GET sur {URL_BASE+'parties'} a produit le code d'erreur {rep.status_code}."

# La fonction débuter partie requiert l'idul du joueur et retourne l'id de la partie et son état
def initialiser_partie(idul):
    """La fonction débuter partie lance une partie"""
    rep = requests.post(URL_BASE+'partie/', data={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if rep.get('message') is not None:
            # Si la réponse du serveur contient un message, la fonction soulève une erreur
            raise RuntimeError(rep['message'])
        # La fonction retourne l'id de la partie et son état de départ
        return (rep['id'], rep['état'])
        # La requête n'a pas fonctionner, la fonction affiche le code d'erreur
    return f"Le GET sur {URL_BASE+'parties'} a produit le code d'erreur {rep.status_code}."


# La fonction jouer coup requiert l'id de la partie, le type de coup et sa posisiton
def jouer_coup(id_partie, type_coup, pos):
    """La fonction joueur coup permet de jouer un coup"""
    rep = requests.put(URL_BASE+'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': pos})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if rep.get('message') is not None:
            # Si la réponse du serveur contient un message, la fonction soulève une erreur
            raise RuntimeError(rep['message'])
        if rep.get('gagnant') is not None:
            # S'il y a un gagnant, la focntion soulève une erreur
            raise StopIteration(rep['gagnant'])
        # La fonction retourne le nouvel état de la partie.
        return rep['état']
        # La requête n'a pas fonctionner, la fonction affiche le code d'erreur
    return f"Le GET sur {URL_BASE+'parties'} a produit le code d'erreur {rep.status_code}."
