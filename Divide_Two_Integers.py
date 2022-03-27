class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x=abs(dividend)
        y=divisor
        max=2**26
        r=0
        if dividend>max or dividend<-max and divisor>max or divisor<-max:
            return False
        else:                
            if dividend==0:
                return 0
            else:
                while x>=0:
                    x-=abs(y)
                    r+=1
                if divisor<0 and dividend<0:
                    return r-1
                if divisor<0 or dividend<0:
                    return 0-(r-1)
                else:
                    return r-1
 ################################################################################               
