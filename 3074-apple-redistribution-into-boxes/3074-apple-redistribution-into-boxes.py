class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        capacity.sort(reverse=True)
        ans=0
        i=0
        while s>0 and i<len(capacity):
            # print(s, ans)
            s=s-capacity[i]
            i+=1
            ans+=1
        return ans