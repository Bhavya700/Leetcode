class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_sum = 0
        prev = 0 
        for num in nums:
            if num > prev:  
                max_sum += num - prev
            prev = num  
        return max_sum