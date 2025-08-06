class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                seen.remove(nums[i])
        return next(iter(seen))