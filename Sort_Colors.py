class Solution:
    def sortColors(self, nums: List[int]) -> None:
        idx=0
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]==0:
                nums[idx],nums[left]=nums[left],nums[idx]
                idx+=1
                left+=1
            elif nums[left]==1:
                left+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
