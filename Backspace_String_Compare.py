class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1,t1 = [],[]
        for c in s:
            if c=='#' and s1:
                s1.pop()
            elif c!='#':
                s1.append(c)
        for c in t:
            if c=='#' and t1:
                t1.pop()
            elif c!='#':
                t1.append(c)
        return s1==t1
