class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l=len(s)
        a = 0 
        for i in range(l):
            if s[i]=='0':
                a=len(set(s[i:]))
                break
        if a>1:
            return False
        return True