class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        n = len(s)
        for a in range(n-1):
            if value[s[a]] < value[s[a+1]]:
                ans -= value[s[a]]
            else:
                ans += value[s[a]]
        
        return ans + value[s[-1]]

