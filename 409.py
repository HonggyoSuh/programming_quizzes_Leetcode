import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        counter = collections.Counter(s)
        flag = False

        for i in counter:
            val = counter.get(i)

            if val % 2 == 0:
                result += val
            else:
                result += val - 1
                flag = True

        return result + 1 if flag else result

        # ss = set()
        # for letter in s:
        #     if letter not in ss:
        #         ss.add(letter)
        #     else:
        #         ss.remove(letter)
        # if len(ss) != 0:
        #     return len(s) - len(ss) + 1
        # else:
        #     return len(s)
