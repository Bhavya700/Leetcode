class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        time=0
        fresh=0
        q=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])
        neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in neighbours:
                    row=dr+r
                    col=dc+c
                    if (min(row,col)<0 or row==ROWS or col==COLS or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        
        if fresh>0:
            return -1
        return time 







