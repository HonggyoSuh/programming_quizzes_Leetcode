# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # result = []

        # while head:
        #     result += [head.val]
        #     head = head.next

        # left, right = 0, len(result) - 1

        # while left < right:
        #     if result[left] != result[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True

        string = ""

        while head:
            string += str(head.val)
            head = head.next

        return string == string[::-1]
