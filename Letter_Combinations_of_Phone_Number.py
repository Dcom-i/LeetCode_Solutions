class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2" : "abc", 
            "3" : "def", 
            "4" : "ghi", 
            "5" : "jkl", 
            "6" : "mno", 
            "7" : "pqrs", 
            "8" : "tuv", 
            "9" : "wxyz",   
        }
        comb=[]
        for i in range(len(digits)):
            if digits[i] in dic:
                dic[digits[i]]
                symb=dic[digits[i]]
                n=len(comb)
                for j in symb:
                    if n>0:
                        for k in range(0,n):
                            comb.append(comb[k]+j)
                    else:
                        comb.append(j)
                comb=comb[n:]
        return comb
