def build_nxt(self, b):
    m = len(b)
    nxt = [0 for _ in range(m)]
    j = 0
    for i in range(1, m):
        while j > 0 and b[i] != b[j]:
            j = nxt[j - 1]
        if b[i] == b[j]:
            j += 1
        nxt[i] = j
    return nxt


def kmp(self, a, b):
    n = len(a)
    m = len(b)
    if m == 0:
        return 0
    if n == 0 or n < m:
        return -1

    nxt = self.build_nxt(b)
    j = 0
    for i in range(n):
        while j > 0 and a[i] != b[j]:
            j = nxt[j - 1]
        if a[i] == b[j]:
            j += 1
        if j == m:
            return i - m + 1

    return -1
