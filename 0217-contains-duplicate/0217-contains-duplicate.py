class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=set(nums)
        if (len(l)==len(nums)):
            return False
        else:
            return True