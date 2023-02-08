from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        copy = mat

        while True:
            copy = [list(i) for i in zip(*copy[::-1])]

            if copy == target:
                return True
            if copy == mat:
                return False

        return False
