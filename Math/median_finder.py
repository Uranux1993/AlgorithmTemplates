# https://leetcode-cn.com/contest/season/2020-fall/problems/5TxKeK/
# https://leetcode-cn.com/problems/find-median-from-data-stream

from heapq import *


class MedianFinder:
    def __init__(self, nums=None):
        self.left_heap = []
        self.right_heap = []
        self.left_sum = self.right_sum = 0
        if nums:
            for num in nums:
                self.add(num)

    def add(self, num: int) -> None:
        heappush(self.left_heap, -num)
        self.left_sum += num + self.left_heap[0]
        self.right_sum += -self.left_heap[0]
        heappush(self.right_heap, -heappop(self.left_heap))
        if len(self.left_heap) < len(self.right_heap):
            self.right_sum -= self.right_heap[0]
            self.left_sum += self.right_heap[0]
            heappush(self.left_heap, -heappop(self.right_heap))

    def get_median(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        return -self.left_heap[0]

    def get_left_median(self) -> int:
        return -self.left_heap[0]

    def get_diff_sum(self) -> int:
        median = self.get_left_median()
        return self.right_sum - len(self.right_heap) * median + len(self.left_heap) * median - self.left_sum
