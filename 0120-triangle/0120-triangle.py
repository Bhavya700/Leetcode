class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        a = triangle[-1]
        l=len(triangle)
        for i in range(l-2, -1, -1):
            for j in range(i+1):
                a[j] = min(a[j], a[j+1]) + triangle[i][j]
        
        return a[0]