class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }  
        for el in range(len(s)-1):
            if d[s[el]]<d[s[el+1]]:
                res-=d[s[el]]
            else:
                res+=d[s[el]]
        res+=d[s[-1]]
        return res


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         base = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         result = 0
#         for i,j in enumerate(s):
#             val = base[j]
#             if i == len(s)-1:
#                 result += val
#                 break
#             n_val = base[s[i+1]]
#             if n_val > val:
#                 result -= val
#             else:
#                 result += val
#         return result
