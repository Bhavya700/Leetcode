class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        curr = numbers[left] + numbers[right]

        while curr != target:
            if curr > target:
                right -= 1
            else:
                left += 1
            curr = numbers[left] + numbers[right]
            
        return [left+1, right +1]

