class Solution:
    def isPalindrome(self, s: str) -> bool:
        #     temp = ""

        #     for i in s.lower():
        #         if i.isalpha() or self.isInteger(i):
        #             temp += i

        #     left, right = 0, len(temp) - 1

        #     while left <= right:
        #         if temp[left] != temp[right]:
        #             return False

        #         left += 1
        #         right -= 1

        #     return True

        # def isInteger(self, i: str) -> bool:
        #     try:
        #         i = int(i)
        #     except ValueError:
        #         return False
        #     else:
        #         return True

        #     import string
        #     s = s.translate(str.maketrans('', '', string.punctuation)).replace(' ','').lower()
        #     return s == s[::-1]

        s = "".join(e for e in s if e.isalnum()).lower()

        return s == s[::-1]
