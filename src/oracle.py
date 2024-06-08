import os
from random import randint

import networkx as nx

import requetes as r
import const as c


def make_dir(fpath):
    '''Créer un répertoire nommé fpath s'il n'existe pas déjà

    Args:
        fpath (Path): un chemin d'accès où créer le répertoire
    '''

    if not os.path.exists(fpath):
        os.makedirs(fpath)


def clear():
    """Efface le contenu du terminal"""

    os.system('cls' if os.name == 'nt' else 'clear')


def liste_fichiers(chemin):
    """Retourne la liste des fichiers présent dans un répertoire

    Args:
        path (Path): le chemin d'accès au répertoire

    Returns:
        list: la liste des fichiers .txt du répertoire
    """

    try:
        make_dir(chemin)
        
        fic_list = []
        for fic in os.listdir(chemin):
            if fic.endswith(".txt") and "test" not in fic:
                fic_list.append(fic)

        fic_list.sort()

    except:
        print('Le chemin vers le(s) fichier(s) est introuvable.')
        fic_list = []

    return fic_list


def affiche_liste(prompt, liste):
    """Affiche une liste indéxé

    Args:
        prompt (str): le texte indiquant ce que contient la liste
        liste (list): la liste que l'on veut afficher
    """

    print(f'{prompt}\n')
    for i in range(len(liste)):
        print(f'  {i + 1}. {liste[i]}')


def choisir_proposition(liste):
    """Demande à l'utilisateur, de choisir une proposition parmis une liste indéxée

    Args:
        liste (list): la liste des propositions

    Returns:
        int: l'indice de la reponse choisie
    """

    invite = '\nVeuillez choisir une propositions parmis celles proposés ci dessus: '

    reponse = input(invite)
    bornes = range(1, len(liste) + 1)
    while not reponse.isnumeric() or int(reponse) not in bornes:
        print("\n\033[93m <!> Vous devez insérer un entier assigné à l'une des propositions <!> \033[0m")
        reponse = input(invite)

    return int(reponse)


def affiche_demande(prompt, liste):
    """Affiche une liste indéxé, et demande à l'utilisateur quel proposition de la liste il veut choisir

    Args:
        prompt (str): Le texte indiquant ce que contient la liste
        liste (list): la liste de propositions

    Returns:
        int: l'indice de la reponse choisie
    """

    affiche_liste(prompt, liste)
    ind = choisir_proposition(liste)

    return ind


def affiche_distance(G, u, v="Kevin Bacon"):
    """Affiche dans le terminal la distance entre deux acteurs d'un graphe

    Args:
        G (nx.Graph): un graphe networkx
        u (str): un premier sommet du graphe
        v (str, optional): un second sommet du graphe. Defaults to "Kevin Bacon".
    """

    clear()
    dist = r.distance(G, u, v)
    
    if v == "Kevin Bacon":
        print(f"\n\033[92m{u} a un nombre de Bacon égal à {dist}\033[0m")
    else:
        print(f"\n\033[92m{u} est à une distance de {v} égale à {dist}\033[0m")


def liste_choix(liste):
    """Créer une chaine contenant des éléments d'une liste

    Args:
        liste (list): la liste que l'on veut transformer en chaine

    Returns:
        str: La chaine contenant des éléments de la liste
    """

    chaine = ""
    n = 5 if len(liste) > 5 else len(liste)
    for _ in range(n):
        ind = randint(0, len(liste) - 1)
        chaine += f"{liste[ind]}, "
        
    return chaine + "..." if n >= 5 else chaine[:-2]


def saisir_texte(ensemble, invite, exemples=True):
    """Permet à l'utilisateur de choisir un texte parmis un ensemble de chaines de caractères

    Args:
        ensemble (set): l'ensemble de chaines de caractères
        invite (str): la phrase demandant à l'utilisateur de saisir quelque chose
        exemples (bool, optional): si l'on doit afficher des exemples de textes. Defaults to True.

    Returns:
        str: La réponse de l'utilisateur
    """

    if exemples:
        print(f'\nVoici quelques exemples: {liste_choix(list(ensemble))}')

    reponse = input(invite)
    rep_possibles = {elt.lower() for elt in ensemble}

    while reponse.lower() not in rep_possibles:
        print("\n \033[93m<!> Ce n'est pas un des choix possible <!>\033[0m")
        reponse = input(invite)

    return reponse.title()


def choisir_fichier(liste_fic):
    """Permet à l'utilisateur de choisir un fichier et de le transformet en graphe

    Args:
        liste_fic (list): la liste des fichiers

    Returns:
        nx.Graph: un graphe networkx correspondant au fichier choisi
    """

    G = nx.Graph()

    if liste_fic:
        ind_fic = affiche_demande('\nVoici la liste des fichiers .txt disponibles :', liste_fic)
        print("Cela peut prendre quelques secondes ...")
        G = r.json_vers_nx(c.FIC_PATH / liste_fic[ind_fic - 1])
        print("Le fichier a été chargé !")

        return G
    
    else:
        print("\nAucun fichier .txt n'est disponible\n")


def main():
    """La fonction principale du programme"""

    clear()
    titre = '''
   ____                  __              ____   ______  _________  ______
  / __ \_________ ______/ /__     ____  / __/  /  _/ / / /_  __( )/ __  /
 / / / / ___/ __ `/ ___/ / _ \   / __ \/ /_    / // / / / / /  |// / / /
/ /_/ / /  / /_/ / /__/ /  __/  / /_/ / __/  _/ // /_/ / / /    / /_/ / 
\____/_/   \__,_/\___/_/\___/   \____/_/    /___/\____/ /_/     \____/  
                                                                        
'''
    print(f'\033[94m{titre}\033[0m')

    liste_fic = liste_fichiers(c.FIC_PATH)
    G = choisir_fichier(liste_fic)

    rep_quit = ''
    while rep_quit != 'Q' and G is not None:
        liste_recherche = [
            "Afficher le nombre de bacon d'un acteur", 
            "Afficher la distance entre deux acteurs",
            "Charger un autre fichier",
            "Quitter",
        ] 

        choix = affiche_demande('\nQue voulez vous faire ?', liste_recherche)
        clear()

        if choix == 1:
            u = saisir_texte(set(G.nodes()), "\nVeuillez renseigner le prénom et nom d'un acteur: ")
            affiche_distance(G, u)
            
        elif choix == 2:
            u = saisir_texte(set(G.nodes()), "\nVeuillez renseigner le prénom et nom d'un premier acteur: ")
            v = saisir_texte(set(G.nodes()), "\nVeuillez renseigner le prénom et nom d'un second acteur: ")
            affiche_distance(G, u, v)
            
        elif choix == 3:
            G = choisir_fichier(liste_fic)

        elif choix == 4:
            break
        
        if choix != 3:
            rep_quit = saisir_texte({'m','q'}, '\nVoulez vous retourner au menu (m) ou quitter (q) ? ', False)
            clear()


if __name__ == '__main__':
    main()
