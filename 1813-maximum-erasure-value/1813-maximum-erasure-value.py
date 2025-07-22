class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        curr = 0
        l = 0
        r = 0
        n=len(nums)
        while r<n:
            if nums[r] not in seen:
                seen.add(nums[r])
                curr+=nums[r]                
            else:
                ans=max(curr, ans)
                while nums[l]!=nums[r]:
                    seen.remove(nums[l])
                    curr-=nums[l]
                    l+=1
                l+=1
            r+=1

        return max(ans, curr)

