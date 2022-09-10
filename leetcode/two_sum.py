class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            if target - nums[i] in map:
                if map[target - nums[i]] != i:
                    return [i, map[target - nums[i]]]


c = Solution()

a = c.twoSum([3, 7, 11, 15, 5, 200, -191], 9)
print(a)
