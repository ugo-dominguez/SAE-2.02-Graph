import json

import networkx as nx


def json_vers_nx(chemin):
    """converti un fichier json en graphe networkx

    Args:
        chemin (str): un chemin vers le fichier à convertir

    Returns:
        nx.Graph: un graphe networkx correspondant au fichier
    """
    ...


def collaborateurs_communs(G, u, v):
    """retourne les collaborateurs en communs de deux sommets d'un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        k (str): un second sommet du graphe

    Returns:
        set: l'ensemble des collaborateurs en commun de u et v
    """
    ...


def collaborateurs_sujet(G, u, k):
    """retourne l'ensemble des collaborateurs d'un sommet à une distance k (version donnée)

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un sommet du graphe
        k (int): distance des collaborateurs de u

    Returns:
        set: l'ensemble des collaborateurs proches de u à une distance k
    """
    ...


def collaborateurs_proches(G, u, k):
    """retourne l'ensemble des collaborateurs d'un sommet à une distance k

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un sommet du graphe
        k (int): distance des collaborateurs de u

    Returns:
        set: l'ensemble des collaborateurs proches de u à une distance k
    """
    ...

    
def est_proche(G, u, v, k=1):
    """indique si deux sommets sont à une distance k l'un de l'autre dans un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str): un second sommet du graphe
        k (int, optional): la distance à laquelle on veut vérifier. Defaults to 1.

    Returns:
        boolean: un boolean indiquant si les sommets sont à une distance k ou non
    """
    ...

    
def distance_naive(G, u, v):
    """retourne la distance entre deux sommets d'un graphe (version naive)

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str): un second sommet du graphe

    Returns:
        int: la distance entre les deux sommets
    """
    ...
    

def distance(G, u, v):
    """retourne la distance entre deux sommets d'un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str): un second sommet du graphe

    Returns:
        int: la distance entre les deux sommets
    """
    ...


def centralite(G, u):
    """retourne la distance maximale entre un sommet u et n'importe quel autre sommet du graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un sommet du graphe

    Returns:
        int: la distance maximale entre le sommet u et un autre sommet du graphe
    """
    ...


def centre_hollywood(G):
    """retourne le sommet le plus central d'un graphe

    Args:
        G (nx.Graph): un graphe networkx

    Returns:
        str: le sommet le plus central du graphe
    """
    ...


def eloignement_max(G):
    """retourne la plus grande distance entre deux sommet d'un graphe

    Args:
        G (nx.Graph): un graphe networkx

    Returns:
        int: la plus grande distance entre deux sommet du graphe
    """
    ...