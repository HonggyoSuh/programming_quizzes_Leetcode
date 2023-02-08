from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result, slow, fast = [], nums[0], nums[0]

        for i in nums[1:]:
            print(i, slow, fast)
            if i > fast + 1:
                result.append(f"{slow}->{fast}" if slow != fast else f"{slow}")
                slow, fast = i, i
            else:
                fast = i

        result.append(f"{slow}->{fast}" if slow != fast else f"{slow}")

        return result
