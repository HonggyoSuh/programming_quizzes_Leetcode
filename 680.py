class Solution:
    # def check(self, s: str, left: int, right: int, flag: bool) -> bool:
    #     while left <= right:
    #         if s[left] != s[right]:
    #             if flag:
    #                 return False
    #             else:
    #                 return self.check(s, left + 1, right, True) or self.check(
    #                     s, left, right - 1, True
    #                 )
    #         left += 1
    #         right -= 1

    #     return True

    def validPalindrome(self, s: str) -> bool:
        # return self.check(s, 0, len(s) - 1, False)

        reverse = s[::-1]

        if s == reverse:
            return True

        for index, i in enumerate(s):
            if i != reverse[index]:
                s_front = s[:index] + s[index + 1 :]
                s_end = reverse[:index] + reverse[index + 1 :]

                return s_front == s_front[::-1] or s_end == s_end[::-1]

        return True
