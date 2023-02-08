import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = collections.Counter(moves)
        return counter["L"] == counter["R"] and counter["U"] == counter["D"]
