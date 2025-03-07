class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[prev] = nums[i]
                prev += 1
        return prev
            
                