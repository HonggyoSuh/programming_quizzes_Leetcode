from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hashmap = {i: format(i, "b").count("1") for i in arr}
        arr.sort(key=lambda x: (hashmap[x], x))
        # arr.sort(key=lambda x: (format(x, "b").count("1"), x))

        # return sorted(arr, key = lambda x: (format(x, "b").count("1"), x))
        return arr
