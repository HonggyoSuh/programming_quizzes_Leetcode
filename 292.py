class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4

        # dp = [True for _ in range(n)]

        # for i in range(3, n):
        #     dp[i] = not dp[i - 1] or not dp[i - 2] or not dp[i - 3]

        # return dp[-1]
