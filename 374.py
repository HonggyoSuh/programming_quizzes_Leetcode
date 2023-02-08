# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n

        while left != right:
            mid = (left + right) // 2
            # check = guess(mid)

        #     if check == 1:
        #         if left == mid:
        #             left += 1
        #         else:
        #             left = mid
        #     elif check == -1:
        #         if right == mid:
        #             right -= 1
        #         else:
        #             right = mid
        #     else:
        #         return mid

        # return left
