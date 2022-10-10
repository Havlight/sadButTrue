class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set.add(nums[i])
            else:
                return True
        return False