# Definition for singly-linked list.
from collections import deque
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr: ListNode = head
        queue: Deque[int] = deque()

        while curr:
            queue.append(curr.val)
            curr = curr.next

        return sum((2 ** (len(queue) - index - 1)) * i for index, i in enumerate(queue))

        # result = 0
        # while head:
        #     result = 2 * result + head.val
        #     head = head.next
        # return result
