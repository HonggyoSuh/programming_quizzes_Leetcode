from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int, str(int("".join(map(str, num))) + k)))

        # number = 0

        # for index, i in enumerate(reversed(num)):
        #     number += i * (10 ** index)

        # return [int(i) for i in str(number + k)]
