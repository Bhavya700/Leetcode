class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u=max(piles)
        if len(piles)==h:
            return u
        l=1
        ans=u
        while l<=u:
            k=math.floor((l+u)/2)
            # print(k)
            total=0
            for a in piles:
                total+=math.ceil(a/k)
            # print(total)
            if total<=h:
                ans=min(ans,k)
                u=k-1
                continue
            else:
                l=k+1

        return ans
         