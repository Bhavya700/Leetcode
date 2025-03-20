class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        a=2
        b=3
        c=4
        while c<=n:
            temp=b
            b+=a
            a=temp
            c+=1

        return b
