class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        rows=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            curr=[1]
            for j in range(1,i):
                curr.append(rows[i-1][j-1]+rows[i-1][j])
            curr.append(1)
            rows.append(curr)
        return rows[rowIndex]