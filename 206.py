# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

        # if not head:
        #     return prev

        # next, head.next = head.next, prev
        # return self.reverseList(next, head)
