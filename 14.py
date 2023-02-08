from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        i = 0
        for i, chars in enumerate(zip(*strs), start = 1):
            if len(set(chars)) != 1:
                i -= 1
                break
        
        return strs[0][:i]