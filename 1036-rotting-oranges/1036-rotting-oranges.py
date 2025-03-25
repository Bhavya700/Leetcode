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
                    q.append((r,c))
        if fresh == 0:
            return 0

        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in neighbours:
                    row=dr+r
                    col=dc+c
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1 
