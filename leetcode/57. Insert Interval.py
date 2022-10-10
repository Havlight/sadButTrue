class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        nums = intervals

        def bs(lo=0, hi=len(nums) - 1):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid][0] > newInterval[0]:
                    hi = mid - 1
                elif nums[mid][0] < newInterval[0]:
                    lo = mid + 1
                else:
                    return mid
            return lo

        idx = bs()
        nums.insert(idx, newInterval)
        ans = intervals[:idx - 1]
        for item in intervals[idx - 1:]:
            if ans and ans[-1][1] >= item[0]:
                ans[-1][1] = max(item[1], ans[-1][1])
            else:
                ans += [item]

        return ans


s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
