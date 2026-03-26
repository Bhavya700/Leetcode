class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, temp, remaining):
            if remaining == 0:
                res.append(temp[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                backtrack(i, temp, remaining - candidates[i])
                temp.pop()
        backtrack(0, [], target)
        return res