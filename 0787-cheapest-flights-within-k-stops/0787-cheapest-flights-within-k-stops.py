class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, c in flights:
            adj[a].append((b, c))
        
        cost = [float('inf')]*n
        cost[src] = 0

        queue = collections.deque([(0, src, 0)]) 
        
        while queue:
            stops, node, curr = queue.popleft()
            if stops > k: 
                continue
            
            for v, w in adj[node]:
                if curr + w < cost[v]:
                    cost[v] = curr + w
                    queue.append((stops + 1, v, cost[v]))
                    
        return cost[dst] if cost[dst] != float('inf') else -1
