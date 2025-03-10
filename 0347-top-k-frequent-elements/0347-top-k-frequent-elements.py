import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = Counter(nums)
        if len(nums)==len(r):
            return nums
        heap=[-x for x in r.values()]
        heapq.heapify(heap)
        b=[-heapq.heappop(heap) for _ in range(k)]
        keys = [k for k, v in r.items() if v in b]
        return keys
        