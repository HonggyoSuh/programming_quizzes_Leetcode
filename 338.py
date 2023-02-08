from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # return [format(i, "b").count("1") for i in range(n + 1)]

        queue = [0]
        queue.extend(queue[i >> 1] + i % 2 for i in range(1, n + 1))
        return queue
