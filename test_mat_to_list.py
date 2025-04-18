import unittest

def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        neighbors = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                neighbors.append(j)
        adj_list.append(neighbors)
    return adj_list

class TestMatToList(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(mat_to_list([]), [])

    def test_single_node_no_edges(self):
        self.assertEqual(mat_to_list([[0]]), [[]])

    def test_two_nodes_one_edge(self):
        self.assertEqual(mat_to_list([[0, 1], [0, 0]]), [[1], []])

    def test_undirected_graph(self):
        self.assertEqual(mat_to_list([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), [[1], [0, 2], [1]])

    def test_directed_graph(self):
        adj_mat = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]
        expected_list = [[1], [2], [3], [0]]
        self.assertEqual(mat_to_list(adj_mat), expected_list)

if _name_ == '_main_':
    unittest.main()
