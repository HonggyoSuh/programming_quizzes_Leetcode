from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_vowels = deque()
        result = ""
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        for i in s:
            if i in vowels:
                s_vowels.append(i)

        for i in s:
            if i in vowels:
                result += s_vowels.pop()
            else:
                result += i

        return result

        # s = list(s)
        # vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        # left, right = 0, len(s) - 1

        # while left < right:
        #     if s[left] not in vowels:
        #         left += 1
        #     if s[right] not in vowels:
        #         right -= 1
        #     if s[left] in vowels and s[right] in vowels:
        #         s[left], s[right] = s[right], s[left]
        #         left += 1
        #         right -= 1

        # return "".join(s)
