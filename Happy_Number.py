class Solution:
    def isHappy(self, n: int) -> bool:        
        l=[]
        while n!=1:
            el=0
            c=str(n)
            for i in c:
                el+=int(i)**2
            if el in l:
                return False
            l.append(el)
            n=el
        return True
