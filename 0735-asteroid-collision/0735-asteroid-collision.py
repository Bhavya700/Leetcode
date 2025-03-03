class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        stack=[]
        n=len(asteroids)
        for i in range(n):
            temp=asteroids[i]
            d=temp>0
            if d==True:
                stack.append(temp)
            else:
                if not stack:
                    ans.append(temp)
                else:
                    while True:
                        if not stack:
                            ans.append(temp)
                            break
                        a=stack.pop()
                        if abs(a)>abs(temp):
                            stack.append(a)
                            break
                        elif abs(a)==abs(temp):
                            break
                        else:
                            continue
        
        ans+=stack
        return ans
