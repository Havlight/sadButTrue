class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []

        def dfs(nums, idx, path, total=0):
            if total > target:
                return
            if total == target:
                ans.append(path)
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, path + [nums[i]], total + nums[i])

        dfs(sorted(candidates), 0, [], 0)

        return ans


s = Solution()
print(s.combinationSum2([2, 2, 3, 5], 8))
