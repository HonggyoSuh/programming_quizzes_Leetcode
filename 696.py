class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # prev, curr = 0, 1
        # counter = 0

        # for index in range(1, len(s)):
        #     if s[index] == s[index - 1]:
        #         curr += 1
        #     else:
        #         counter += min(prev, curr)
        #         prev = curr
        #         curr = 1

        # counter += min(prev, curr)
        # return counter

        s = s.replace("01", "0 1")
        s = s.replace("10", "1 0")
        result = 0
        length = list(map(len, s.split()))

        for i, j in zip(length, length[1:]):
            result += min(i, j)

        return result
