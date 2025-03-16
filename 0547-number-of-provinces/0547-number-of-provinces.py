class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visit.add(i)
            for j in range(n):
                if j not in visit and isConnected[i][j]==1:
                    dfs(j)

        visit=set()
        n=len(isConnected)
        b=0
        for i in range(n):
            if i not in visit:
                dfs(i)
                b+=1

        return b

