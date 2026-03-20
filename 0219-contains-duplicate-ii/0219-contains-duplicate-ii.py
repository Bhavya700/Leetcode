class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = dict()

        for i in range(len(nums)):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            else:
                map[nums[i]] = i
        
        return False
                    