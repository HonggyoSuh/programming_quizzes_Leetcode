import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # queue = deque(magazine)

        # for i in ransomNote:
        #     if i in queue:
        #         queue.remove(i)
        #     else:
        #         return False

        # return True

        # rm = collections.Counter(ransomNote)
        # mg = collections.Counter(magazine)

        # for k, v in rm.items():
        #     if k not in mg or mg[k] < v:
        #         return False

        # return True

        return not collections.Counter(ransomNote) - collections.Counter(magazine)
