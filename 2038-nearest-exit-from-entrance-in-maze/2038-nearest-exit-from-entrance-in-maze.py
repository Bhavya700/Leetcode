from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m=len(maze)
        n=len(maze[0])
        visited=set()
        step=0
        a=entrance[0]
        b=entrance[1]
        q=deque()
        q.append(entrance)
        visited.add((a,b))
        neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in neighbors:
                    row=r+dr
                    col=c+dc
                    if min(row,col)<0 or row>=m or col>=n or (row, col) in visited or maze[row][col]=="+":
                        continue
                    
                    if (row==m-1 or row==0 or col==0 or col==n-1):
                        return step+1
                    q.append([row,col])
                    visited.add((row,col))
            step+=1
        
        return -1




