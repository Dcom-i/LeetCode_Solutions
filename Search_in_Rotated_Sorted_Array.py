class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i                 
        except:
            return -1
        return -1
