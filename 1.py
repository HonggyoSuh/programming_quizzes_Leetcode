from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = len(nums)
        # for i in range(l):
        #     for j in range(i + 1, l):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        l = len(nums)
        for i in range(l):
            # print("i: ", i)
            subs = target - nums[i]
            newNums = nums[i + 1:]
            # print("newNums: ", newNums)
            if subs in newNums:
                # print([i, newNums.index(subs) + i + 1])
                return [i, newNums.index(subs) + i + 1]

if __name__ == "__main__":
    Solution().twoSum(list(map(int, input().split())), int(input()))