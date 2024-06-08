import unittest

import networkx as nx

import requetes as r
import const as c


"""
Classe de test des fonctions du fichier requetes.py
"""
class test_case(unittest.TestCase):  
    def setUp(self):
        self.G = nx.Graph(c.DICO_TEST)

    def test_json_vers_nx(self):
        graphe = r.json_vers_nx(c.FIC_PATH / "data_test.txt")
        self.assertEqual(graphe.adj, self.G.adj)

    def test_collaborateurs_communs(self):
        res = r.collaborateurs_communs(self.G, "a1", "d1")
        self.assertEqual(res, {'a3', 'd3', 'p2', 'd2', 'p1', 'p3', 'a2'})
        res = r.collaborateurs_communs(self.G, "p5", "d3")
        self.assertEqual(res, set())
        res = r.collaborateurs_communs(self.G, "a4", "a3")
        self.assertEqual(res, {"a2", "a5", "d2", "p2"})
        res = r.collaborateurs_communs(self.G, "a2", "p4")
        self.assertEqual(res, {"p2", "a4", "a6", "d4", "d6", "p6", "d2"})
        res = r.collaborateurs_communs(self.G, "z5", "z6")
        self.assertIsNone(res)

    def test_collaborateurs_proches(self):
        res = r.collaborateurs_sujet(self.G, "a1", 0)
        self.assertEqual(res, r.collaborateurs_proches(self.G, "a1", 0))
        res = r.collaborateurs_sujet(self.G, "a1", 1)
        self.assertEqual(res, r.collaborateurs_proches(self.G, "a1", 1))
        res = r.collaborateurs_sujet(self.G, "a1", 2)
        self.assertEqual(res, r.collaborateurs_proches(self.G, "a1", 2))
        res = r.collaborateurs_sujet(self.G, "a1", 3)
        self.assertEqual(res, r.collaborateurs_proches(self.G, "a1", 3))
        res = r.collaborateurs_proches(self.G, "z5", 1)
        self.assertIsNone(res)

    def test_est_proche(self):
        res = r.est_proche(self.G, "a1", "a1", 0)
        self.assertTrue(res)
        res = r.est_proche(self.G, "a1", "a2")
        self.assertTrue(res)
        res = r.est_proche(self.G, "a1", "a2", 2)
        self.assertTrue(res)
        res = r.est_proche(self.G, "a6", "a7", 2)
        self.assertFalse(res)
        res = r.est_proche(self.G, "z5", "z6")
        self.assertIsNone(res)

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