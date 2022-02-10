from Graph import Graph

import time


class Driver():

    def load_file_to_graph(self, file_name):
        self.graph = Graph()
        fileObj = open(file_name)
        fileContent = [line.split() for line in fileObj.readlines()]
        fileContent = fileContent[2:]
        for line in fileContent:
            self.graph.add_node(int(line[0]), int(line[1]))

    def time_bfs(self, start, npath=100):
        files = ["mediumG.txt", "largeG.txt"]
        bothPaths = []
        for fileObj in files:
            self.load_file_to_graph(f"../{fileObj}")
            start_time = time.time()
            paths = self.graph.bfs(start)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Time for BFS on {fileObj}: {elapsed_time}")
            bothPaths.append(paths)

        # for paths in bothPaths:
        #     length = len(paths)
        #     if npath is None or npath > length:
        #         npath = length
        #     for toNode, path, _ in zip(paths.keys(), paths.values(), range(npath)):
        #         print(f"{toNode}: {path}")

        
    def test_bfs(self):
        G = Graph() 
        G.add_node(1, 2)
        G.add_node(1, 5)
        G.add_node(2, 5)
        G.add_node(2, 3)
        G.add_node(2, 4)
        G.add_node(3, 4)
        G.add_node(4, 5)


        
        for node, neighbors in zip(G.adj_list.keys(), G.adj_list.values()):
            print (f"{node}: {neighbors}")

        paths = G.bfs(1)
        for toNode, path, _ in zip(paths.keys(), paths.values(), range(6)):
            print(f"{toNode}: {path}")
            

D = Driver()

# D.test_bfs()
D.time_bfs(0, npath=None)
