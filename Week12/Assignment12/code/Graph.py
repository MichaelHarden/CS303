
class Graph() :
    def __init__(self, directed=False):
        self._adj_list = {}
        self._directed = directed

    def add_node(self, node, neighbor):
        if node not in self._adj_list:
            self._adj_list[node] = set()
        self._adj_list[node].add(neighbor)

        if neighbor not in self._adj_list:
            self._adj_list[neighbor] = set()
        if not self._directed:
            self._adj_list[neighbor].add(node)


    def dfs(self, start):
        paths = {start: f"{start}"}
        return self._dfs_helper(start, set(), paths)

    
    def _dfs_helper(self, node, visited, paths=None, found=None):
        visited.add(node)
        neighbors = self._adj_list[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                if paths is not None:
                    paths[neighbor] = paths[node] + f" , {neighbor}"
                self._dfs_helper(neighbor, visited, paths, found)
        if found is not None:
            found.append(node)
        return (paths, found)

    def topological_sort(self):
        if not self._directed:
            print("must be an undirected graph")
            return

        visited = set()
        topOrder = []
        
        for node in self._adj_list:
            if node not in visited:
                found = []
                self._dfs_helper(node, visited, found=found)
                for n in found:
                    topOrder.append(n)
        topOrder.reverse()
        return topOrder

        
# G = Graph(directed=True)

# G.add_node(1, 3)
# G.add_node(2, 3)
# G.add_node(3, 4)
# G.add_node(3, 5)
# G.add_node(4, 6)
# G.add_node(5, 6)
# G.add_node(6, 6)

# print(G.topological_sort())

# G.add_node(1, 2)
# G.add_node(1, 5)

# G.add_node(2, 1)
# G.add_node(2, 5)
# G.add_node(2, 3)
# G.add_node(2, 4)

# G.add_node(3, 2)
# G.add_node(3, 4)

# G.add_node(4, 2)
# G.add_node(4, 5)
# G.add_node(4, 3)

# G.add_node(5, 4)
# G.add_node(5, 2)
# G.add_node(5, 1)

# paths = G.dfs(1)[0]
# for key, value in zip(paths.keys(), paths.values()):
#     print(f"{key} : {value}")


