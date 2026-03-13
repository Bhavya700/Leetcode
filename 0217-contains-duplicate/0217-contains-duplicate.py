class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        l = len(set(nums))
        return l!=n