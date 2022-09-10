class Solution:
    def threeSum(self, nums: list[int]):
        nums.sort()
        hash_set = set()

        for i in range(len(nums)):
            tar_val = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                n = nums[j] + nums[k]
                if n < tar_val:
                    j += 1
                elif n > tar_val:
                    k -= 1
                else:
                    hash_set.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return list(hash_set)


li = [-1, 0, 1, 2, -1, -4]

s = Solution().threeSum(li)
print(s)
