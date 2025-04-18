def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        neighbors = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                neighbors.append(j)
        adj_list.append(neighbors)
    return adj_list
