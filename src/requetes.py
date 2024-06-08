import json

import networkx as nx

import const as c


def format_personne(personne):
    """formate une chaine de caractère pour renvoyer uniquement le nom/prenom

    Args:
        personne (str): une chaine de caractère correspondant à une personne

    Returns:
        sre: une chaine de caractère nom/prenom
    """

    if '(' in personne:
        personne = personne[:personne.index('(')]
    
    if '|' in personne:
        personne = personne[:personne.index('|')]
    
    return personne.strip("[]").strip()


def json_vers_nx(chemin):
    """converti un fichier json en graphe networkx

    Args:
        chemin (str): un chemin vers le fichier à convertir

    Returns:
        nx.Graph: un graphe networkx correspondant au fichier
    """

    G = nx.Graph()
    
    with open(file=chemin, mode='r', encoding='UTF-8') as fichier:
        for ligne in fichier.readlines():
            film = json.loads(ligne)
            personnes = set()
            
            for metier in c.COLLABS:
                personnes |= set(map(format_personne, film.get(metier, [])))
            
            for personne1 in personnes:
                for personne2 in personnes:
                    if personne1 != personne2 and not G.has_edge(personne1, personne2):
                        G.add_edge(personne1, personne2)
                        
    return G


def collaborateurs_communs(G, u, v):
    """retourne les collaborateurs en communs de deux sommets d'un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        k (str): un second sommet du graphe

    Returns:
        set: l'ensemble des collaborateurs en commun de u et v
    """

    return set(G[u]) & set(G[v]) if u in G.nodes and v in G.nodes else None


def collaborateurs_sujet(G, u, k):
    """retourne l'ensemble des collaborateurs d'un sommet à une distance k (version donnée)

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un sommet du graphe
        k (int): distance des collaborateurs de u

    Returns:
        set: l'ensemble des collaborateurs proches de u à une distance k
    """

    if u not in G.nodes:
        return None
    
    collaborateurs = set()
    collaborateurs.add(u)

    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)

        collaborateurs = collaborateurs.union(collaborateurs_directs)

    return collaborateurs


def collaborateurs_proches(G, u, k):
    """retourne l'ensemble des collaborateurs d'un sommet à une distance k

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un sommet du graphe
        k (int): distance des collaborateurs de u

    Returns:
        set: l'ensemble des collaborateurs proches de u à une distance k
    """

    if u not in G.nodes:
        return None
    
    collaborateurs = {u}
    a_parcourir = {u}
    
    for _ in range(k):
        seront_parcourus = set()
        
        for sommet in a_parcourir:
            voisins = set(G.adj[sommet])
            seront_parcourus |= voisins - collaborateurs
            
        collaborateurs |= seront_parcourus
        a_parcourir = seront_parcourus
    
    return collaborateurs

    
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

    return v in collaborateurs_proches(G, u, k) if u in G.nodes and v in G.nodes else None

    
def distance_naive(G, u, v):
    """retourne la distance entre deux sommets d'un graphe (version naive)

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str): un second sommet du graphe

    Returns:
        int: la distance entre les deux sommets
    """
    
    if u not in G.nodes or v not in G.nodes:
        return None
    
    if u == v:
        return 0
    
    for k in range(1, nx.number_of_nodes(G)):
        if est_proche(G, u, v, k):
            return k
    

def distance(G, u, v):
    """retourne la distance entre deux sommets d'un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str): un second sommet du graphe

    Returns:
        int: la distance entre les deux sommets
    """

    if u not in G.nodes or v not in G.nodes:
        return None

    if u == v:
        return 0

    niveau = 0
    niveau_actuel = {u}
    niveau_suivant = set()

    while niveau_actuel:
        courrant = niveau_actuel.pop()
        
        for voisin in G[courrant]:
            if voisin not in niveau_actuel:
                if voisin == v:
                    return niveau + 1
                
                niveau_suivant.add(voisin)
                
        if not niveau_actuel:
            niveau += 1
            niveau_actuel = niveau_suivant
            niveau_suivant = set()


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