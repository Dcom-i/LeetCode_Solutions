class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=[]
        n2=[]
        s1=0
        s2=0
        for i in range(len(num1)):
            n1.append(ord(num1[i])-48)            
        for i in range(len(num2)):
            n2.append(ord(num2[i])-48)
        for i,v in enumerate(n1):
            s1+=v*10**((len(n1)-1)-i)
        for i,v in enumerate(n2):
            s2+=v*10**((len(n2)-1)-i)    
        return "{}".format(s1*s2)
