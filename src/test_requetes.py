import unittest

import networkx as nx

import requetes as r


"""
Classe de test des fonctions du fichier requetes.py
"""
class test_case(unittest.TestCase):  
    def setUp(self):
        ...

    def test_json_vers_nx(self):
        ...

    def test_collaborateurs_communs(self):
        ...

    def test_collaborateurs_proches(self):
        ...

    def test_est_proche(self):
        ...

    def test_distance_naive(self):
        ...

    def test_distance(self):
        ...

    def test_centralite(self):
        ...

    def test_centre_hollywood(self):
        ...

    def test_eloignement_max(self):
        ...


if __name__ == '__main__':
    unittest.main()