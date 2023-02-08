from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0 for _ in range(length)]
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, length):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])
