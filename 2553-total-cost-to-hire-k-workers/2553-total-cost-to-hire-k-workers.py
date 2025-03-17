class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_candidates = costs[:candidates]
        right_candidates = costs[-candidates:]
        left_incoming_pointer = candidates
        right_incoming_pointer = len(costs) - candidates - 1

        if left_incoming_pointer > right_incoming_pointer:
            left_candidates = costs[:-candidates]

        heapq.heapify(left_candidates)
        heapq.heapify(right_candidates)

        cost = 0

        for _ in range(k):
            if (left_candidates and right_candidates and left_candidates[0] <= right_candidates[0]) or not right_candidates:
                cost += heapq.heappop(left_candidates)
                if left_incoming_pointer <= right_incoming_pointer:
                    heapq.heappush(left_candidates, costs[left_incoming_pointer])
                    left_incoming_pointer += 1
            else:
                cost += heapq.heappop(right_candidates)
                if left_incoming_pointer <= right_incoming_pointer:
                    heapq.heappush(right_candidates, costs[right_incoming_pointer])
                    right_incoming_pointer -= 1
            
        return cost
