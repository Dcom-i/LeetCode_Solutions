class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size=0
        str=""
        for t in s:
            if t in str:
                 for i in range(len(str)):
                    if str[i]==t:
                        str=str[i+1:]
                        break
            str+=t
            if len(str)>size:
                size=len(str)
        return size