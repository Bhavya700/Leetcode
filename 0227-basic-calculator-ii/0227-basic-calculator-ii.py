class Solution:
    def calculate(self, s: str) -> int:
        res, cur, prev, op = 0, 0, 0, '+'

        for c in s + '+':
            if c == ' ': continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if op in '*/':
                    prev = prev * cur if op == '*' else int(prev / cur)
                else: 
                    res += prev
                    prev = cur if op == '+' else -cur
                op = c
                cur = 0
        
        return res + prev