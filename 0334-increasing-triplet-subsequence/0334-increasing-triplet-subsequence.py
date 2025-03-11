from collections import defaultdict
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False



        '''l=len(nums)
        d=[]
        d.append([nums[0]])
        c=1
        for i in range(1,l):
            j=0
            while j<c:
                if nums[i]>d[j][-1]:
                    d[j].append(nums[i])
                    if len(d[j])==3:
                        return True
                    break
                elif nums[i]<d[j][-1]:
                    if nums[i]<d[j][0] and j==c:
                        d.append([nums(i)])
                        c+=1
                        break
                    else:
                        d.append([nums[i],d[j][0]])
                        break
                
        print(d)
        return False'''
        
