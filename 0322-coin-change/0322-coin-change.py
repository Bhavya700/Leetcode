class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1] * (amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==amount+1 else dp[-1]
