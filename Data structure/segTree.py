class SegTree:
    def __init__(self, arr = None, length = None):
        if arr is None:
            self._len = length
            self._segtree = [0] * (length * (2 << 1) + 1)
        else:
            self._len = len(arr)
            self._segtree = [0] * (self._len * (2 << 1) + 1)
            self._build(arr, 1, 0, self._len - 1)

    @property
    def len(self): 
        return self._len
    @property
    def segtree(self): 
        return self._segtree
    
    def _build(self, arr, curr_node, left, right):
        if left == right:
            self._segtree[curr_node] = arr[left]
            return
        middle = (left + right) >> 1
        self._build(arr, curr_node << 1, left, middle)  
        self._build(arr, (curr_node << 1) + 1, middle + 1, right)
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
    
    def first_preffix(self, at, left, right, _max, preffix):
        if left == right:
            return left
        middle = (left + right) >> 1
        sum_left = preffix + self._segtree[at << 1]
        if sum_left >= _max:
            return self.first_preffix(at << 1, left, middle, _max, preffix) 
        return self.first_preffix((at << 1) + 1, middle + 1, right, _max, sum_left)

    def set(self, ind, val):
        self.update(ind, val, 1, 0, self._len - 1)

    def range_sum(self, start, end):
        return self.query(start, end, 1, 0, self._len - 1)

    def find_min_prefix(self, val):
        return self.first_preffix(1, 0, self._len - 1, val, 0)
    
    def root(self):
        return self._segtree[1]
