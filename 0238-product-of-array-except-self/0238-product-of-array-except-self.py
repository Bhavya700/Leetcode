class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1: return [0 for i in nums]
        prod: int = 1
        altProd: int = 1
        for i in nums:
            prod *= i
            if i: altProd *= i
        return [(prod//i if i != 0 else altProd) for i in nums]