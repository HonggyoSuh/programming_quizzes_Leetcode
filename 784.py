from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i in s:
            if i.isdigit():
                ans = [c + i for c in ans]
            else:
                tmp1 = [c + i.lower() for c in ans]
                tmp2 = [c + i.upper() for c in ans]
                ans = tmp1 + tmp2
        return ans
