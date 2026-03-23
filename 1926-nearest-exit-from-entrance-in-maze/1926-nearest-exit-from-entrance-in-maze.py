class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        l_r = len(maze)
        l_c = len(maze[0])
        x, y = entrance
        queue = deque([(x, y, 0)])
        maze[x][y] = "+"
        while queue:
            x, y, n = queue.popleft()
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                dx = x + dx
                dy = y + dy
                if 0 <= dx < l_r and 0 <= dy < l_c and maze[dx][dy] != "+":
                    if dx == 0 or dx == l_r -1 or dy == 0 or dy == l_c - 1:
                        return n + 1
                    queue.append((dx, dy, n+1))
                    maze[dx][dy] = "+"
        return -1
