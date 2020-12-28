def fast_power(self, a, b, mod):
    if b == 0:
        return 1
    m = b // 2
    sub_result = self.fast_power(a, m, mod)
    ans = sub_result ** 2
    if b % 2 == 1:
        ans *= a
    return ans % mod
