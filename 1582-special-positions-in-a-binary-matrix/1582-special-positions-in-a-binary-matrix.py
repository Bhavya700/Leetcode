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
                        del seen[i]
        
        return len(nc-cols)



        # res = 0
        # m, n = len(mat), len(mat[0])
        # row_sums = [sum(row) for row in mat]
        # col_sums = [sum(row[i] for row in mat) for i in range(n)]
        # for i in range(m):
        #     if row_sums[i] > 1 or row_sums[i] == 0:
        #         # we don't need to iterate over full matrix
        #         # only need to consider valid rows/cols
        #         continue  
        #     for j in range(n):
        #         if col_sums[j] > 1 or col_sums[j] == 0:
        #             continue
        #         is_special = (row_sums[i] + col_sums[j] - mat[i][j]) == 1 and mat[i][j] == 1
        #         if is_special:
        #             res += 1
        # return res


