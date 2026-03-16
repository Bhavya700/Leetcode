class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tg = sum(gas)
        tc = sum(cost)
        if tc>tg:
            return -1
        ans = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total<0:
                total = 0
                ans = i+1
        return ans
