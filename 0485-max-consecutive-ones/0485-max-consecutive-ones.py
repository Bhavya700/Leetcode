class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        c=0
        for i in range (len(nums)):
            if nums[i]==1:
                c+=1
            else:
                ans=max(c,ans)
                c=0
        return max(ans,c)