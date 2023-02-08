class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        binary_n = format(n, "b")

        for index, i in enumerate(binary_n[::-1]):
            result += int(i) * (2 ** (31 - index))

        return result
