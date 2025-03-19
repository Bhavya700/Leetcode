class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        a=prices[0]
        for i in prices:
            if i<a:
                a=min(a,i)
            profit=i - a
            if profit>ans:
                ans=max(ans, profit)
        
        return ans
            