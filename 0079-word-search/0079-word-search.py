class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ROW=len(board)
        # COL=len(board[0])
        # visit=set()
        # def dfs(r, c, i):
        #     nonlocal ROW, COL, visit
        #     if i==len(word):
        #         return True
        #     if (r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visit or board[r][c]!=word[i]):
        #         return False

        #     visit.add((r,c))
        #     ans = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        #     visit.remove((r,c))
        #     return ans
        
        # for r in range(ROW):
        #     for c in range(COL):
        #         if dfs(r,c,0):
        #             return True
        
        # return False
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (not (0 <= r < ROWS) or not (0 <= c < COLS) or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            temp = board[r][c]
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = temp

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
        
