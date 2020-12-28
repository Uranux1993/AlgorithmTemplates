# https://leetcode-cn.com/problems/subsets/

class Solution:
    def backtrack(self, cnt, pos, nums):
        if pos == len(nums):
            return [[]]
        ans = [[]]
        for i in range(pos, len(nums)):
            cnt.append(nums[i])
            for sub_ans in self.backtrack(cnt, i + 1, nums):
                ans.append([nums[i]] + sub_ans)
            cnt.pop()
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack([], 0, nums)
