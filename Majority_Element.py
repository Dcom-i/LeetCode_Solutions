class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        k=tuple(nums)
        d={}
        for i in s:
            d[i]=k.count(i)
        for k, v in d.items():
            if v==max(d.values()):
                return k
