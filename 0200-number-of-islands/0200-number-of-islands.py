from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        def dfs(i, j):
            if i<0 or j<0 or i>=ROWS or j >=COLS or grid[i][j]!='1':
                return
            else:
                grid[i][j]='0'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        ans=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        
        return ans