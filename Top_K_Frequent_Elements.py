class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        p=[]
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        p = sorted(s, key=lambda x:s[x], reverse=True)
        return p[:k]
