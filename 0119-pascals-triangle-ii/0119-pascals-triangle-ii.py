class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1, rowIndex + 1):
            prevRow = ans[-1]
            ans.append([])
            ans[-1].append(1)
            for i in range(len(prevRow) - 1):
                ans[-1].append(prevRow[i] + prevRow[i + 1])
            ans[-1].append(1)
            ans.pop(0)
        return ans[-1]
