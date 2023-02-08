class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        while 1 > n or n not in nums:
            nums.add(n)
            n = Solution().calculation(n)
        
        return True if n == 1 else False

    def calculation(self, n: int) -> int:
        n = str(n)
        result = 0

        for i in range(len(n)):
            result += int(n[i]) ** 2
        
        return result
