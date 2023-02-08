from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # result = copy.deepcopy(words)
        # hashmap = {}
        # for i in "qwertyuiop":
        #     hashmap[i] = 1

        # for i in "asdfghjkl":
        #     hashmap[i] = 2

        # for i in "zxcvbnm":
        #     hashmap[i] = 3

        # for i in words:
        #     row = 0
        #     for j in i:
        #         print(i, j, row, hashmap[j.lower()], result)
        #         if row and hashmap[j.lower()] != row:
        #             result.remove(i)
        #             break
        #         row = hashmap[j.lower()]

        # return result

        result = []

        for i in words:
            value = set(i.lower())
            first = value.issubset(set("qwertyuiop"))
            second = value.issubset(set("asdfghjkl"))
            third = value.issubset(set("zxcvbnm"))

            if first or second or third:
                result.append(i)

        return result
