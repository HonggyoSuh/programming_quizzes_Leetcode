import math


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        result = 0

        for i in range((n // 2) + 1):
            result += int(
                math.factorial(n - i) / (math.factorial(n - i * 2) * math.factorial(i))
            )

        return result
