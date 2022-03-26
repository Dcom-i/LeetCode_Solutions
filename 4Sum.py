class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                h=len(nums)-1
                while l<h:
                    sum=nums[i]+nums[j]+nums[l]+nums[h]
                    if sum < target:
                        l+=1
                    elif sum > target:
                        h-=1
                    else:
                        s.add((nums[i],nums[j],nums[l],nums[h]))
                        l+=1
                        h-=1
        return s
