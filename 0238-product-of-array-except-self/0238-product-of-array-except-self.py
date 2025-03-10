import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        d=Counter(nums)
        r=[]
        print(d)
        if d.get(0) is None:
            p=np.prod(nums)
            for i in range(l):
                r.append(int(p//nums[i]))
            
        else:
            if d[0]==1:
                r=[0]*l
                c=nums.index(0)
                nums.remove(0)
                p=np.prod(nums)
                r[c]=int(p)

            else:
                r=[0]*l

        return r        
