class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for index, j in enumerate(typed):
            if i < len(name) and name[i] == j:
                print(j, "if")
                i += 1
            elif index == 0 or j != typed[index - 1]:
                print(j, "false")
                return False

        return i == len(name)

        # left = right = 0
        # length1 = len(name)
        # length2 = len(typed)

        # while left <= length1 and right < length2:
        #     if left < length1 and name[left] == typed[right]:
        #         left += 1
        #         right += 1
        #     elif name[left - 1] == typed[right] and left != 0:
        #         right += 1
        #     else:
        #         return False

        # return left == length1 and right == length2
