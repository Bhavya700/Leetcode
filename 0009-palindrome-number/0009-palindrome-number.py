class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        a=str(x)
        b=a[::-1]
        if a==b:
            return True
        return False