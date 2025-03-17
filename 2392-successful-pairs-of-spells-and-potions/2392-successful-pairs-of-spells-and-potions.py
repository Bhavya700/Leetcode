class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        maxPot = max(potions)
        minPot = min(potions)
        n = (maxPot-minPot+1)

        counts = [0]*n
        for pot in potions:
            counts[pot-minPot] += 1

        prev = 0
        for i in range(len(counts)-1,-1,-1):
            if counts[i] == 0:
                counts[i] = prev
                continue
            counts[i] = counts[i] + prev
            prev = counts[i]

        ans = []
        for spell in spells:
            minSuccess = ceil(success/spell)            
            if (minSuccess-minPot) >= n: 
                ans.append(0)
            elif minSuccess < minPot:
                ans.append(counts[0])
            else:
                ans.append(counts[minSuccess - minPot])

        return ans