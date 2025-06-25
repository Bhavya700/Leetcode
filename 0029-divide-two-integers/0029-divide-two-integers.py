class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=dividend/divisor
        if a<0:
            if a<-(2**31):
                return -2**31-1
            return math.ceil(a)
        
        else:
            if a>(2**31)-1:
                return 2**31-1
            return math.floor(a)