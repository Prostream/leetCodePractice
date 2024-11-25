class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [0] * n

    #只有一个优化，去长链
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
