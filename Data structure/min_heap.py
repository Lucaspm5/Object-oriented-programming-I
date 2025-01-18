class HeapBinary:
    def __init__(self):
        self._N, self._xs = 0, [None]
        
    @property
    def N(self): return self._N
    
    @staticmethod
    def parent(i): return i >> 1
    @staticmethod
    def left_children(i): return i << 1
    @staticmethod
    def right_children(i): return i << 1 + 1
    
    def insert(self, x):
        if self._N + 1 == len(self._xs): self._xs.append(x)
        else: self._xs[self._N + 1] = x
        
        dad, curr_index = self.parent(self._N + 1), self._N + 1
        
        while(dad and self._xs[dad] > self._xs[curr_index]):
            self._xs[dad], self._xs[curr_index] = self._xs[curr_index], self._xs[dad]
            curr_index = dad
            dad = self.parent(curr_index)
        
        self._N += 1

    def get_xs(self): return self._xs[1:]

    def empty(self): return self._N == 0
    
    def min(self):
        if self.empty():
            raise ValueError('Empty heap')
        return self._xs[1]
    
    def extract_min(self):
        x = self.min()
        
        self._xs[1], self._xs[self._N] = self._xs[self._N], self._xs[1]
        self._N -= 1
        
        i = 1
        left_pointer = self.left_children(i) if self.left_children(i) <= self._N else 0
        while left_pointer:
            right_pointer = self.right_children(i) if self.right_children(i) <= self._N else 0
            
            if right_pointer and self._xs[right_pointer] < self._xs[left_pointer]:
                left_pointer = right_pointer
            
            if self._xs[i] > self._xs[left_pointer]:
                self._xs[i], self._xs[left_pointer] = self._xs[left_pointer], self._xs[i]
                i = left_pointer
                left_pointer = self.left_children(i) if self.left_children(i) <= self._N else 0
            else: left_pointer = 0
            
        return x
#------------------------------------------
try:
    priority_queue = HeapBinary()
    priority_queue.insert(7)
    priority_queue.insert(30)
    priority_queue.insert(20)
    priority_queue.insert(10)
    priority_queue.insert(5)
    
    print(priority_queue.min())
    print(priority_queue.get_xs())
    print(priority_queue.extract_min())
    print(priority_queue.get_xs())
except ValueError as error:
    print(error)
            
