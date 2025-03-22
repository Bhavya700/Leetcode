class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a=0
        b=1
        c=2
        while c<=n:
            temp=b
            b+=a
            a=temp
            c+=1
        return b
            
