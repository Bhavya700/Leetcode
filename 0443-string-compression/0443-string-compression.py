class Solution:
    def compress(self, c: List[str]) -> int:
        n = len(c)
        if n == 0: return 0
        w = 0
        r = 0
        while r < n:
            x = c[r]
            cnt = 0
            while r < n and c[r] == x:
                r += 1
                cnt += 1
            c[w] = x
            w += 1
            print(cnt,w,r,x)
            if cnt > 1:
                for d in str(cnt):
                    c[w] = d
                    w += 1
        return w



'''
        a=Counter(chars)
        l=len(chars)
        c=0
        d=[]
        while c<l-1:
            i=a[chars[c]]
            if i>1 and i<10:
                d.append(chr(chars[c]))
                d.append(str(i))
                c+=i
            elif i>=10 and i<100:
                d.append(chars[c])
                d.append(str(i//10))
                d.append(str(i%10))
            else:
                d.append(chars[c])
                c+=1
        
        return d


            elif i>=100 and i<1000:
                d.append(chars[c])
                d.append(str(i//100))
                i=i%100
                d.append(str(i//10))
                d.append(str(i%10))
            elif i>=1000:
                d.append(chars[c])
                d.append(str(i//1000))
                i=i%1000
                d.append(str(i//100))
                i=i%100
                d.append(str(i//10))
                d.append(str(i%10))

'''