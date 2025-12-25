class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        pair=Counter(nums)
        ans=[]
        a=sum(pair.keys())
        n=len(nums)
        b=(n * (n + 1)) // 2
        ans.append(pair.most_common(1)[0][0])
        ans.append(b-a)
        return ans
            

        

            