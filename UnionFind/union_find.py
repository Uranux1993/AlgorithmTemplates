class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if self.rank[pa] <= self.rank[pb]:
            self.p[pa] = pb
        else:
            self.p[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pb] += 1


class WeightedUnionFind:
    def __init__(self, n=0, keys=None):
        if keys:
            self.p = {x: x for x in keys}
            self.weight = {x: 1.0 for x in keys}
        else:
            self.p = list(range(n))
            self.weight = [1.0] * n

    def find(self, x):
        if self.p[x] == x:
            return x
        tmp = self.p[x]
        self.p[x] = self.find(self.p[x])
        self.weight[x] *= self.weight[tmp]  # 往上累计
        return self.p[x]

    def union(self, a, b, v):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        self.p[pb] = pa
        self.weight[pb] = self.weight[a] * v / self.weight[b]
