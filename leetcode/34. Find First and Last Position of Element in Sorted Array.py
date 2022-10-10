class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = 0
        hi = len(nums) - 1

        def bs(lo=0, hi=len(nums) - 1, target=0, left=True):
            index = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    index = mid
                    if left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return index

        ls = bs(target=target)
        rs = bs(target=target, left=False)
        return [ls, rs]


s = Solution()

print(s.searchRange([3, 3, 3], 3))
