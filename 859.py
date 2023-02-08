class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(s) - len(set(s)) > 0

        diff = []
        for index, i in enumerate(s):
            if i != goal[index]:
                diff.append(index)

                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        return s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
