class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        s = 0
        zero = -1
        for i in range(len(nums)):
            if nums[i]==0:
                s = zero+1
                zero = i
            ans = max(ans, i-s)
        return ans
