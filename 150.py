from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)

            if token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second + first)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(trunc(second / first))
            else:
                stack.append(int(token))

        return stack.pop()
