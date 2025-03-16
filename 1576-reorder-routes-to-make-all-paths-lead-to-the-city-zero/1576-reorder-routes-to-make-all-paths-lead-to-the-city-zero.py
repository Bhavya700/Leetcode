class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj={(a,b) for a, b in connections}
        neighbors={city:[] for city in range(n)}
        ans=0
        visit=set()
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal adj, neighbors, visit, ans
            for x in neighbors[city]:
                if x in visit:
                    continue
                if (x, city) not in adj:
                    ans+=1
                visit.add(x)
                dfs(x)
        
        visit.add(0)
        dfs(0)
        return ans

