from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary) / len(salary)
        # print(sum(salary) / len(salary))

if __name__ == "__main__":
    Solution().average(list(map(int, input().split())))