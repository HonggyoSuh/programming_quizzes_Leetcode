class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return int(num**0.5) == num**0.5

        # return not "." in str(num**0.5)[:-2]

        # root = (num + 1) // 2
        # while root**2 > num:
        #     root = (root + num / root) // 2
        # return root**2 == num

        if num == 1:
            return True

        left, right = 1, num

        while left < right:
            mid = (left + right) // 2
            sqr = mid * mid

            if sqr == num:
                return True

            if sqr < num:
                left = mid + 1
            else:
                right = mid

        return False
