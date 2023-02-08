class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        for i, j in zip(list(s1), list(s2)):
            if i != j:
                num += 1
            
            if num > 2:
                return False
        
        return True

        # return False if sum(i != j for i, j in zip(list(s1), list(s2))) > 2 else True