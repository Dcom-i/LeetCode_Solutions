class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x=abs(dividend)
        y=abs(divisor)
        q=2**31
        if dividend==-q and divisor==-1 or dividend==q and divisor==1:
            return q-1               
        if dividend==0:
            return 0
        else:
            res=0
            while x>=y:
                r=1
                while x>y+y:
                    y+=y
                    r+=r
                res+=r
                x-=y
                y=abs(divisor)        
        if divisor<0 and dividend<0:
            return res
        if divisor<0 or dividend<0:
            return 0-(res)
        else:
            return res
