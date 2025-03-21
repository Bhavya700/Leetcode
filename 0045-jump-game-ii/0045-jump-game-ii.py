class Solution:
    def jump(self, nums: List[int]) -> int:
        end=0
        far=0
        ans=0
        n=len(nums)
        for i in range(n-1):
            far=max(far, i+nums[i])
            if i == end:
                ans+=1
                end=far
                if end>=n-1:
                    break
        return ans
        


        

        