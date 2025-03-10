class Solution:
    def reverseVowels(self, s: str) -> str:
        a=set('AaEeIiOoUu')
        d=list(s)
        l=0
        r=len(s)-1
        while l<r:
            while s[l] not in a and l<r:
                l+=1
            while s[r] not in a and l<r:
                r-=1
            d[l],d[r]=d[r],d[l]
            l+=1
            r-=1

        return ''.join(d)

            


                

