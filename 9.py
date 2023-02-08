class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        copy, reverse = x, 0

        while copy > 0:
            remainder = copy % 10
            reverse = reverse * 10 + remainder
            copy = copy // 10

        if x == reverse:
            return True

        return False
