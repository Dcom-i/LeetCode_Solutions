class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # for i in range(len(cost)-3,-1,-1):
        #     cost[i]+=min(cost[i+1],cost[i+2])
        # return min(cost[0],cost[1])
        
        for i in range(2,len(cost)):
            temp=cost[i]+min(cost[0],cost[1])
            cost[0]=cost[1]
            cost[1]=temp
        return min(cost[0],cost[1])
