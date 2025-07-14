class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        a=""
        p=True
        while i<n:
            if s[i]=='-' or s[i]=='+':
                if a:
                    break
                else:
                    a+='0'
                    if s[i]=='-':
                        p=False
            elif s[i].isdigit():
                a+=s[i]
            elif s[i].isalpha() or s[i]=='.':
                break
            elif s[i]==' ':
                if a:
                    break
            i+=1

        if not a:
            return 0
        a=int(a)
        if not p:
            a=a*-1
            if a<-1*(2**31):
                return (-2)**31
        if a>(2**31)-1:
            return (2**31)-1
        return a