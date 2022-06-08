class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str, p = s.split(), pattern
        d={}
        if len(p)!=len(str) or len(set(p))!=len(set(str)): return False
        for i in range(len(str)):
            if p[i] not in d:
                d[p[i]]=str[i]
            else:
                if d[p[i]]!=str[i]:
                    return False
        return True
