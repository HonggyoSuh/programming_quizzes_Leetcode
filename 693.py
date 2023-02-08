class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # n = format(n, "b")
        # return all(int(n[i]) + int(n[i + 1]) == 1 for i in range(len(n) - 1))

        # n = format(n, "b")
        # return "11" not in n and "00" not in n

        return n & (n >> 1) == 0 and n | (n >> 2) == n
