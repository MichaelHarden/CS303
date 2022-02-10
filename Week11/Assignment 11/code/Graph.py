from os import path


class Graph() :
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node, neighbor):
        try:
            self.adj_list[node].add(neighbor)
        except KeyError:
            self.adj_list[node] = set()
            self.adj_list[node].add(neighbor)

        
        try:
            self.adj_list[neighbor].add(node)
        except KeyError:
            self.adj_list[neighbor] = set()
            self.adj_list[neighbor].add(node)
        
    def bfs(self, start):
        queue = []
        was_queued = set()
        paths = {}
        try:
            self.adj_list[start]
            queue.append(start)
            was_queued.add(start)
            paths[start] = f'{start}'
        except KeyError:
            print('Start node, not found')
        
        while len(queue) != 0:
            node = queue.pop(0)
            neighbors = self.adj_list[node]
            
            for neighbor in neighbors:
                if neighbor in was_queued:
                    continue
                queue.append(neighbor)
                was_queued.add(neighbor)
                paths[neighbor] = f'{paths[node]} -> {neighbor}'
        return paths







# G = Graph()
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

# paths = G.bfs(1)
# for key in paths:
#     print(paths[key])
