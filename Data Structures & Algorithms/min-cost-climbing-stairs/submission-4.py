class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: 
            return min(cost)
        
        cost = cost + [0]
        one = cost[0]
        two = cost[1]

        for i in range(2, len(cost)):
            temp = two  
            two = cost[i] + min(one, two)
            one = temp 

        return two