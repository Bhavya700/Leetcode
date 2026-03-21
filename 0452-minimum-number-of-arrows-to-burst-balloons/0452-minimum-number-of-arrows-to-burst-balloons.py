class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ans=len(points)
        prev = points[0]
        for curr in points[1:]:
            if curr[0]<=prev[1]:
                ans -=1
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                prev = curr
        
        return ans