class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort(key=lambda x: x[0])
        c=[]
        prev = i[0]
        for inter in i[1:]:
            if inter[0]<=prev[1]:
                prev[1]=max(prev[1],inter[1])
            else:
                c.append(prev)
                prev=inter
        
        c.append(prev)
        return c
                    