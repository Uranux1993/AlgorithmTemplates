def C(n, m):
    a = b = 1
    if n < m:
        m, n = n, m
    m = min(m, n - m)
    for j in range(m):
        a *= n - j
        b *= m - j
    return a // b


def A(n, m):
    if n < m:
        m, n = n, m
    ans = 1
    for i in range(m):
        ans *= n - i
    return ans
