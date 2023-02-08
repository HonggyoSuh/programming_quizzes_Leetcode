from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        result = []
        index_sum = len(list1) + len(list2)

        for index, i in enumerate(list1):
            hashmap[i] = index

        for index, i in enumerate(list2):
            if i in hashmap:
                temp_sum = hashmap[i] + index
                if temp_sum == index_sum:
                    result.append(i)
                elif temp_sum < index_sum:
                    result = [i]
                    index_sum = temp_sum

        return result
