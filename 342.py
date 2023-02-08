class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 4 == 0:
            n /= 4
        return n == 1

        # if n < 1:
        #     return False

        # n = format(n, "b")
        # if n.count("1") == 1 and len(n) % 2 == 1:
        #     return True

        # return False

        # return n > 0 and not(n & (n - 1)) and n & 1431655765 == n

        # return n > 0 and not(n & (n-1)) and int(sqrt(n)) * int(sqrt(n)) == n

        # return n > 0 and log(n, 4).is_integer()
