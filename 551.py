class Solution:
    def checkRecord(self, s: str) -> bool:
        # absent = 0
        # cons_late = 0

        # for i in s:
        #     if i == "P":
        #         cons_late = 0
        #     elif i == "L":
        #         cons_late += 1
        #     else:
        #         absent += 1
        #         cons_late = 0

        #     if absent > 1 or cons_late > 2:
        #         return False

        # return True

        if "LLL" in s:
            return False
        if s.count("A") >= 2:
            return False
        return True
