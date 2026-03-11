class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bn = bin(n)[2:]
        l = len(bn)
        ans=0
        for i in range(-1, -l-1, -1):
            if bn[i]=='0':
                ans+=2**((-1*i)-1)
        return ans