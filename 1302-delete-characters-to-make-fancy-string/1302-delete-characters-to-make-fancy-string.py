class Solution:
    def makeFancyString(self, s: str) -> str:
        last=""
        c=0
        word=""
        for i in s:
            if i!=last:
                last=i
                c=1
                word+=i
            else:
                if c<2:
                    word+=i
                c+=1
        return word
                

                    
