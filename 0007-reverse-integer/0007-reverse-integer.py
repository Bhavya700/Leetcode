class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            s=1
        else:
            s=-1
        x=abs(x)
        reverse_str=str(x)[::-1]
        final_val=int(reverse_str)*s
        if final_val <= -2**31 or final_val >= 2**31-1:
            return 0
        return final_val
