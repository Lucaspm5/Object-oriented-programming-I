class SegTree:
    def __init__(self, arr = None, length = None):
        self._len = len(arr)
        self._segtree = [0] * (self._len * (2 << 1) + 1)
        self.build(arr, 1, 0, self._len - 1)

    @property
    def len(self): 
        return self._len
    @property
    def segtree(self): 
        return self._segtree
    
    def build(self, arr, curr_node, left, right):
        if left == right:
            self._segtree[curr_node] = arr[left]
            return
        middle = (left + right) >> 1
        self.build(arr, curr_node << 1, left, middle)  
        self.build(arr, (curr_node << 1) + 1, middle + 1, right)
        self._segtree[curr_node] = self._segtree[curr_node << 1] + self._segtree[(curr_node << 1) + 1]
    
    def update(self, ind, x, curr_node, left, right):
        if left == right:
            self._segtree[curr_node] = x 
            return
        middle = (left + right) >> 1
        if ind <= middle:
            self.update(ind, x, curr_node << 1, left, middle) 
        else:
            self.update(ind, x, (curr_node << 1) + 1, middle + 1, right)
        self._segtree[curr_node] = self._segtree[curr_node << 1] + self._segtree[(curr_node << 1) + 1]
    
    def query(self, i, j, curr_node, l, r):
        if r < i or j < l:
            return 0  
        if i <= l and r <= j:
            return self._segtree[curr_node] 
        middle = (l + r) >> 1
        L = self.query(i, j, curr_node << 1, l, middle)  
        R = self.query(i, j, (curr_node << 1) + 1, middle + 1, r)  
        return L + R

    def set(self, ind, val):
        self.update(ind, val, 1, 0, self._len - 1)

    def range_sum(self, start, end):
        return self.query(start, end, 1, 0, self._len - 1)
    
    def root(self):
        return self._segtree[1]
