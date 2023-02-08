class Solution:
    def binaryGap(self, n: int) -> int:
        # bin_n = format(n, "b")
        # pointer_1 = pointer_2 = distance = 0

        # for index, i in enumerate(bin_n, 1):
        #     if i == "1":
        #         if pointer_1 == 0:
        #             pointer_1 = index
        #         else:
        #             pointer_2 = index
        #             distance = max((pointer_2 - pointer_1), distance)
        #             pointer_1 = pointer_2

        # return distance

        last = None
        ans = 0
        for i in range(31):
            if (n >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans
