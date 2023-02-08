from typing import Dict, List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_hashmap: Dict[str, int] = {
            i: index for index, i in enumerate(list(order))
        }

        for index1, i in enumerate(words[:-1]):
            a, b = words[index1], words[index1 + 1]

            if a != b:
                for index2, j in enumerate(order_hashmap):
                    if index2 == len(b):
                        return False
                    if index2 == len(a):
                        break

                    a_char, b_char = a[index2], b[index2]
                    a_ix, b_ix = order_hashmap[a_char], order_hashmap[b_char]

                    if a_ix < b_ix:
                        break
                    elif a_ix > b_ix:
                        return False

        return True
