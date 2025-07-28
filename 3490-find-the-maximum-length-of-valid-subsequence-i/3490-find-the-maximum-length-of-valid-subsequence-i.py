class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        prev=0 
        curr=1 
        l=len(nums)
        c1=1 # %2 != 0
        o=0
        e=0

        for i in range(l):
            if nums[i]%2==0:
                nums[i]=2
                e+=1
            else:
                nums[i]=1
                o+=1
        m=max(e,o)

        if m>1:
            c2=m
        else:
            c2=0

        while curr<l:
            if nums[curr]!=nums[prev]:
                c1 += 1
                prev = curr
            curr += 1
            
        print(o ,e)
        print(c2, c1)
        return max(c2, c1)

