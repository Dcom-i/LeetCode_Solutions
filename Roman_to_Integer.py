class Solution:
    def romanToInt(self, s: str) -> int:
        base = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i,j in enumerate(s):
            val = base[j]
            if i == len(s)-1:
                result += val
                break
            n_val = base[s[i+1]]
            if n_val > val:
                result -= val
            else:
                result += val
        return result
