class BinaryIndexTree:
    def __init__(self, N):
        self.N = N
        self.C = [0 for _ in range(self.N + 1)]

    def lowbit(self, x):
        return x & -x

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.C[i]
            i -= self.lowbit(i)
        return ans

    def update(self, i: int, val: int) -> None:
        diff = val - self.sumRange(i, i)
        while i <= self.N:
            self.C[i] += diff
            i += self.lowbit(i)

    def sumRange(self, i: int, j: int) -> int:
        return self.query(j) - self.query(i - 1)
