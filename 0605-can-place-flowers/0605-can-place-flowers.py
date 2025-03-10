class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        c=0
        for i in range(l):
            if flowerbed[i]==0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == l - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    c += 1
            if c >= n:
                return True
        
        if c>=n:
            return True
        else:
            return False

