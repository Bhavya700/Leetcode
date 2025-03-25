class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        ans = 0
        total = 0
        for n in nums:
            total+=n
            if total - k in seen:
                ans += seen[total-k]
            seen[total] = 1 + seen.get(total, 0)

        return ans
