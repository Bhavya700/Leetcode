class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        a=[]
        for z in range(r*c):
            a.append(matrix[y][x])
            matrix[y][x]="*"
            if not 0 <= x + dx < c or not 0 <= y + dy < r or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx
            x += dx
            y += dy
    
        return a
