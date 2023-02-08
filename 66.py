from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = ""
        # for i in digits:
        #     num += str(i)
        # num = int(num) + 1
        # return list(map(int, str(num)))

        return map(int, str(int("".join(str(i) for i in digits)) + 1))
