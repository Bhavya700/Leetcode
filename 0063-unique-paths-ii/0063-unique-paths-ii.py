class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dp[j] = 0
                else:
                    if j>0:
                        dp[j] += dp[j-1]
        
        return dp[-1]