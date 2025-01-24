from node import Node
from min_heap import HeapBinary

oo = float('inf')

class Graph:
    def __init__(self):
        self._neighbors, self._nameIndex, self._indexName, self._visited = [], {}, [], []
        self._distance, self._parent = [], []
        
    def create_node(self, name):
        assert name not in self._nameIndex
        self._nameIndex[name] = len(self._nameIndex)
        self._indexName.append(name)
        self._neighbors.append([])
        self._distance.append(oo)
        self._parent.append(oo)
        self._visited.append(False)
    
    def remove_node(self, nome):
        assert nome in self._nameIndex
        idx = self._nameIndex[nome]

        for neighbor in self._neighbors[idx]:
            v = neighbor.vertex
            self._neighbors[v] = [node for node in self._neighbors[v] if node.vertex != idx]

        self._nameIndex.pop(nome)
        self._indexName.pop(idx)
        self._neighbors.pop(idx)
        self._distance.pop(idx)
        self._parent.pop(idx)
        self._visited.pop(idx)

        for i in range(len(self._nameIndex)):
            for neighbor in self._neighbors[i]:
                if neighbor.vertex > idx:
                    neighbor.vertex -= 1

            self._nameIndex[self._indexName[i]] = i
    
    def add_edge(self, name_u, name_v, weight_uv):
        assert (name_u in self._nameIndex) and (name_v in self._nameIndex)
        u, v = self._nameIndex[name_u], self._nameIndex[name_v]
        self._neighbors[u].append(Node(weight_uv, v))
        self._neighbors[v].append(Node(weight_uv, u))
    
    def remove_edge(self, nome_u, nome_v):
        assert (nome_u in self._nameIndex) and (nome_v in self._nameIndex)
        u, v = self._nameIndex[nome_u], self._nameIndex[nome_v]

        self._neighbors[u] = [node for node in self._neighbors[u] if node.vertex != v]
        self._neighbors[v] = [node for node in self._neighbors[v] if node.vertex != u]
    
    def get_nameIndex(self, name): return self._nameIndex[name]
    def get_indexName(self, indx): return self._indexName[indx]
    def get_distance(self, destino): return self._distance[self.get_nameIndex(destino)]
    def get_nameNodes(self): return self._nameIndex
    
    def dijkstra(self, start):
        self._distance[start], self._parent[start] = 0, oo
        
        priority_queue = HeapBinary()
        priority_queue.insert(Node(0, start)) 
        
        while not priority_queue.empty():
            node = priority_queue.extract_min() 
            d, u = node.distance, node.vertex  
            
            if self._visited[u]: continue            
            for node in self._neighbors[u]:
                v, w = node.vertex, node.distance
                if self._distance[v] > d + w:
                    self._distance[v] = d + w
                    self._parent[v] = u
                    priority_queue.insert(Node(self._distance[v], v))
            self._visited[u] = True
    
    def restore_path(self, start, end):
        path, v = [], end
        while v != start:
            assert not self._parent[v] == oo
            path.append(self.get_indexName(v))
            v = self._parent[v]
        path.append(self.get_indexName(start))
        path.reverse()  
        return path
    
    def clean(self):
        n = len(self._neighbors)
        self._visited = [False] * n
        self._distance, self._parent = [oo] * n, [oo] * n 
