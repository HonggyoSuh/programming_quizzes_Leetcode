class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary_n = format(n, "b")
        if binary_n[0] == "1" and binary_n.count("1") == 1:
            return True

        return False

        # return n > 0 and n & (n - 1) == 0
