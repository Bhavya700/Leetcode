class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)        
        max_heap = [(-freq, char) for char, freq in c.items()]
        heapq.heapify(max_heap)

        res = ""
        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res+=char

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            freq += 1
            prev_freq, prev_char = freq, char

        if len(res) != len(s):
            return ""
        return res