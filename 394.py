from collections import deque


class Solution(object):
    def decodeString(self, s: str) -> str:
        queue, curr_num, curr_string = deque(), 0, ""

        for char in s:
            if char == "[":
                queue.append(curr_string)
                queue.append(curr_num)
                curr_string = ""
                curr_num = 0
            elif char == "]":
                num = queue.pop()
                prev_string = queue.pop()
                curr_string = prev_string + num * curr_string
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
            else:
                curr_string += char

        return curr_string
