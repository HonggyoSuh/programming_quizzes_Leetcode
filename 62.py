import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return int(
        #     math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1))
        # )

        dp = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]
