import itertools
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        return self.char_shortest_distancer(s, c)

    def char_shortest_distancer(self, string, char):
        length = len(string)
        result = [length for _ in range(length)]
        prev_char = -length

        for i in itertools.chain(range(length), reversed(range(length))):
            if string[i] == char:
                prev_char = i
            result[i] = min(result[i], abs(i - prev_char))

        return result
