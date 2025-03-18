class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        i=3
        if n<i:
            return a[n]
        while i<=n:
            t1=a[1]
            t2=a[2]
            a[2]=a[0]+a[1]+t2
            a[1]=t2
            a[0]=t1
            i+=1

        return a[2]