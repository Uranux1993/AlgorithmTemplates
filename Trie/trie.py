class Trie:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.children = [None for _ in range(26)]

    def search(self, s):
        if not s:
            return True, self.is_leaf
        root = self
        for c in s:
            if not root.children[ord(c) - ord('a')]:
                return False, False
            root = root.children[ord(c) - ord('a')]
        return True, root.is_leaf

    def add(self, s):
        if not s:
            self.is_leaf = True
            return

        root = self
        for c in s:
            if not root.children[ord(c) - ord('a')]:
                root.children[ord(c) - ord('a')] = Trie()
            root = root.children[ord(c) - ord('a')]
        root.is_leaf = True


class BinTrie:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.children = [None for _ in range(2)]
        self.int_size = 32

    def int_to_bin(self, x):
        ret = bin(x)[2:]
        return '0' * (self.int_size - len(ret)) + ret

    def search(self, x):
        s = self.int_to_bin(x)
        root = self
        for c in s:
            if not root.children[ord(c) - ord('0')]:
                return False, False
            root = root.children[ord(c) - ord('0')]
        return True, root.is_leaf

    def get_max_xor(self, x):
        s = self.int_to_bin(x)
        root = self
        ans = 0
        for c in s:
            cnt_bit = ord(c) - ord('0')
            wanted = 1 - cnt_bit
            ans <<= 1
            if root.children[wanted]:
                ans += 1
                root = root.children[wanted]
            else:
                root = root.children[cnt_bit]
        return ans

    def add(self, x):
        s = self.int_to_bin(x)
        root = self
        for c in s:
            if not root.children[ord(c) - ord('0')]:
                root.children[ord(c) - ord('0')] = BinTrie()
            root = root.children[ord(c) - ord('0')]
        root.is_leaf = True
