class Solution:

    def validPalindrome(self, s: str) -> bool:
        def func(s, l, r) -> bool:
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        n = len(s)
        if n<2:
            return True

        l = 0
        r = n-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if func(s,l,r-1) or func(s,l+1,r):
                    return True
                else:
                    return False
        
        return True
