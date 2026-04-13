class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
             cost[i] += min(cost[i+1], cost[i+2])

        # we can do this because we are given that in the problem statement
        # that we will get at least two values 
        return min(cost[0], cost[1])