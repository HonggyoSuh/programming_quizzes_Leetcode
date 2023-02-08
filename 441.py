class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1

        while n > 0:
            n -= count

            if n < count:
                return count if n >= 0 else count - 1

            count += 1

        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            sum_upto = int((mid * (mid + 1)) / 2)

            if sum_upto == n:
                return mid
            elif sum_upto < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
