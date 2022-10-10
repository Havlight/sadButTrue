import sys

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        total = 0
        ans = -sys.maxsize
        for i in range(len(nums)):
            total += nums[i]
            ans = max(ans, total)
            if total < 0: total = 0
        return ans
