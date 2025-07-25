class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        pos = True
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                if nums[i]>0:
                    ans += nums[i] 
                    pos = False

        if pos:
            return max(nums)
        return ans