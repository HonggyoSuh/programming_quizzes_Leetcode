class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        newP = ""
        for i in range(len(p)):
            if p[i] == "*":
                if i != 0 and p[i - 1] != "*":
                    newP += p[i - 1]
            else:
                newP += p[i]

        if len(newP) != len(s): return False
        return True

#Not completed

print(Solution().isMatch("aa", "**a."))
                
