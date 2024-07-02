# Implementation of Union-Find data structure

class UnionFind:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")
        self.parents = [i for i in range(n)]

    def __repr__(self):
        return f"UnionFind({self.parents})"

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u]) # Path compression
        return self.parents[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        self.parents[root_v] = root_u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def full(self):
        base = self.find(0)
        return all(self.find(i) == base for i in range(1, len(self.parents)))