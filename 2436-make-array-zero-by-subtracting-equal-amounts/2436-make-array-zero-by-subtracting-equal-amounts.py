class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums=list(set(nums))
        heapq.heapify(nums)
        c=0
        val = heapq.heappop(nums)
        if val!= 0:
            heapq.heappush(nums,val)
        if len(nums)==0:
            return c
        s=sum(nums)
        while len(nums)!=0:
            val = heapq.heappop(nums)
            s-=val
            c+=1
        return c




