class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr, res=[],""
        for i in range(len(s)):
            if arr and arr[-1][0]==s[i]:
                arr[-1][1]+=1
            else:
                arr.append([s[i],1])
            if arr[-1][1]==k:
                arr.pop()    
        for c, num in arr:
            res+=(c*num)
        return res
