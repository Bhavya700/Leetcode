class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=[(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs=sorted(pairs, key=lambda p: p[1], reverse=True)

        heap=[]
        n1Sum=0
        ans=0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(heap, n1)
            if len(heap)>k:
                temp=heapq.heappop(heap)
                n1Sum-=temp
            if len(heap)==k:
                ans=max(ans, n1Sum * n2)

        return ans

