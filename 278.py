import bisect

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bisect.bisect_left(self, True, 1, n)
    
    # def __getitem__(self, key):
    #     return isBadVersion(key)