class Solution:
    def integerReplacement(self, n: int) -> int:
        c=0
        while n!=1:
            if n < 4:
                return c+(n-1)
            if n%2==0: 
                n//=2
            else:
                if n % 4 == 3:
                    n += 1
                else:
                    n -= 1
               
            c+=1
        return c
