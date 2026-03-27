class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bisectleft(arr, x):
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        return bisectleft(nums, target)
        