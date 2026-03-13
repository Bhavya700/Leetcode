class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = dict()
        x = sorted(nums, reverse=True)
        last = x[0]
        l=len(nums)
        for i, num in enumerate(x):
            if num == last:
                continue
            else:
                result[last] = l - i
                last = num

        return [result.get(num, 0) for num in nums]
        # return [sorted(nums).index(num) for num in nums]