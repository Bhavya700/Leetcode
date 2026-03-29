import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        nums = sorted(zip(capital, profits))
        i = 0
        l = len(nums)
        
        for _ in range(k):
            while i < l and nums[i][0] <= w:
                heapq.heappush(maxProfit, -nums[i][1])
                i += 1
            
            if not maxProfit:
                break
            w+=(-1*heapq.heappop(maxProfit))
        
        return w