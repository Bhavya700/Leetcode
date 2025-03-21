class Solution:
    def maxArea(self, height: List[int]) -> int:
        b=0
        c=len(height)-1
        d=0
        m=max(height)
        while b<c:
            d=max((c-b)*min(height[b], height[c]), d)
            if height[b]<height[c]:
                b+=1
            else:
                c-=1
            if d >= m*(c-b):
                break

        return d
