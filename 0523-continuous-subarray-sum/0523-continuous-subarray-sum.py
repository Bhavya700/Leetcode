class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        t = 0
        hashmap = {0: -1}    
        for i, a in enumerate(nums):
            t += a
            r = t%k
            if r not in hashmap:
                hashmap[r]=i
            elif i-hashmap[r]>1:
                return True
        return False 
