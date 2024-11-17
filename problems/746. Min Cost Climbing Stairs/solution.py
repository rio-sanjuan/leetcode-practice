class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 0:
            return 0
        elif n <= 1:
            return cost[0]

        prev_prev = cost[0]
        prev = cost[1]

        for i in range(2, n):
            current = cost[i] + min(prev, prev_prev)
            prev, prev_prev = current, prev

        return min(prev, prev_prev)
