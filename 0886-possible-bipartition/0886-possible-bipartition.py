class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        group = {i:None for i in range(1, n+1)}

        def dfs(node, g):
            if not group[node]:
                group[node]=g
            else: 
                return group[node]==g
            
            for a in adj[node]:
                if not dfs(a, 2 if g==1 else 1):
                    return False
            return True

        for i in range(1, n+1):
            if not group[i] and not dfs(i, 1):
                return False
        
        return True
            


