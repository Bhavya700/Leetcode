class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        for i in range(row):
            for j in range(col):
                live = 0                # live neighbors count
                for x, y in directions: # check and count neighbors in all directions
                    if ( i + x < row and i + x >= 0 ) and ( j + y < col and j + y >=0 ) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):     # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:                  # Rule 4
                    board[i][j] = 2
        for i in range(row):
            for j in range(col):
                board[i][j] = 1 if(board[i][j] > 0) else 0
        return board
        

