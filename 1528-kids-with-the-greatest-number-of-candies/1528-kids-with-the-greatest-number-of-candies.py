class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        m=max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                a.append(True)
            else:
                a.append(False)
        
        return a