from collections import defaultdict

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        seen = defaultdict(set)
        cols = set()
        nc = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    seen[i].add(j)
            if len(seen[i])>1:
                cols.update(seen[i])
                del seen[i]
            elif len(seen[i])==1:
                val = next(iter(seen[i]))
                if val in cols:
                    cols.add(val)
                    del seen[i]
                else:
                    if val in nc:
                        cols.add(val)
                        nc.discard(val)
                        del seen[i]
                    else:
                        nc.add(val)
            
        
        return len(nc-cols)