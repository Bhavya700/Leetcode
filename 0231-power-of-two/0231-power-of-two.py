class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False

        while True:
            if n==1:
                return True
            if (n & 1) == 1:
                return False
            n = n >>1
