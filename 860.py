from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {5: 0, 10: 0}

        for i in bills:
            if i == 5:
                hashmap[5] += 1

            elif i == 10:
                hashmap[10] += 1

                if hashmap[5] > 0:
                    hashmap[5] -= 1
                else:
                    return False

            elif i == 20:
                if hashmap[10] > 0:
                    hashmap[10] -= 1
                    if hashmap[5] > 0:
                        hashmap[5] -= 1
                    else:
                        return False
                else:
                    if hashmap[5] > 2:
                        hashmap[5] -= 3
                    else:
                        return False

        return True
