class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def bs(c):
            l = 0
            r = n-1
            while l<=r:
                mid = (l+r)//2
                if matrix[c][mid]==target:
                    return True
                if matrix[c][mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return False
        
        
        for i in range(m):
            if target <= matrix[i][-1]:
                return bs(i)

        return False
        
        
        