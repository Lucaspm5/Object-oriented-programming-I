class Node:
    def __init__(self, distance, vertex):
        self._distance, self._vertex = distance, vertex
    
    @property
    def distance(self): 
        return self._distance
    @property
    def vertex(self): 
        return self._vertex

    def __lt__(self, other):
        return self.distance < other.distance
    def __repr__(self):
        return '{} - {}'.format(self._distance, self._vertex)
