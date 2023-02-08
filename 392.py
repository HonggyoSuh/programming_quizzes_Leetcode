class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j  = 0, 0

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1

        # return i == len(s)

        sequence = t

        for char in s:
            print(sequence)
            index = sequence.find(char)

            if index == -1:
                return False
            else:
                sequence = sequence[index + 1 :]

        return True
