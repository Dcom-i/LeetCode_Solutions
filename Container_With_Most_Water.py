class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr=height
        j=len(arr)-1
        i,res,r=0,0,0
        while (i<j):
            if arr[i]<arr[j]:
               r=arr[i]*(j-i)
            else:
                r=arr[j]*(j-i)
            res=max(res,r)
            if arr[i]>arr[j]:
                j-=1
            else:
                i+=1
        return res
