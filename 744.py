from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for i in letters:
        #     if ord(target) < ord(i):
        #         return i

        # return letters[0]

        # i = bisect.bisect(letters, target)
        # return letters[i % len(letters)]

        left, right = 0, len(letters) - 1
        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[left] if letters[left] > target else letters[0]

        # for i in range(1, 26):
        #     char = chr(ord(target) + i)

        #     if char in letters:
        #         return char
        # return letters[0]
