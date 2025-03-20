class Solution:
    def longestPalindrome(self, s: str) -> str:
        si,ml=0,0
        for i in range(len(s)+1):
            if i-ml>=0:
                tmpstr = s[i-ml:i]
                if tmpstr == tmpstr[::-1]:
                    si = i-ml
                    ml += 1
            if i-ml-1>=0:
                tmpstr = s[i-ml-1:i]
                if tmpstr == tmpstr[::-1]:
                    si = i-ml-1
                    ml += 2
        return s[si:si+ml-1]
