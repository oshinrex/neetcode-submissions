class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # array cost, cost[i]: cost fo taking a step from ith floor of a staircase
        # after paying the cost, can step to either (i+1)th
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])