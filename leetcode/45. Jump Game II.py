class Solution:
    def jump(self, nums: list[int]) -> int:
        max_len = len(nums)
        pos_max = 0
        jump_max = 0
        idx = 0
        level = 0

        while pos_max - idx + 1 > 0:
            level += 1
            while idx <= pos_max:
                jump_max = max(jump_max, nums[idx] + idx)
                if jump_max >= max_len - 1:
                    return level
                idx += 1
            pos_max = jump_max

        return 0


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
