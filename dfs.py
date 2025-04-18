def reachable(adj_list, start_node):
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)

    dfs(start_node)
    return visited
