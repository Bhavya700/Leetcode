class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys={
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
        }

        if len(digits)==0:
            return []

        ans=[]
        
        for a in digits:
            temp=[]
            if not ans:
                ans+=keys[int(a)]
                continue
            else:
                for i in ans:
                    for c in keys[int(a)]:
                        temp.append(i+c)
                ans=temp
            del temp
        return ans
        