class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r = len(matrix)
        c = len(matrix[0])
        row,col = [0]*r,[0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row[i], col[j] = 1, 1

        for i in range(r):
            for j in range(c):
                if row[i] or col[j]:
                    matrix[i][j]=0

        return None