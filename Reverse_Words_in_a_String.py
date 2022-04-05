class Solution:
    def reverseWords(self, s: str) -> str:
        sen=""
        res = s.split()
        for i in res[::-1]:
            sen+=i+" "
        return sen[:-1]
