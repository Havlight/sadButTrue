from functools import lru_cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_len = len(nums)
        i = 0
        pos = 0
        while i <= pos:
            pos = max(pos, i + nums[i])
            if pos >= max_len - 1:
                return True
            i += 1
        return False
    # def canJump(self, nums: list[int]) -> bool:
    #     max_len = len(nums)
    #
    #     @lru_cache(maxsize=None)
    #     def dfs(idx=0):
    #         if idx == max_len - 1:
    #             return True
    #
    #         max_jump = nums[idx]
    #
    #         for i in range(idx + 1, min(idx + max_jump, max_len - 1) + 1):
    #             if dfs(i):
    #                 return True
    #         return False
    #
    #     return dfs()

# s = Solution()
# print(s.canJump([2, 3, 1, 1, 4]))
