# Treino antes do dijkstra

class Graph:
    def __init__(self):
        self._neighbors, self._nameIndex, self._indexName, self._visited = [], {}, [], []
        
    def create_node(self, name):
        assert name not in self._nameIndex
        self._nameIndex[name] = len(self._nameIndex)
        self._indexName.append(name)
        self._neighbors.append([])
        self._visited.append(False)
        
    def add_edge(self, name_u, name_v, weight_uv):
        assert (name_u in self._nameIndex) and (name_v in self._nameIndex)
        u, v = self._nameIndex[name_u], self._nameIndex[name_v]
        self._neighbors[u].append((v, weight_uv))
        self._neighbors[v].append((u, weight_uv))
        
    def dfsRecursive(self, curr_node):
        print(self.get_indexName(curr_node), end = '')
        self._visited[curr_node] = True
        for neighbors in self._neighbors[curr_node]:
            if not self._visited[neighbors[0]]:
                self.dfsRecursive(neighbors[0])
                
    def dfsIterative(self, start):
        self._visited[start] = True
        st = [start]
        while st:
            curr_node = st.pop()
            print(self.get_indexName(curr_node), end = '')
            for neighbor in self._neighbors[curr_node]:
                if not self._visited[neighbor[0]]:
                    self._visited[neighbor[0]] = True
                    st.append(neighbor[0])
                    
    def bfs(self, start):
        self._visited[start] = True
        q = [start]
        while q:
            curr_node = q.pop(0)
            print(self.get_indexName(curr_node), end = '')
            for neighbor in self._neighbors[curr_node]:
                if not self._visited[neighbor[0]]:
                    self._visited[neighbor[0]] = True
                    q.append(neighbor[0])
        
    def get_nameIndex(self, name): return self._nameIndex[name]
    def get_indexName(self, indx): return self._indexName[indx]

    def clean(self): self._visited = [False] * len(self._visited)
    
teste = Graph()

teste.create_node('lucas')
teste.create_node('liedson')
teste.create_node('mateus')
teste.create_node('rai')

teste.add_edge('lucas', 'liedson', 500)
teste.add_edge('lucas', 'rai', 500)
teste.add_edge('liedson', 'rai', 500)
teste.add_edge('liedson', 'mateus', 500)

teste.dfsRecursive(teste.get_nameIndex('lucas'))
teste.clean()
print()
teste.dfsIterative(teste.get_nameIndex('lucas'))
teste.clean()
print()
teste.bfs(teste.get_nameIndex('lucas'))
