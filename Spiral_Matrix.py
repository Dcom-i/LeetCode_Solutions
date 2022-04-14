class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        l = 0
        r = n
        top = 0
        bot = n 
        num = 1   
        while l < r and top < bot:
            for i in range(l, r):
                res[top][i] = num
                num+=1
            top+=1
            for i in range(top,bot):
                res[i][r-1] = num
                num+=1
            r -=1
            for i in range(r-1,l-1,-1):
                res[bot-1][i] = num
                num+=1
            bot-=1
            for i in range(bot-1,top-1,-1):
                res[i][l] = num 
                num+=1
            l+=1
        return res
