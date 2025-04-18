import unittest
from dfs import reachable

class TestDFS(unittest.TestCase):
    def test_reachable_from_0(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        result = reachable(adj_list, 0)
        self.assertEqual(result, {0, 1, 2, 3, 4})

    def test_reachable_from_3(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        result = reachable(adj_list, 3)
        self.assertEqual(result, {3, 4})

if _name_ == '_main_':
    unittest.main()
