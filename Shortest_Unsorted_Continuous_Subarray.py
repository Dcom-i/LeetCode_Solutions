class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nsrt=sorted(nums)
        res=[]
        if len(nums)<=1:
            return 0
        elif (nsrt==nums):
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]!=nsrt[i]:
                    res.append(i)
            return max(res)-min(res)+1
