class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        hashmap = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in list(s):
            if i in hashmap:
                stack.append(i)
            elif len(stack) == 0 or hashmap[stack.pop()] != i:
                return False

        return len(stack) == 0
