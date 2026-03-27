class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmax = 0
        cmin = 0
        gmax = nums[0]
        gmin = nums[0]
        total = 0
        for a in nums:
            total+=a
            cmax = max(cmax+a, a)
            gmax = max(cmax, gmax)
            cmin = min(cmin+a, a)
            gmin = min(gmin, cmin)
        
        if gmax<0:
            return gmax
        return max(total-gmin, gmax)
        
