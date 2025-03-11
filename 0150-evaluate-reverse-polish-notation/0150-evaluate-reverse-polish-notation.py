class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for t in tokens:
            if t.isdigit() or (t.startswith('-') and t[1:].isdigit()):
                a.append(int(t))
            else:
                if len(a)>=2:
                    b=int(a.pop())
                    c=int(a.pop())
                    if t=="+":
                        a.append(c+b)
                    elif t=="*":
                        a.append(c*b)
                    elif t=="-":
                        a.append(c-b)
                    elif t=="/":
                        a.append(c/b)

        if len(a)==1:
            return int(a[0])