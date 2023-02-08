import collections


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        queue = collections.deque(s)

        for index, i in enumerate(s):
            if i.isalpha():
                if queue:
                    temp = queue.pop()

                    while not temp.isalpha() and queue:
                        temp = queue.pop()

                    s[index] = temp

        return "".join(s)
