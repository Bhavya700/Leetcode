class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return n

        map={}
        i,j=0,0
        ans,c=0,0
        while i<=j and j<n and i<n:
            if s[j] not in map:
                map[s[j]]=1
                j+=1
                c+=1
            else:
                ans=max(c,ans)
                while s[i]!=s[j]:
                    del map[s[i]]
                    i+=1
                    c-=1
                i+=1
                j+=1
        
        return max(ans,c)

                    




        return ans
