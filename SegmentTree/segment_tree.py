class TreeNode:
    def __init__(self, l, r, val, left=None, right=None):
        self.l = l
        self.r = r
        self.val = val
        self.left = left
        self.right = right
        self.lazy = False
        self.lazy_val = 0

class SegmentTree:
    def __init__(self, weights: List[int]):
        self._tree = self._build(weights, 0, len(weights) - 1)

    def _build(self, weights, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(l, r, weights[l])
        m = (l + r) // 2
        left = self._build(weights, l, m)
        right = self._build(weights, m + 1, r)
        cnt_val = 0
        if left:
            cnt_val += left.val
        if right:
            cnt_val += right.val
        root = TreeNode(l, r, cnt_val, left, right)
        return root

    def _query(self, l, r, root):
        if l > r or not root or l > root.r or r < root.l:
            return 0
        if root.lazy:
            self._pushdown(root)
        r = min(r, root.r)
        l = max(l, root.l)
        if l == root.l and r == root.r:
            return root.val
        return max(self._query(l, r, root.left), self._query(l, r, root.right))

    def _pushdown(self, root):
        root.val = max(root.val, root.lazy_val)
        root.lazy_val = 0
        root.lazy = False
        if root.left:
            root.left.lazy = True
            root.left.lazy_val = max(root.left.lazy_val, root.val)
        if root.right:
            root.right.lazy = True
            root.right.lazy_val = max(root.right.lazy_val, root.val)
    
    def _range_update(self, l, r, val, root):
        if not root or root.r < l or root.l > r:
            return
        cnt_l = max(l, root.l)
        cnt_r = min(r, root.r)
        if cnt_l == root.l and cnt_r == root.r:
            root.val = max(root.val, val, root.lazy_val)
            root.lazy = True  # 打延迟标记
            root.lazy_val = root.val
            return

        root.val = max(root.val, val, root.lazy_val)
        if root.lazy:
            self._pushdown(root)
        self._range_update(l, r, val, root.left)
        self._range_update(l, r, val, root.right)

    def range_update(self, l: int, r: int, val: int):
        self._range_update(l, r, val, self._tree)

    def query(self, i: int, j: int) -> int:
        return self._query(i, j, self._tree)
