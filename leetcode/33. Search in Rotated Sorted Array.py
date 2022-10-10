class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_piov(lo=0, hi=len(nums) - 1):
            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if nums[mid] > nums[hi]:
                    if nums[mid + 1] < nums[mid]:
                        return mid + 1
                    else:
                        lo = mid
                elif nums[mid] < nums[hi]:
                    if nums[mid - 1] < nums[mid]:
                        hi = mid - 1
                    else:
                        return mid
            return lo

        def find(lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            return -1

        piov = find_piov()
        if nums[0] <= target <= nums[piov - 1]:
            return find(0, piov - 1)
        else:
            return find(piov, len(nums) - 1)


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 12))
