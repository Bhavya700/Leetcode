class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a=set(nums)
        count = 0
        for i in a:
            if i-1 not in a:
                c=1
                while i+c in a:
                    c+=1
                count=max(count,c)
        return count


