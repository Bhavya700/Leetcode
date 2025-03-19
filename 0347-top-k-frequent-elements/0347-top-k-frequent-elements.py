import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freqs = [(freq, num) for num, freq in counts.items()]
        heap = []
        
        for freq in freqs:
            heapq.heappush(heap, freq)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]