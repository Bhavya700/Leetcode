class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS=len(board)
        COLS=len(board[0])

        def dfs(i, j,):
            if i<0 or j<0 or i>=ROWS or j >=COLS or board[i][j]!='O':
                return 
            board[i][j] = 'T'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(ROWS):
            dfs(i, 0)      # left border
            dfs(i, COLS-1) # right border
        
        for j in range(COLS):
            dfs(0, j)      # top border
            dfs(ROWS-1, j) # bottom border
        
        # STEP 2: Flip remaining O's to X (these are surrounded)
        # Restore safe ones back to O
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # surrounded
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # safe, restore

        

