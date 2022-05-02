class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s1,s2=[],[]
        if len(nums)==1: return nums
        for n in nums:
            if n%2==0: s1.append(n)
        for n in nums:
            if n%2!=0: s2.append(n)
        return s1 + s2
