class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        n = len(citations)
        for i, c in enumerate(citations):
            if c>0:
                if n-i>=c:
                    ans = max(ans, c)
                elif n-i>ans:
                    ans = max(ans, n-i)
        return ans

            