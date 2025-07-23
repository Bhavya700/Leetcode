class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        first, second = ('a', 'b') if x >= y else ('b', 'a')
        high, low = (x, y) if x >= y else (y, x)

        
        stack = []
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                res += high
            else:
                stack.append(ch)

 
        final = []
        for ch in stack:
            if final and final[-1] == second and ch == first:
                final.pop()
                res += low
            else:
                final.append(ch)

        return res