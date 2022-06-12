class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        arr=sorted(nums)
        n=0
        for i in range(len(arr)-1):
            n=max(n,arr[i+1]-arr[i])
        return n
        
        # second option #####
        # for i in range(len(arr)-1):
        #     if arr[i+1]-arr[i]>n:
        #         n=arr[i+1]-arr[i]
        # return n
