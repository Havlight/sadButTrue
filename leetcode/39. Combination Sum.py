class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def dfs(nums, item=[], total=0):
            if total > target:
                return
            if total == target:
                ans.append(item)
                return
            for i in range(len(nums)):
                dfs(nums[i:], item+[nums[i]], total + nums[i])

        dfs(candidates)
        return ans


s = Solution()

print(s.combinationSum([2, 3, 5], 8))
