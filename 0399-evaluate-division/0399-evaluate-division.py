class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0/value
            
        def dfs(start, end, visited):
            if start not in graph or end not in graph: return -1.0
            if start == end: return 1.0
            
            visited.add(start)
            for neighbour in graph[start]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    intermediate_result = dfs(neighbour, end, visited)
                    if intermediate_result != -1.0:
                        return intermediate_result * graph[start][neighbour]
            return -1.0
            
        result = []
        
        for dividend, divisor in queries:
            result.append(dfs(dividend, divisor, set()))
        
        return result