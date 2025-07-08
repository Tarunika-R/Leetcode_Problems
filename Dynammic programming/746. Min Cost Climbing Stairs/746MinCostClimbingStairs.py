class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, current
        
        return min(prev1, prev2)
