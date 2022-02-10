from Graph import Graph



class Driver():

    def load_file_to_graph(self, file_name, directed=False):
        self.graph = Graph(directed=directed)
        fileObj = open(file_name)
        fileContent = [line.split() for line in fileObj.readlines()]
        fileContent = fileContent[2:]
        for line in fileContent:
            self.graph.add_node(int(line[0]), int(line[1]))

    def dfs(self, start, npath=100):
        if self.graph is not None:
            paths = self.graph.dfs(start)[0]
            length = len(paths)
            if npath is None or npath > length:
                npath = length
            for toNode, path, _ in zip(paths.keys(), paths.values(), range(npath)):
                print(f"{toNode}: {path}")
        else:
            raise OSError("File not loaded into graph")

    def top_sort(self, file_name):
        self.load_file_to_graph(file_name, directed=True)
        print(self.graph.topological_sort())
       


    def test_dfs(self):
        G = Graph() 
        G.add_node(1, 2)
        G.add_node(1, 5)
        G.add_node(2, 5)
        G.add_node(2, 3)
        G.add_node(2, 4)
        G.add_node(3, 4)
        G.add_node(4, 5)


        
        for node, neighbors in zip(G._adj_list.keys(), G._adj_list.values()):
            print (f"{node}: {neighbors}")

        paths = G.dfs(1)[0]
        for toNode, path in zip(paths.keys(), paths.values()):
            print(f"{toNode}: {path}")

    
            

D = Driver()


### -- UNCOMMENT TO RUN DFS ON mediumG.txt -- ###
D.load_file_to_graph("../mediumG.txt")
D.dfs(0, npath=None)


### -- UNCOMMENT TO TEST DFS -- ###
# D.test_dfs()


### -- UNCOMMENT TO RUN TOPOLOGICAL SORT ON tinyAcDG.txt -- ###
# D.top_sort('../tinyAcDG.txt')
