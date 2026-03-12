from collections import defaultdict
from typing import List

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
        print(seen)

        for a in list(seen.keys()):
            if not seen[a]:  
                continue
            val = next(iter(seen[a])) 
            if val not in cols and val not in nc:
                nc.add(val)
            else:
                cols.add(val)
                nc.discard(val)

        print(cols)
        print(nc)
        return len(nc)


