class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        n=len(candidates)
        def backtrack(i, sum):
            if sum==target:
                ans.append(curr[:])
                return
            if sum>target or i==n:
                return 
            backtrack(i+1, sum)
            curr.append(candidates[i])
            backtrack(i, sum+candidates[i])
            curr.pop()

        backtrack(0, 0)
        return ans


