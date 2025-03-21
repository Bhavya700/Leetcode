class Solution:
    def firstUniqChar(self, s: str) -> int:
        m=Counter(s)
        for i in m.keys():
            if m[i]==1:
                return s.index(i)
        return -1
