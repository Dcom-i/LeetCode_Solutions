class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        f=count=0
        l=len(nums)-1
        while f<l:
            if (nums[f]+nums[l])==k:
                count+=1
                f+=1
                l-=1
            elif (nums[f]+nums[l])>k:
                l-=1
            else:
                f+=1
        return count
