class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for a in s:
            if a!="]":
                stack.append(a)
            else:
                temp=""
                while stack and stack[-1]!="[":
                    temp=stack.pop()+temp
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(temp*int(num))

        return "".join(stack)

                
