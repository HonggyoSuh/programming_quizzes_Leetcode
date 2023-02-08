# import collections


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # s_queue = collections.deque(s)
        # goal_queue = collections.deque(goal)
        # result = 0

        # while s_queue != goal_queue:
        #     s_queue.rotate(1)
        #     result += 1

        #     if result > len(s):
        #         return False

        # return True

        return len(s) == len(goal) and goal in s + s
