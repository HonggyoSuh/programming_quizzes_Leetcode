from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in accounts:
            maximum = sum(i) if maximum < sum(i) else maximum
        
        return maximum