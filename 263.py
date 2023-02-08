class Solution:
    def isUgly(self, n: int) -> bool:
        # for p in 2, 3, 5:
        #     while n % p == 0 < n:
        #         n /= p
        # return n == 1

        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1
