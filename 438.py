from collections import deque
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # queue, length_s, length_p = deque(), len(s), len(p)

        # for i in range(length_s - length_p + 1):
        #     if s[i : i + length_p] == p:
        #         queue.append(i)

        # return queue

        queue, length_s, length_p = deque(), len(s), len(p)

        if length_s < length_p:
            return queue

        base, diff = ord("a"), [0 for _ in range(26)]

        for i in range(length_p):
            diff[ord(p[i]) - base] += 1
            diff[ord(s[i]) - base] -= 1

        if diff.count(0) == 26:
            queue.append(0)

        for i in range(length_s - length_p):
            diff[ord(s[i]) - base] += 1
            diff[ord(s[i + length_p]) - base] -= 1

            if diff.count(0) == 26:
                queue.append(i + 1)

        return queue

        # queue, length_s, length_p = deque(), len(s), len(p)

        # if length_s < length_p:
        #     return queue

        # base, diff = ord("a"), [0 for _ in range(26)]

        # for i in range(length_p):
        #     diff[ord(p[i]) - base] += 1
        #     diff[ord(s[i]) - base] -= 1

        # if diff.count(0) == 26:
        #     queue.append(0)

        # for i in range(length_s - length_p):
        #     diff[ord(s[i]) - base] += 1
        #     diff[ord(s[i + length_p]) - base] -= 1

        #     if diff.count(0) == 26:
        #         queue.append(i + 1)

        # return queue
