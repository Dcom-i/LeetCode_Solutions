class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        arr=sorted(nums)
        if len(arr)==2: return arr[1]-arr[0]
        if len(arr)<2:return 0
        else:
            m=[]
            for i in range(len(arr)-1):
                s=arr[i+1]-arr[i]
                m.append(s)
            return max(m)
        
        # second option #####
        # arr=sorted(nums)
        # n=0
        # for i in range(len(arr)-1):
        #     n=max(n,arr[i+1]-arr[i])
        # return n
        
        # third option #####
        # for i in range(len(arr)-1):
        #     if arr[i+1]-arr[i]>n:
        #         n=arr[i+1]-arr[i]
        # return n
