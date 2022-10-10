import sys


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()
        tmp = sys.maxsize
        ans = 0
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur_total = nums[i] + nums[j] + nums[k]
                if abs(cur_total - target) < tmp:
                    ans = cur_total
                    tmp = abs(cur_total - target)

                if cur_total < target:
                    j += 1
                elif cur_total > target:
                    k -= 1
                else:
                    return target
        return ans
