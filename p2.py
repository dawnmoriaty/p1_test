class SegmentTree:
    def __init__(self, data, k):
        self.n = len(data)
        self.k = k
        self.tree = [0] * (4 * self.n)
        self.create(data, 0, 0, self.n - 1)

    def create(self, data, node, start, end):
        if start == end:
            self.tree[node] = self.calculate_b(data[start],start)
        else:
            mid = (start + end) // 2
            self.create(data, 2 * node + 1, start, mid)
            self.create(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
# cal b[x]
    def calculate_b(self, value,idx):
        if idx % self.k == 0 or str(self.k) in str(idx):
            return 2 * value
        return value
#update idx
    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = self.calculate_b(value,idx)
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, value, 2 * node + 1, start, mid)
            else:
                self.update(idx, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
#sum[L,R]
    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(L, R, 2 * node + 1, start, mid)
        right_sum = self.query(L, R, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    k = 2
    seg_tree = SegmentTree(a, k)
    seg_tree.update(2, 10, 0, 0, len(a) - 1)
    result = seg_tree.query(1, 4, 0, 0, len(a) - 1)
    print(result)
