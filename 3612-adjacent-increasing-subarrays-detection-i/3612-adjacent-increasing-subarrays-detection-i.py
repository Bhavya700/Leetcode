class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        step = k-1
        n=len(nums)
        if k==1:
            return n>=2
        for i in range(k+1,n):
            if nums[i]>nums[i-1] and nums[i-k]>nums[i-k-1]:
                step -= 1
            else:
                step = k-1
            if step==0:
                return True
        return False

           


