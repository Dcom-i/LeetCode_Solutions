class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        big=max(nums)
        sm=min(nums)
        l=[]
        for i in range(sm,big+1): l.append(i)
        res = list(set(nums)^set(l))
        if res==[] and sm==0:
            return big+1
        elif res==[] and sm>0:
            return sm-1
        else:
            return res[0]
