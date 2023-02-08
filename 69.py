class Solution:
    def mySqrt(self, x: int) -> int:
        # if not x:
        #     return 0
        # if x == 1:
        #     return 1

        # for i in range(x):
        #     exp = i**2
        #     if exp == x:
        #         return i
        #     elif exp > x:
        #         return i - 1

        # return i

        if x == x**2:
            return x

        left, right = 1, x

        while left < right:
            mid = (left + right) // 2
            sqr = mid**2

            if x == sqr:
                return mid

            if x >= sqr:
                left = mid + 1
            else:
                right = mid

        return left - 1
