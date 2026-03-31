class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0], -x[1]))

        def lis(nums):
            subs = [nums[0]]
            for i in range(len(nums)):
                num = nums[i]
                if num > subs[-1]:
                    subs.append(num)
                else:
                    j = bisect_left(subs, num)
                    subs[j] = num
            return len(subs)
        return lis([x[1] for x in envelopes])