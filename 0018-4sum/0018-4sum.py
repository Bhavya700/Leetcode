class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            #print("i=",i)
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[n-3]+nums[n-2]+nums[n-1]<target:
                continue
            for j in range(i+1,n-2):
                #print("j=",j)
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                if nums[i]+nums[j]+nums[n-2]+nums[n-1]<target:
                    continue
                val=target-nums[i]-nums[j]
                left=j+1
                right=n-1
                while left<right:
                    nl=nums[left]
                    nr=nums[right]
                    sum = nl+nr
                    if sum==val:
                        out.append([nums[i],nums[j],nl,nr])
                        left += 1
                        right -= 1
                        while left<right and nums[left]==nl:
                            left += 1
                        while left<right and nums[right]==nr:
                            right -= 1
                    elif sum<val:
                        left += 1
                    else:
                        right -= 1
        return out
