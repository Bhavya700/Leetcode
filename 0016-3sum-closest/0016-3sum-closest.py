class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo ,hi = i+1, n-1
            while lo < hi:
                curr = nums[i] + nums[lo] + nums[hi]
                if abs(curr-target) < abs(closest-target):
                    closest = curr

                if curr==target:
                    return curr
                elif curr<target:
                    lo += 1
                else:
                    hi -= 1
                
        return closest
        #TC: O(N^2)